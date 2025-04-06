import pandas as pd
import json
from collections import defaultdict
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

# Load dataset
df = pd.read_csv("student_submissions.csv", sep=";")
df = df.sort_values(by=["username", "timestamp"])

# Normalize numerical values
# scaler = MinMaxScaler()
# df[["duration", "keystrokes", "attempts"]] = scaler.fit_transform(df[["duration", "keystrokes", "attempts"]])

# Encode categorical values

topic_encoder = LabelEncoder()
df["topic"] = topic_encoder.fit_transform(df["topic"])

# Group submissions by student and question
user_sessions = defaultdict(lambda: defaultdict(list))

for _, row in df.iterrows():
    user_sessions[row["username"]][row["problem_id"]].append(row)

# Create experience replay memory
experience_replay = []

for username, problems in user_sessions.items():
    problem_keys = list(problems.keys())  # Order of problems attempted
    for i, problem_id in enumerate(problem_keys):
        submissions = problems[problem_id]
        action = -1
        for j in range(len(submissions)):
            
            state = {
                "submission_history": submissions[j]["code"],  # Track the code of the current submission
                "durations": submissions[j]["duration"],  # Duration of the current submission
                "keystrokes": submissions[j]["keystrokes"],  # Keystrokes of the current submission
                "attempts": submissions[j]["attempts"],  # Attempts for the current submission
                "test_case_accuracy": submissions[j]["test_cases_passed"] / submissions[j]["total_test_cases"],  # Accuracy for the current submission
                "difficulty": submissions[j]["difficulty"],  # Difficulty of the current submission
                "topic": submissions[j]["topic"],  # Topic of the current submission
                "current_problem": problem_id  # Current problem ID
            }


            # Determine the next state
            if j < len(submissions) - 1:
                # Next state is the next submission of the same problem
                next_submission = submissions[j + 1]
                next_state = {
                    "submission_history": next_submission["code"],  # Code of the next submission
                    "durations": next_submission["duration"],  # Duration of the next submission
                    "keystrokes": next_submission["keystrokes"],  # Keystrokes of the next submission
                    "attempts": next_submission["attempts"],  # Attempts for the next submission
                    "test_case_accuracy": next_submission["test_cases_passed"] / next_submission["total_test_cases"],  # Accuracy for the next submission
                    "difficulty": next_submission["difficulty"],  # Difficulty of the next submission
                    "topic": next_submission["topic"],  # Topic of the next submission
                    "current_problem": problem_id  # Current problem ID
                }
                action = problem_id
            elif i < len(problem_keys) - 1:
                # Next state is the first submission of the next problem
                next_problem = problem_keys[i + 1]
                next_submission = problems[next_problem][0]
                next_state = {
                    "submission_history": next_submission["code"],
                    "durations": next_submission["duration"],
                    "keystrokes": next_submission["keystrokes"],
                    "attempts": next_submission["attempts"],
                    "test_case_accuracy": next_submission["test_cases_passed"] / next_submission["total_test_cases"],
                    "difficulty": next_submission["difficulty"],
                    "topic": next_submission["topic"],
                    "current_problem": next_problem
                }
                action = next_problem
            else:
                next_state = None  # No further data

            # # Reward: Improvement in test case accuracy or reduced attempts
            # reward = (state["test_case_accuracy"][-1] - state["test_case_accuracy"][0]) - (0.05 * state["attempts"][-1])

            experience_replay.append({
                "state": state,
                "action": action,  # The AI picks which problem to recommend
                "next_state": next_state if next_state else None,
                "done": next_state is None
            })

# Save experiences
with open("experience_replay.json", "w") as f:
    json.dump(experience_replay, f, indent=4)
