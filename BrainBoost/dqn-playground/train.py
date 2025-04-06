import gym
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import random
import json
from model import DQN
from environment import BrainBoostEnv

# Initialize Gym environment (using offline data)
env = BrainBoostEnv(data_path="experience_replay.json")


# Hyperparameters
gamma = 0.95  # Discount factor
lr = 1e-4     # Learning rate 0.0001
batch_size = 16
hidden_dim = 128
input_dim = 6  # Adjust according to your state space size
output_dim = env.action_space.n  # Number of possible actions (next question or stay)

model = DQN(input_dim=input_dim, hidden_dim=hidden_dim, output_dim=output_dim)
optimizer = optim.Adam(model.parameters(), lr=lr)


# Replay buffer
class ReplayBuffer:
    def __init__(self, max_size=10000):
        self.buffer = []
        self.max_size = max_size

    def push(self, experience):
        if len(self.buffer) >= self.max_size:
            self.buffer.pop(0)  # Remove oldest experience
        self.buffer.append(experience)

    def sample(self, batch_size):
        return random.sample(self.buffer, batch_size)

    def __len__(self):
        return len(self.buffer)
    def _get_buffer(self):
        return  self.buffer
    
    def clear(self):
        self.buffer = []

replay_buffer = ReplayBuffer()

# Training loop
num_epochs = 200
state = env.reset()
finished = False

for epoch in range(num_epochs):
    if finished:
        state = env.reset()
        finished = False
    done = False
    while not done:
        # Choose action (use epsilon-greedy for exploration)
        state_tensor = torch.Tensor(state).unsqueeze(0)
        q_values = model(state_tensor)
        action = torch.argmax(q_values, dim=1).item()

        # Take step in the environment
        next_state, reward, done, is_finished = env.step(action) # note this action does not do anything because offline training data already has actions
        
        if is_finished:
            print("environment reset")
            finished = True
            break
        # Store experience in replay buffer
        replay_buffer.push((state, action, reward, next_state))
        
       
        if done: # run it by student submission
            # do we need this > len(replay_buffer) >= batch_size

            # print(len(replay_buffer))
            batch = replay_buffer._get_buffer() 
            states, actions, rewards, next_states = zip(*batch)

           # Convert to tensors
            states_tensor = torch.tensor(states, dtype=torch.float32)
            next_states_tensor = torch.tensor([ns if ns is not None else np.zeros_like(state) for ns in next_states], dtype=torch.float32)
            actions_tensor = torch.tensor(actions, dtype=torch.long)
            rewards_tensor = torch.tensor(rewards, dtype=torch.float32)

            # Compute Q-values for states and next statesex
            q_values = model(states_tensor)  # (batch_size, action_dim)
            next_q_values = model(next_states_tensor)  # (batch_size, action_dim)

            # Compute target total rewards (immediate and future ) Q-values using the Bellman equation
            target_q_values = rewards_tensor + gamma * torch.max(next_q_values, dim=1)[0]
            target_q_values = torch.where(next_states_tensor.sum(dim=1) == 0, rewards_tensor, target_q_values)  # Handle terminal states

            # Immediate Reward
            action_q_values = q_values.gather(1, actions_tensor.unsqueeze(1))  # (batch_size, 1) 

            # Compute the loss
            loss = nn.MSELoss()(action_q_values.squeeze(1), target_q_values)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            replay_buffer.clear()
    if epoch % 1 == 0 and finished is False:
        print(f"Epoch {epoch}, Loss: {loss.item()}")

torch.save(model.state_dict(), "dqn_brainboost.pth")
