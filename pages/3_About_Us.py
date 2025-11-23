import streamlit as st

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="Capstone Project - Learning Roadmap"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("About this Learning Roadmap App")

with st.expander("How to use this application", expanded=True):
    st.write("1. Enter your interest, career inspiration  in the text area.")
    st.write("2. Enter job role you would like to be trained in the text box.")
    st.write("3. Upload your resume for skill gap analysis.")
    st.write("2. Click the 'Submit' button.")
    st.write("3. The application will perform skill gaps analysis for the job role and suggest a learning roadmap and the learning resources to take up the job.")
