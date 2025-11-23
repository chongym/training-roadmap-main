import streamlit as st

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="Capstone project - Learning Roadmap"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("About this App")

st.write("**Overview**: The Streamlit web application will base on the user interest and career aspiration to help identify skill gaps and recommend learning roadmap for the job role.\n\n")
st.write("**Goals**: Make planning for a career path easy by providing a learning roadmap to help individuals to achieve their learning goals.\n")

st.write("**Specification:**")
st.write("1. Provide the skills required of a job role based on Skill Framework (SFw) from SkillsFuture.")
st.write("2. Based on the work experience and current skills to identify skill gaps.")     
st.write("3. Recommend learning roadmap with courses or apprenticeships opportunities to help gain the skills.\n")     

st.write("**Workflow:**")
st.write("Request for user profile -> Extract neeeded skills from SFw -> Identify skill gaps ->")
st.write("Generate learning recommendation")

st.divider()

with st.expander("How to use this App"):
    st.write("1. Enter your interest, career inspiration  in the text area.")
    st.write("2. Enter job role you would like to be trained in the text box.")
    st.write("3. Upload your resume for skill gap analysis.")
    st.write("2. Click the 'Submit' button.")
    st.write("3. The app will analyse skill gaps for the job role and suggest a learning roadmap and the learning resources.")
