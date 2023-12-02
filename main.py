import streamlit as st
import pandas as pd
import base64
import io

def convert_excel_to_json(uploaded_file):
    # Read the Excel file
    df = pd.read_excel(uploaded_file)
    # Convert the dataframe to JSON
    return df.to_json(orient='records')

def get_table_download_link(json_str):
    # Generate a download link for the JSON file
    b64 = base64.b64encode(json_str.encode()).decode()
    href = f'<a href="data:file/json;base64,{b64}" download="converted_file.json">Download JSON file</a>'
    return href

def main():
    st.title("Excel to JSON Converter")

    # File uploader widget
    uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx"])

    if uploaded_file is not None:
        # Convert the file to JSON
        json_str = convert_excel_to_json(uploaded_file)
        st.write("JSON output:")
        st.text_area("Output", json_str, height=250)
        st.markdown(get_table_download_link(json_str), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
