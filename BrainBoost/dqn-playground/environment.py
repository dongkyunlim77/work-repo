# environment.py
import gym
from gym import spaces
import json
import numpy as np

class BrainBoostEnv(gym.Env):

    def __init__(self, data_path="experience_replay.json"):
        super(BrainBoostEnv, self).__init__()

        # Load offline experience replay data
        with open(data_path, "r") as f:
            self.experiences = json.load(f)

        self.current_index = 0  # Track current experience

        # Define observation space (flattened state vector)
        obs_size = self._get_observation_size()
        self.observation_space = spaces.Box(low=0, high=1, shape=(obs_size,), dtype=np.float32)

        # Define action space (number of unique problems)
        self.problem_ids = sorted(set(exp["action"] for exp in self.experiences))
        self.action_space = spaces.Discrete(len(self.problem_ids))

        # Map problem ID to action index

        # save this so we can use for the test.py
        self.problem_id_to_action = {pid: i for i, pid in enumerate(self.problem_ids)}
        self.action_to_problem_id = {i: pid for pid, i in self.problem_id_to_action.items()}
        with open('action_to_prob_id.json', 'w') as f:
            json.dump(self.action_to_problem_id, f)

    def reset(self):
        """ Resets the environment and returns the first state. """
        self.current_index = 0
        return self._get_observation(self.experiences[self.current_index]["state"])

    def step(self, action):
        """ Takes an action (recommending a problem) and returns (next_state, reward, done). """
        exp = self.experiences[self.current_index]

        # Get mapped problem ID from action
        chosen_problem_id = self.action_to_problem_id[action]

        # Compute reward dynamically
        reward = self._compute_reward(exp["state"], exp["next_state"]) if exp["next_state"] else -1
        # print(reward)
        # Determine next state
        next_state = self._get_observation(exp["next_state"]) if exp["next_state"] else None
        done = exp["next_state"] is None

        # Move to next experience
        self.current_index += 1 
        is_finished = self._is_finished()

        return next_state, reward, done, is_finished

    def _is_finished(self):
        if self.current_index >= len(self.experiences):
            return True
        else:
            return False
    def _get_observation_size(self):
        """ Determines observation size based on the first state in dataset. """
        sample_state = self.experiences[0]["state"]
        return len(self._flatten_state(sample_state))

    def _get_observation(self, state_dict):
        """ Converts state dictionary into a flat NumPy array. """
        return np.array(self._flatten_state(state_dict), dtype=np.float32)

    def _flatten_state(self, state_dict):
        """ Flattens the state dictionary into a feature vector. """
        #do we need topic?, we dont need submission history
        return [
            state_dict["durations"],  # Latest submission duration
            state_dict["keystrokes"],  # Latest submission keystrokes
            state_dict["attempts"],  # Number of attempts
            state_dict["test_case_accuracy"],  # Latest test case accuracy
            state_dict["difficulty"],  # Problem difficulty
            state_dict["topic"]  # Problem topic
        ]

    def _compute_reward(self, state, next_state):
        """ Computes reward based on student improvement. """
        if not next_state:
            return 0  # Negative reward if no next state
        reward = 0.0
        # mastery_level = state.get("mastery_level", 0.5)
        problem_difficulty = state.get("difficulty", 1)
        accuracy_improvement = next_state["test_case_accuracy"] - state["test_case_accuracy"]

        if accuracy_improvement > 0:
            reward += (accuracy_improvement * 2) * problem_difficulty # * (1 - mastery_level)
        elif accuracy_improvement == 0:
            reward -= 0.2
        else:
            reward -= 1.0
        
        if state["current_problem"] != next_state["current_problem"]: # skipped or completed problem
            if next_state["test_case_accuracy"] == 1.0:
                reward += 1.5 * problem_difficulty
            elif next_state["test_case_accuracy"] >= 0.75:
                reward += 0.7 * problem_difficulty
            elif next_state["test_case_accuracy"] >= 0.5:
                reward += 0.5
            elif next_state["test_case_accuracy"] > 0 :
                reward += 0.1
            else:
                reward -= 0.5
        
        attempt_penalty = 0.1 * (next_state["attempts"] - state["attempts"])
        time_penalty = 0.05  * (next_state["durations"] - state["durations"])
        keystroke_penalty = 0.05 * (next_state["keystrokes"] - state["keystrokes"])
        total_penalty = attempt_penalty + time_penalty + keystroke_penalty

        reward -= total_penalty

        return reward

    def render(self, mode="human"):
        pass
