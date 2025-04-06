import streamlit as st
from streamlit_ace import st_ace
import pandas as pd
import ast
import io
import matplotlib.pyplot as plt
from utils import APIClient


course = 32180
# course = 12345
client = APIClient()

if "evaluator" not in st.session_state:
    st.session_state["evaluator"] = ""
if "selectedProblem" not in st.session_state:
    st.session_state["selectedProblem"] = None
if "problems" not in st.session_state:
    st.session_state["problems"] = []
if "unconfirmed" not in st.session_state:
    st.session_state["unconfirmed"] = []
if "allSubmissions" not in st.session_state:
    st.session_state["allSubmissions"] = []
if "currentProblem" not in st.session_state:
    st.session_state["currentProblem"] = {}
if "submissionID" not in st.session_state:
    st.session_state["submissionID"] = {}
if "submission" not in st.session_state:
    st.session_state["submission"] = {}
if "errors" not in st.session_state:
    st.session_state["errors"] = {}


st.title("Error Analysis Dashboard")
st.write("Use this dashboard to manually confirm LLM-generated errors.")

st.session_state.evaluator = st.text_input("Please enter your first name:").lower()

if st.session_state.evaluator:

    if not st.session_state.problems:
        st.session_state.problems = client.get_problems(course)

    funcNames = [problem["functionName"] for problem in st.session_state.problems]
    selectedProblem = st.selectbox("Select a Question:", [""] + funcNames)

    if selectedProblem:
        selectedProblem = funcNames.index(selectedProblem)

        # Decide whether you need to refresh the problem
        if st.session_state.selectedProblem != selectedProblem:
            st.session_state.selectedProblem = selectedProblem
            changedProblem = True
        else:
            changedProblem = False

        questionID = st.session_state.problems[st.session_state.selectedProblem]["id"]
        st.session_state.unconfirmed = client.get_unconfirmed_submissions(questionID, st.session_state.evaluator)
        st.session_state.allSubmissions = client.get_all_submissions_with_errors(questionID)

        # Display question
        if changedProblem:
            st.session_state.currentProblem = client.get_question_by_id(questionID)

        problem_id = st.session_state.currentProblem['id']
        function_name = st.session_state.currentProblem['functionName']
        parameters = st.session_state.currentProblem['parameters']
        num_parameters = len(parameters.split(','))
        returns = st.session_state.currentProblem['returns']
        description = st.session_state.currentProblem['description']
        example = st.session_state.currentProblem['example']
        test_cases = (st.session_state.currentProblem['testCases'])

        st.header(f"**Problem**: `{function_name}()`")
        st.markdown(f"**Parameters**: {parameters}")
        st.markdown(f"**Returns**: {returns}")
        st.markdown(f"**Description**: {description}")
        st.write(f"Example:")
        st.code(example)    

        st.divider()

        # Progress of confirming errors
        if len(st.session_state.allSubmissions) == 0:
            st.subheader("No errors to confirm!")
        else:

            col1, col2 = st.columns([1, 4])

            with col1:
                st.write(f"{(len(st.session_state.allSubmissions) - len(st.session_state.unconfirmed))} / {len(st.session_state.allSubmissions)} Completed")

            with col2:
                st.progress((len(st.session_state.allSubmissions) - len(st.session_state.unconfirmed)) / len(st.session_state.allSubmissions))


            if len(st.session_state.unconfirmed) == 0:
                st.subheader("Finished confirming all errors!")
            else:

                # Choose a submission to confirm
                submissionID = st.session_state.unconfirmed[0]   # A dictionary of studentID and submissionID

                # Decide whether you need to refresh the submission
                if submissionID != st.session_state.submissionID:
                    st.session_state.submission = client.get_submission(submissionID["studentID"], submissionID["submissionID"])
                    st.session_state.errors = client.get_errors(submissionID["studentID"], submissionID["submissionID"])

                st.subheader("Student Code:")
                st.write(f"Student {submissionID['studentID']}, Submission {submissionID['submissionID']}")

                st.code(st.session_state.submission["code"], language="python", line_numbers=True)

                st.subheader("Error Classification:")
                st.write("The errors listed below have been classified by the LLM. Check off all rows you believe contain errors that **exist** and are **correctly classified**.")

                errorIDs = []

                with st.form(f"submission-{submissionID['studentID']}-{submissionID['submissionID']}"):
                    if st.session_state.errors["errors"]["syntax_errors"]:
                        st.subheader("Syntax Errors:")
                        for error in st.session_state.errors["errors"]["syntax_errors"]:
                            st.checkbox(error["error_description"], key=f"{error['error_id']}")
                            errorIDs.append(f"{error['error_id']}")

                    if st.session_state.errors["errors"]["conceptual_errors"]:
                        st.subheader("Conceptual Errors:")
                        for error in st.session_state.errors["errors"]["conceptual_errors"]:
                            st.checkbox(error["error_description"], key=f"{error['error_id']}")
                            errorIDs.append(f"{error['error_id']}")

                    if st.session_state.errors["errors"]["strategic_errors"]:
                        st.subheader("Strategic Errors:")
                        for error in st.session_state.errors["errors"]["strategic_errors"]:
                            st.checkbox(error["error_description"], key=f"{error['error_id']}")
                            errorIDs.append(f"{error['error_id']}")

                    submittedForm = st.form_submit_button("Submit Confirmations", use_container_width=True)

                # Submit responses to database
                if submittedForm:
                    for errorID in errorIDs:
                        isCorrect = 1 if st.session_state[errorID] else 0
                        client.submit_confirmations(errorID, st.session_state.evaluator, isCorrect)
                    st.rerun()


            

                


        





