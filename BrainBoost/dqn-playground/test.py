
import gym
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import random
import json
from model import DQN
from environment import BrainBoostEnv



# Load the trained model
model = DQN(6, 128, 20)  # Ensure this matches the architecture
model.load_state_dict(torch.load("dqn_brainboost.pth"))
model.eval()  # Set to evaluation mode


# Load experience replay data
with open("experience_replay.json", "r") as f:
    experiences = json.load(f)

submission_ind = np.random.randint(0, len(experiences)- 1)
sample_experience = experiences[submission_ind]  # You can loop through different ones
state_dict = sample_experience["state"]

# Convert to a tensor (flatten the dictionary)
def preprocess_state(state):
    return torch.tensor([
        state["durations"],
        state["keystrokes"],
        state["attempts"],
        state["test_case_accuracy"],
        state["difficulty"],
        state["topic"]
    ], dtype=torch.float32).unsqueeze(0)  # Add batch dimension

state_tensor = preprocess_state(state_dict)
print(state_dict)


with torch.no_grad():  # Disable gradients for inference
    q_values = model(state_tensor)
    recommended_action = torch.argmax(q_values, dim=1).item()
print (q_values)
print(f"Recommended next question ID: {recommended_action}")
