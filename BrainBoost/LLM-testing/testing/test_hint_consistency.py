import csv
import requests
import json

# Define API endpoint
API_ENDPOINT = "http://localhost:8000/api/generate_error_classification"

# Function to process CSV and convert it to a list of dictionaries
def read_csv_to_dict_array(file_path):
    data = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        currProblem = ""
        currDescription = ""
        for row in csv_reader:
            currProblem = row["Problem"] if len(row["Problem"]) > 0 else currProblem
            currDescription = row["Description"] if len(row["Description"]) > 0 else currDescription
            problem_info = {
                'Problem': currProblem,
                'Description': currDescription,
                'Wrong Answer': row['Wrong Answer']
            }
            data.append(problem_info)
    return data

# Function to make API requests and write results immediately after each successful response
def make_api_requests(data, output_file_path):
    headers = {
        'Content-Type': 'application/json'
    }
    
    # Set up the CSV file and write the header once
    field_names = ['problem', 'description', 'wrong answer', 'general_error_description', 'syntax_errors', 'conceptual_errors', 'strategic_errors', 'hint']
    with open(output_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=field_names)
        csv_writer.writeheader()
        
        # Process each question and write result after each API call
        for question in data:
            # Repeat the request for each question 10 times
            for i in range(10):
                payload = json.dumps({
                    "studentCode": question["Wrong Answer"],
                    "originalQuestion": question["Description"]
                })
                response = requests.post(url=API_ENDPOINT, headers=headers, data=payload)
                # Check for a successful response
                while response.status_code != 200:
                    response = requests.post(url=API_ENDPOINT, headers=headers, data=payload)
                    
                output = json.loads(response.text)
                res = output.get('result')
                print(f"Successfully received response of {response.status_code} for question: {question['Problem']} (Attempt {i+1})")
                
                # Parse and write the result to CSV
                question_description = question['Description']
                question_problem = question['Problem']
                wrong_answer = question['Wrong Answer']
                
                # Extract error details
                general_error_description = res.get('general_error_description', "")
                syntax_errors = res.get("errors", {}).get('syntax_errors', "")
                conceptual_errors = res.get("errors", {}).get('conceptual_errors', "")
                strategic_errors = res.get("errors", {}).get('strategic_errors', "")
                hint = res.get('hint', "")
                
                # Write to CSV immediately
                csv_writer.writerow({
                    'problem': question_problem,
                    'description': question_description,
                    'wrong answer': wrong_answer,
                    'general_error_description': general_error_description,
                    'syntax_errors': syntax_errors,
                    'conceptual_errors': conceptual_errors,
                    'strategic_errors': strategic_errors,
                    'hint': hint
                })
            break
# Main function to read input CSV and process each row
def main():
    input_file = "./dummy_error_classification_database(in).csv"
    output_file = "hint_consistency_report.csv"

    questions = read_csv_to_dict_array(input_file)
    make_api_requests(questions, output_file)
    
    print(f"Processing completed. Results written to {output_file}")

if __name__ == "__main__":
    main()
