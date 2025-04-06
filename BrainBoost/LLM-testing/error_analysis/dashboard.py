import streamlit as st
import pandas as pd
import ast
import io
import matplotlib.pyplot as plt

# Load data from CSV file
uploaded_file = st.file_uploader("Upload your CSV file", type="csv")
if uploaded_file is not None:
    # Read the CSV into a DataFrame
    if 'df' not in st.session_state:
        df = pd.read_csv(uploaded_file)
        # Strip whitespace from column headers and make them lowercase
        df.columns = df.columns.str.strip().str.lower()

        # Initialize confirmation columns if they don't exist
        for idx, row in df.iterrows():
            if pd.notna(row["syntax_errors"]):
                syntax_errors = ast.literal_eval(row["syntax_errors"])
                for i in range(len(syntax_errors)):
                    col_name = f"syntax_error_{i+1}_confirmed"
                    if col_name not in df.columns:
                        df[col_name] = False

            if pd.notna(row["conceptual_errors"]):
                conceptual_errors = ast.literal_eval(row["conceptual_errors"])
                for i in range(len(conceptual_errors)):
                    col_name = f"conceptual_error_{i+1}_confirmed"
                    if col_name not in df.columns:
                        df[col_name] = False

            if pd.notna(row["strategic_errors"]):
                strategic_errors = ast.literal_eval(row["strategic_errors"])
                for i in range(len(strategic_errors)):
                    col_name = f"strategic_error_{i+1}_confirmed"
                    if col_name not in df.columns:
                        df[col_name] = False

        st.session_state['df'] = df
    else:
        df = st.session_state['df']

    # Display title and the full dataset
    st.title("Error Analysis Dashboard")
    st.subheader("Full Data Table")
    st.dataframe(df)

    # Select a row from the dropdown menu
    if st.session_state.get('selected_row') is None:
        st.session_state['selected_row'] = None

    row_indices = df.index.tolist()
    selected_index = st.selectbox("Select a Row", options=row_indices)

    # Update selected row in session state
    if st.session_state['selected_row'] != selected_index:
        st.session_state['selected_row'] = selected_index

    if st.session_state['selected_row'] is not None:
        selected_data = df.loc[st.session_state['selected_row']]

        # Display problem description
        st.subheader("Problem Description")
        st.write(selected_data["description"])

        # Display student solution
        st.subheader("Student Solution")
        st.code(selected_data["wrong answer"], language='python')

        # Display error analysis
        st.subheader("Error Analysis")
        st.write("General Error Description:")
        st.write(selected_data["general_error_description"])

        # Checkbox inputs for error validation
        st.write("Syntax Errors:")
        if pd.notna(selected_data["syntax_errors"]):
            syntax_errors = ast.literal_eval(selected_data["syntax_errors"])
            for idx, error in enumerate(syntax_errors):
                st.write(f"- {error['error_description']} (Line {error['error_line']})")
                col_name = f"syntax_error_{idx+1}_confirmed"
                is_correct = st.checkbox(
                    f"Confirm Syntax Error {idx+1} is correct",
                    key=f"syntax_{st.session_state['selected_row']}_{idx}",
                    value=selected_data[col_name]
                )
                df.at[st.session_state['selected_row'], col_name] = is_correct

        st.write("Conceptual Errors:")
        if pd.notna(selected_data["conceptual_errors"]):
            conceptual_errors = ast.literal_eval(selected_data["conceptual_errors"])
            for idx, error in enumerate(conceptual_errors):
                st.write(f"- {error['error_description']} (Line {error['error_line']})")
                col_name = f"conceptual_error_{idx+1}_confirmed"
                is_correct = st.checkbox(
                    f"Confirm Conceptual Error {idx+1} is correct",
                    key=f"conceptual_{st.session_state['selected_row']}_{idx}",
                    value=selected_data[col_name]
                )
                df.at[st.session_state['selected_row'], col_name] = is_correct

        st.write("Strategic Errors:")
        if pd.notna(selected_data["strategic_errors"]):
            strategic_errors = ast.literal_eval(selected_data["strategic_errors"])
            for idx, error in enumerate(strategic_errors):
                st.write(f"- {error['error_description']} (Line {error['error_line']})")
                col_name = f"strategic_error_{idx+1}_confirmed"
                is_correct = st.checkbox(
                    f"Confirm Strategic Error {idx+1} is correct",
                    key=f"strategic_{st.session_state['selected_row']}_{idx}",
                    value=selected_data[col_name]
                )
                df.at[st.session_state['selected_row'], col_name] = is_correct

        # Display hint
        st.subheader("Hint")
        st.write(selected_data["hint"])

    # Graphs to visualize number of errors per problem
    st.subheader("Error Analysis Summary")

    # Calculate the number of each type of error per problem
    df['num_syntax_errors'] = df['syntax_errors'].apply(lambda x: len(ast.literal_eval(x)) if pd.notna(x) else 0)
    df['num_conceptual_errors'] = df['conceptual_errors'].apply(lambda x: len(ast.literal_eval(x)) if pd.notna(x) else 0)
    df['num_strategic_errors'] = df['strategic_errors'].apply(lambda x: len(ast.literal_eval(x)) if pd.notna(x) else 0)

    # Plot the number of errors per problem as a stacked histogram
    st.write("Number of Errors per Problem (Stacked Histogram):")
    error_summary = df.groupby('problem')[['num_syntax_errors', 'num_conceptual_errors', 'num_strategic_errors']].mean()
    fig, ax = plt.subplots()
    error_summary.plot(kind='bar', stacked=True, ax=ax)
    plt.xticks(rotation=90)
    plt.ylabel("Average Number of Errors")
    plt.legend(title="Error Type")
    st.pyplot(fig)

    # Calculate the number of confirmed errors per problem
    st.write("Confirmed Errors per Problem (Stacked Histogram):")
    df['num_syntax_confirmed'] = df.filter(like='syntax_error_').sum(axis=1)
    df['num_conceptual_confirmed'] = df.filter(like='conceptual_error_').sum(axis=1)
    df['num_strategic_confirmed'] = df.filter(like='strategic_error_').sum(axis=1)

    confirmed_summary = df.groupby('problem')[['num_syntax_confirmed', 'num_conceptual_confirmed', 'num_strategic_confirmed']].mean()
    fig, ax = plt.subplots()
    confirmed_summary.plot(kind='bar', stacked=True, ax=ax)
    plt.xticks(rotation=90)
    plt.ylabel("Average Number of Confirmed Errors")
    plt.legend(title="Confirmed Error Type")
    st.pyplot(fig)

    # Button to download updated dataframe as CSV
    if st.button("Download Updated CSV"):
        to_write = io.BytesIO()
        df.to_csv(to_write, index=False)
        to_write.seek(0)
        st.download_button(label="Download CSV", data=to_write, file_name="updated_error_analysis.csv", mime="text/csv")
else:
    st.write("Please upload a CSV file to proceed.")
