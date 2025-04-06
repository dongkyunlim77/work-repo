import os
from datetime import datetime
from typing import List, Dict
from pprint import pprint
from tqdm import tqdm
from utils import APIClient
    
client = APIClient()

questionID = 21420250

nonClassifiedSubmissions = client.get_nonclassified_submissions(questionID)

for submissionDict in tqdm(nonClassifiedSubmissions):
    studentID = submissionDict["studentID"]
    submissionID = submissionDict["submissionID"]
    client.classify_and_store_errors(studentID, submissionID)





