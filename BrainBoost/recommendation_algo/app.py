import streamlit as st
import time
import os
from PIL import Image
import numpy as np

# Import the environment and DQN agent.
from recommendation_env import RecommendationEnv
from dqn_agent import DQNAgent

def flatten_obs(obs):
    """
    Flattens the observation dictionary into a 1D numpy array.
    The state vector is a concatenation of:
      - the descriptor vector,
      - the dwell_time (1 element),
      - the feedback (converted to float).
    """
    return np.concatenate([
        obs["descriptor"],
        obs["dwell_time"],
        np.array([obs["feedback"]], dtype=np.float32)
    ])

# Initialize the environment.
env = RecommendationEnv(pictures_folder="pictures", descriptors_file="descriptors.json", meta_descriptors_file="meta_descriptors.json")

# Initialize Streamlit session state (only once).
if "env_obs" not in st.session_state:
    st.session_state.env_obs = env.reset()
    st.session_state.image_id = env.current_image  # image identifier from the env
    st.session_state.meta_descriptor = env.current_meta_descriptor  # image identifier from the env
    st.session_state.start_time = time.time()
    st.session_state.feedback = "neutral"  # feedback is one of "like", "dislike", "neutral"

if "dqn_agent" not in st.session_state:
    # Our state is: descriptor_length + dwell_time (1) + feedback (1)
    state_size = env.descriptor_length + 1 + 1
    action_size = len(env.image_ids)
    st.session_state.dqn_agent = DQNAgent(state_size, action_size)

# Display the current image.
image_path = os.path.join("pictures", f"{st.session_state.image_id}.png")
if os.path.exists(image_path):
    #st.image(Image.open(image_path), use_container_width=True)
    st.image(Image.open(image_path), width=200)
else:
    st.write("Image not found:", image_path)

# Display the dwell time.
current_time = time.time()
st.write(f"Current Pokemon type: {st.session_state.meta_descriptor}")

# Provide Like and Dislike buttons.
col1, col2 = st.columns(2)
with col1:
    if st.button("Like"):
        st.session_state.feedback = "like"
with col2:
    if st.button("Dislike"):
        st.session_state.feedback = "dislike"

# When the user clicks "Next", process the current state and pick a new image.
if st.button("Next"):
    # Convert current observation to a flat vector.
    current_flat_state = flatten_obs(st.session_state.env_obs)

    # Define a simple heuristic: here, random selection.
    def heuristic_policy(state):
        return np.random.randint(len(env.image_ids))

    # For cold start, you may want to use the heuristic.
    # Here we decide to use it if epsilon is above a threshold.
    use_heuristic = st.session_state.dqn_agent.epsilon > 0.9

    # Select an action (i.e. next image index).
    action = st.session_state.dqn_agent.act(current_flat_state, use_heuristic, heuristic_policy)

    # Call the environment’s step function.
    dwell_time = current_time - st.session_state.start_time
    next_obs, reward, done, info = env.step(action, dwell_time, st.session_state.feedback)

    # Store the experience in replay memory.
    next_flat_state = flatten_obs(next_obs)
    st.session_state.dqn_agent.remember(current_flat_state, action, reward, next_flat_state, done)

    # Perform a training step.
    st.session_state.dqn_agent.replay()

    # Update session state for the next image.
    st.session_state.env_obs = next_obs
    st.session_state.image_id = env.current_image
    st.session_state.meta_descriptor = env.current_meta_descriptor
    st.session_state.start_time = time.time()
    st.session_state.feedback = "neutral"

    # Rerun the app to display the new image.
    st.rerun()
