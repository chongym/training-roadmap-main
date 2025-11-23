import streamlit as st

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="Capstone project - Learning Roadmap"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("Methodology")

st.write("**Overview**: The Streamlit web application will base on the user interest and career aspiration to help identify skill gaps and recommend learning roadmap for the job role provided by the user.\n\n")
st.write("**Goals**: Make planning for career advancement easy by providing a learning roadmap to help individuals to achieve their learning goal.\n")

st.write("**How does it work:**")
st.write("Multi-Action Prompts: Step-by-Step Instructions in a Single Prompt")
st.write("1. Extract the skills required of a job role based on Skill Framework (SFw) from SkillsFuture.")
st.write("2. Based on the work experience and current skills acquired provided in resume to identify skill gaps.")     
st.write("3. Recommend learning roadmap with learning activities needed to acquire the new skills.\n")     

st.divider()
# 1. Define the custom CSS style
custom_css = """
<style>
.fixed-width-container {
    width: 400px; /* Set your desired fixed width */
    border: 2px solid #4CAF50; /* Add a border (color and thickness can be customized) */
    padding: 10px; /* Add some padding for better text spacing */
    border-radius: 5px; /* Optional: rounded corners */
}
</style>
"""
# 2. Inject the CSS into the Streamlit app
st.markdown(custom_css, unsafe_allow_html=True)

st.write("**Workflow:**\n")

with st.container(border=True, width=250):
    #st.markdown('<div class="fixed-width-container">', unsafe_allow_html=True)
    st.write("**Request for user profile**")
    st.write("(Data: interest, resume, job role)")
    #st.markdown('</div>', unsafe_allow_html=True)

with st.container(border=True, width=250):
    st.write("**Extract neeeded skills from SFw**")
    st.write("(Data: Skill framework from SSG)")

with st.container(border=True, width=250):
    st.write("**Identify skill gaps**")
    st.write("(Data: Skills not in profile)")

with st.container(border=True, width=250):
    st.write("**Generate learning recommendation**")
    st.write("(Data: Learning activities and outcomes)")

st.divider()

