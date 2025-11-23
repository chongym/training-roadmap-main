# Set up and run this Streamlit App
import streamlit as st
import pandas as pd
from logics.training_roadmap_query_handler import process_user_message
from io import StringIO
import pdfplumber


# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="Learning Roadmap App"
)

from helper_functions.utility import check_password

# Do not continue if check_password is not True.  
if not check_password():  
    st.stop()

# endregion <--------- Streamlit App Configuration --------->

st.title("Learning Roadmap")

with st.form(key="form"):
    st.subheader("Identify skill gaps and create learning roadmap for your dream job.")

    interest = st.text_area("Enter your interest and career aspiration:", height=50)
    job_role = st.text_input("Enter the job role you would like to be trained in:","Product Manager")
    uploaded_file = st.file_uploader("Upload your resume:", type=["txt", "doc", "pdf"], key='file_uploader')
    submit_button = st.form_submit_button("Submit")
   
if submit_button:
    st.toast(f"User Input Submitted - {interest}")
    st.session_state["interest"] = interest
    st.session_state["job_role"] = job_role   
 
    if uploaded_file is not None:
        if uploaded_file.type == "text/plain":
            resume = uploaded_file.read().decode("utf-8")
            st.write("File content:")
            st.code(resume)
            st.write(resume)
        elif uploaded_file.type == "application/pdf":
            with pdfplumber.open(uploaded_file) as pdf:
                resume = ""
                for page in pdf.pages:
                    resume += page.extract_text() + "\n"
        else:
             st.write("File type not supported")

    response, skill_details = process_user_message(resume, interest, job_role)
    st.write(f"**Skill Needed for {job_role} based on SFw from SSG:**")
    st.write(skill_details)    
    st.divider()
    st.write(response)
