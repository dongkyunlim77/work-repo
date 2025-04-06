import requests
import os
from typing import List, Dict

class APIClient:
    def __init__(self):
        self.base_url = os.getenv('API_URL', 'http://localhost:8000')
        self.session = requests.Session()

    def get_nonclassified_submissions(self, questionID) -> Dict:
        """Retrieve all submissions for a particular question that have not been classified yet"""
        response = self.session.get(
            f"{self.base_url}/errors/unclassified/{questionID}"
        )
        response.raise_for_status()
        return response.json()
    
    def get_unconfirmed_submissions(self, questionID, evaluator) -> Dict:
        """Retrieve all submissions that have unconfirmed errors"""
        response = self.session.get(
            f"{self.base_url}/errors/unconfirmed/{questionID}/{evaluator}"
        )
        response.raise_for_status()
        return response.json()
    
    def get_all_submissions_with_errors(self, questionID) -> Dict:
        """Retrieve all submissions for a particular question that have errors"""
        response = self.session.get(
            f"{self.base_url}/errors/all-submissions-with-errors/{questionID}"
        )
        response.raise_for_status()
        return response.json()
    
    def classify_and_store_errors(self, studentID, submissionID):
        """Classify and store errors based on a studentID and submissionID"""
        response = self.session.get(
            f"{self.base_url}/llm/classify-error-from-submission/{studentID}/{submissionID}"
        )
        response.raise_for_status()
        return response.json()
    
    def classify_errors(self, submission) -> Dict:
        """Classify an error based on a submission"""
        response = self.session.post(
            f"{self.base_url}/llm/classify-errors",
            json=submission
        )
        response.raise_for_status()
        return response.json()
    
    def generate_hint(self, submission) -> Dict:
        """Generate a hint based on a submission"""
        response = self.session.post(
            f"{self.base_url}/llm/generate-hint",
            json=submission
        )
        response.raise_for_status()
        return response.json()
    
    def get_problems(self, courseID) -> List:
        """Get all problems associated with a courseID"""
        response = self.session.get(f"{self.base_url}/problems/from-course/{courseID}")
        response.raise_for_status()
        return response.json()
    
    def get_errors(self, studentID, submissionID) -> List:
        """Get all errors associated with a submission"""
        response = self.session.get(f"{self.base_url}/errors/all-errors-for-submission/{studentID}/{submissionID}")
        response.raise_for_status()
        return response.json()
    
    def store_errors(self, courseID, studentID, submissionID, errors) -> Dict:
        """Generate a hint based on a submission"""
        response = self.session.post(
            f"{self.base_url}/errors/store-errors/{courseID}/{studentID}/{submissionID}",
            json=errors
        )
        response.raise_for_status()
        return response.json()
    
    def get_question_by_id(self, question_id: int) -> Dict:
        """Get a question by ID"""
        response = self.session.get(
            f"{self.base_url}/problems/{question_id}"
        )
        response.raise_for_status()
        return response.json()
    
    def get_submission(self, studentID: int, submissionID: int) -> Dict:
        """Get a submission by ID"""
        response = self.session.get(
            f"{self.base_url}/submissions/{studentID}/{submissionID}"
        )
        response.raise_for_status()
        return response.json()
    
    def submit_confirmations(self, errorID, evaluator, isCorrect) -> Dict:
        """Submit error classification confirmations"""
        response = self.session.get(
            f"{self.base_url}/errors/confirm-error/{errorID}/{evaluator}/{isCorrect}"
        )
        response.raise_for_status()
        return response.json()