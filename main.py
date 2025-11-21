# Set up and run this Streamlit App
import streamlit as st
import pandas as pd
# from helper_functions import llm
#from logics.customer_query_handler import process_user_message
from logics.training_roadmap_query_handler import process_user_message


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

st.title("Learning Roadmap App")

form = st.form(key="form")
form.subheader("Prompt")

user_prompt = form.text_area("Enter your job role you want to get trained in e.g. product manager, business analyst, etc.", height=50)

if form.form_submit_button("Submit"):
    
    st.toast(f"User Input Submitted - {user_prompt}")

    st.divider()

    response, df_skill_details = process_user_message(user_prompt)
    st.write(response)

    st.divider()

    print(df_skill_details)
    #df = pd.DataFrame(skill_details)
    df_skill_details
