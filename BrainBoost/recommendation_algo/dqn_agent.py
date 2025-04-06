import numpy as np
import random
import torch
import torch.nn as nn
import torch.optim as optim
from collections import deque

class DQN(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(DQN, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, output_dim)
        )
    def forward(self, x):
        return self.net(x)

class DQNAgent:
    """
    A simple Deep Q-Network agent.
    """
    def __init__(
        self,
        state_size,
        action_size,
        lr=1e-3,
        gamma=0.99,
        epsilon=1.0,
        epsilon_min=0.1,
        epsilon_decay=0.995,
        batch_size=32,
        memory_size=10000
    ):
        self.state_size = state_size
        self.action_size = action_size
        self.lr = lr
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_min = epsilon_min
        self.epsilon_decay = epsilon_decay
        self.batch_size = batch_size

        self.memory = deque(maxlen=memory_size)

        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = DQN(state_size, action_size).to(self.device)
        self.optimizer = optim.Adam(self.model.parameters(), lr=lr)
        self.loss_fn = nn.MSELoss()

    def remember(self, state, action, reward, next_state, done):
        """Stores experience in replay memory."""
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state, use_heuristic=False, heuristic_policy=None):
        """
        Returns an action for the given state.
        If `use_heuristic` is True and a heuristic_policy function is provided, it is used.
        Otherwise, the agent acts epsilon-greedily.
        """
        if use_heuristic and heuristic_policy is not None:
            return heuristic_policy(state)
        if np.random.rand() <= self.epsilon:
            return np.random.randint(self.action_size)
        state_tensor = torch.FloatTensor(state).unsqueeze(0).to(self.device)
        with torch.no_grad():
            q_values = self.model(state_tensor)
        return int(torch.argmax(q_values[0]).item())

    def replay(self):
        """Trains the network on a batch of experiences."""
        if len(self.memory) < self.batch_size:
            return
        minibatch = random.sample(self.memory, self.batch_size)
        states, targets = [], []
        for state, action, reward, next_state, done in minibatch:
            state_tensor = torch.FloatTensor(state).to(self.device)
            next_state_tensor = torch.FloatTensor(next_state).to(self.device)
            target = reward
            if not done:
                with torch.no_grad():
                    target = reward + self.gamma * torch.max(self.model(next_state_tensor.unsqueeze(0))[0]).item()
            # Get current Q-values and update only the chosen action.
            current_q = self.model(state_tensor.unsqueeze(0))[0]
            target_f = current_q.clone().detach()
            target_f[action] = target
            states.append(state_tensor)
            targets.append(target_f)

        states_tensor = torch.stack(states)
        targets_tensor = torch.stack(targets)

        self.optimizer.zero_grad()
        predictions = self.model(states_tensor)
        loss = self.loss_fn(predictions, targets_tensor)
        loss.backward()
        self.optimizer.step()

        # Decay epsilon
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay
