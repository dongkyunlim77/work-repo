import gymnasium as gym
from gymnasium import spaces
import numpy as np
import json
import os

class RecommendationEnv(gym.Env):
    """
    A simple recommendation environment.
    The state is a dictionary containing:
      - descriptor: one-hot encoded descriptor for the current image.
      - dwell_time: time (in seconds) the user spent looking at the image.
      - feedback: user feedback mapped as 0 for dislike, 1 for neutral, 2 for like.
    The action is a discrete index representing the next image to recommend.
    """
    def __init__(self, pictures_folder="pictures", descriptors_file="descriptors.json", meta_descriptors_file="meta_descriptors.json"):
        super(RecommendationEnv, self).__init__()

        self.pictures_folder = pictures_folder
        self.descriptors_file = descriptors_file
        self.meta_descriptors_file = meta_descriptors_file

        # Load descriptors from JSON.
        # Expected format: {"1": [0,1,0,...], "2": [1,0,0,...], ...}
        with open(descriptors_file, "r") as f:
            self.descriptors = json.load(f)

        with open(meta_descriptors_file, "r") as f:
            self.meta_descriptors = json.load(f)

        # Assume the keys of the JSON are the image identifiers (filenames without extension)
        self.image_ids = list(self.descriptors.keys())

        # Determine the length of the descriptor vector
        example_descriptor = self.descriptors[self.image_ids[0]]
        self.descriptor_length = len(example_descriptor)

        # Define observation space:
        #   - "descriptor": one-hot vector (values 0 or 1)
        #   - "dwell_time": a float (we assume up to 1000 seconds)
        #   - "feedback": a discrete value {0: dislike, 1: neutral, 2: like}
        self.observation_space = spaces.Dict({
            "descriptor": spaces.Box(low=0, high=1, shape=(self.descriptor_length,), dtype=np.float32),
            "dwell_time": spaces.Box(low=0, high=1000, shape=(1,), dtype=np.float32),
            "feedback": spaces.Discrete(3)
        })

        # Action space: choose next image (index in the list of image_ids)
        self.action_space = spaces.Discrete(len(self.image_ids))

        self.current_image = None
        self.current_meta_descriptor = ""

    def reset(self):
        # Start with a random image.
        idx = np.random.randint(len(self.image_ids))
        self.current_image = self.image_ids[idx]
        # Reset observation: dwell_time=0, neutral feedback (mapped to 1)
        obs = {
            "descriptor": np.array(self.descriptors[self.current_image], dtype=np.float32),
            "dwell_time": np.array([0.0], dtype=np.float32),
            "feedback": 1
        }
        return obs

    def step(self, action, dwell_time, feedback):
        """
        Executes one recommendation step.
          - action: index of the next image.
          - dwell_time: how long the user viewed the previous image.
          - feedback: string "like", "dislike", or "neutral".
        Returns: next_obs, reward, done, info.
        """
        # --- Compute reward for the old state (the image just viewed) ---
        # Map textual feedback to a discrete number:
        if feedback == "like":
            fb = 2
        elif feedback == "dislike":
            fb = 0
        else:
            fb = 1

        # Calculate reward based on dwell time and feedback for the old image.
        if dwell_time > 2:
            reward = dwell_time
        else:
            reward = 0
        if feedback == "like":
            reward += 10.0
        elif feedback == "dislike":
            reward -= 10.0

        print(f"Current reward: {reward}")

        # --- Transition to the new state ---
        # Now set the new current image
        self.current_image = self.image_ids[action]
        descriptor_vector = self.descriptors[self.current_image]

        # Compute meta descriptor based on the one-hot encoding.
        self.current_meta_descriptor = self.compute_meta_descriptor(descriptor_vector)

        # Build observation for the new state.
        # Reset dwell time and feedback for the new image.
        obs = {
            "descriptor": np.array(descriptor_vector, dtype=np.float32),
            "dwell_time": np.array([0.0], dtype=np.float32),
            "feedback": 1,  # reset to neutral for the new image
            "meta_descriptor": self.current_meta_descriptor
        }

        done = False  # This environment runs indefinitely.
        info = {"current_image": self.current_image}

        return obs, reward, done, info

    def render(self, mode="human"):
        # Optional: print current state info.
        print(f"Current image: {self.current_image}")

    def compute_meta_descriptor(self, descriptor_vector):
        """
        Given a one-hot descriptor vector, compute a string that represents
        the Pokémon types by looking up active indices in the meta_descriptors dict.
        """
        types = []
        for i, flag in enumerate(descriptor_vector):
            if flag == 1:
                type_str = self.meta_descriptors.get(str(i), None)
                if type_str is not None:
                    types.append(type_str)
        return "/".join(types) if types else "Unknown"
