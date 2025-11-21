import streamlit as st

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="Capstone project - Course Roadmap"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("About this App")

st.write("This is a Streamlit App that provides course roadmap.")

with st.expander("How to use this App"):
    st.write("1. Enter the job role you would like to be trained in in the text area.")
    st.write("2. Click the 'Submit' button.")
    st.write("3. The app will generate a learning roadmap with the skill sets needed and the learning resources based on your prompt.")
