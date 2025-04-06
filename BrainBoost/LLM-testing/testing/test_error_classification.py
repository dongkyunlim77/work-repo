import csv
import requests
import json

API_ENDPOINT = "http://localhost:8000/api/generate_error_classification"
def read_csv_to_dict_array(file_path):
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as csv_file:
            # Read first row to check headers
            csv_reader = csv.reader(csv_file)
            headers = next(csv_reader)
            
            # Find the correct column names
            problem_col = next((i for i, h in enumerate(headers) if 'problem' in h.lower()), None)
            desc_col = next((i for i, h in enumerate(headers) if 'description' in h.lower()), None)
            answer_col = next((i for i, h in enumerate(headers) if 'answer' in h.lower()), None)
            
            if any(col is None for col in [problem_col, desc_col, answer_col]):
                raise ValueError("Required columns not found in CSV")
            
            # Reset file pointer
            csv_file.seek(0)
            csv_reader = csv.DictReader(csv_file)
            
            data = []
            curr_problem = ""
            curr_description = ""
            
            for row in csv_reader:
                row_dict = dict(row)
                problem_key = headers[problem_col]
                desc_key = headers[desc_col]
                answer_key = headers[answer_col]
                
                curr_problem = row_dict[problem_key] if row_dict[problem_key].strip() else curr_problem
                curr_description = row_dict[desc_key] if row_dict[desc_key].strip() else curr_description
                
                problem_info = {
                    'Problem': curr_problem,
                    'Description': curr_description,
                    'Wrong Answer': row_dict[answer_key]
                }
                data.append(problem_info)
                
            return data
    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
        return []
    except Exception as e:
        print(f"Error reading CSV: {str(e)}")
        return []

def make_api_requests(data, output_file_path):
    headers = {'Content-Type': 'application/json'}
    
    field_names = ['problem', 'description', 'wrong answer', 'general_error_description', 
                   'syntax_errors', 'conceptual_errors', 'strategic_errors', 'hint']
    
    try:
        with open(output_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=field_names)
            csv_writer.writeheader()
            
            for question in data:
                try:
                    payload = json.dumps({
                        "studentCode": question["Wrong Answer"],
                        "originalQuestion": question["Description"]
                    })
                    
                    max_retries = 3
                    retry_count = 0
                    
                    while retry_count < max_retries:
                        try:
                            response = requests.post(API_ENDPOINT, headers=headers, data=payload)
                            response.raise_for_status()
                            output = response.json()
                            res = output.get('result', {})
                            
                            if res.get('hint'):
                                break
                            
                        except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
                            print(f"Error in API request: {str(e)}")
                            retry_count += 1
                            if retry_count == max_retries:
                                print(f"Max retries reached for question: {question['Problem']}")
                                continue
                    
                    csv_writer.writerow({
                        'problem': question['Problem'],
                        'description': question['Description'],
                        'wrong answer': question['Wrong Answer'],
                        'general_error_description': res.get('general_error_description', ''),
                        'syntax_errors': res.get('errors', {}).get('syntax_errors', ''),
                        'conceptual_errors': res.get('errors', {}).get('conceptual_errors', ''),
                        'strategic_errors': res.get('errors', {}).get('strategic_errors', ''),
                        'hint': res.get('hint', '')
                    })
                    
                    print(f"Successfully processed question: {question['Problem']}")
                    
                except Exception as e:
                    print(f"Error processing question {question['Problem']}: {str(e)}")
                    continue
                    
    except Exception as e:
        print(f"Error writing to output file: {str(e)}")

def main():
    input_file = "../data/hint_pipeline_test.csv"
    output_file = "../data/hint_pipeline_report.csv"

    questions = read_csv_to_dict_array(input_file)
    if questions:
        make_api_requests(questions, output_file)
        print(f"Processing completed. Results written to {output_file}")
    else:
        print("No data to process")

if __name__ == "__main__":
    main()