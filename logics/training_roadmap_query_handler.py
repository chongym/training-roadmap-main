import os
import json
import openai
import pandas as pd
from helper_functions import llm


# Load the Excel file
filepath = './data/jobsandskills-skillsfuture-skills-framework-dataset.xlsx'
sheetname = 'Job Role_TCS_CCS'
desired_cols = ['Job Role', 'TSC_CCS Title']

xls = pd.ExcelFile(filepath)
df_job_role_skills = pd.read_excel(xls, sheetname, usecols=desired_cols)

print(df_job_role_skills.head())

def get_skills_for_jobrole(jobrole):
    filtered_df = df_job_role_skills[df_job_role_skills['Job Role'].str.contains(jobrole, case=False)]
    print(filtered_df.head())
    filtered_df
    return filtered_df

def identify_skillgaps_for_jobrole(resume, interest, jobrole):
    df_job_role_skills = get_skills_for_jobrole(jobrole)
        
    delimiter = "####"

    system_message = f"""
    Follow these steps to answer the learner's queries.
    The learner's query will be delimited with a pair {delimiter}.

    Step 1: {delimiter} You will identify the skills needed for the job role, {jobrole}, 
    interest and career aspiration {interest} the learner wants to be trained in.
    Understand the relevant skills for the job role from the following list.
    All available skills shown in the data frame  below:
    {df_job_role_skills}
    
    Step 2:{delimiter} Use the information about the skills needed to 
    identify the skill gap based on the resume {resume} provided by the learner.
    You must only rely on the facts or information in the skill information.
    Your response should be as detail as possible and 
    include information that is useful for learn to better understand the skills he or she lacks.
    
    Provide skill gaps for the learner.
    Ensure your response contains is in table format.
    """

    messages =  [
        {'role':'system',
         'content': system_message},
        {'role':'user',
         'content': f"{delimiter}{jobrole},{interest}{delimiter}"},
    ]

    skillgap_response_str = llm.get_completion_by_messages(messages)
    skillgap_response_str = skillgap_response_str.replace("'", "\"")
   
    return skillgap_response_str


def generate_learning_roadmap(interest, jobrole, skills):
    delimiter = "####"

    system_message = f"""
    You will be provided with learning roadmap. \
    The learner wants to be trained in {jobrole} and the needed skills are {skills}.
    Provide learning roadmap for the job role with expected skillsets.
    Ensure your response contains is in table format.
    """

    messages =  [
        {'role':'system',
         'content': system_message},
        {'role':'user',
         'content': f"{delimiter}{jobrole}{delimiter}"},
    ]

    jobrole_and_skill_response_str = llm.get_completion_by_messages(messages)
    jobrole_and_skill_response_str = jobrole_and_skill_response_str.replace("'", "\"")
    return jobrole_and_skill_response_str
    

def generate_sfc_claim_process():
    delimiter = "####"

    system_message = f"""
    Provide the SkillsFuture Singapore's process for individual to claim for SkillsFuture Credit and the amount available for individuals.
    Use a friendly tone make sure the statements are factually accurate.
    Your response should be comprehensive and informative to help the customers to make their decision.
    """

    messages =  [
        {'role':'system',
         'content': system_message},
        {'role':'user',
         'content': f"{delimiter}{delimiter}"},
    ]

    response_on_sfc = llm.get_completion_by_messages(messages)
    response_on_sfc = response_on_sfc.split(delimiter)[-1]
    return response_on_sfc
   


def generate_response_based_on_course_details(user_message, product_details):
    delimiter = "####"

    system_message = f"""
    Follow these steps to answer the learner's queries.
    The learner's query will be delimited with a pair {delimiter}.

    Step 1:{delimiter} If the user is asking about courses, \
    understand the relevant course(s) from the following list.
    All available courses shown in the json data below:
    {product_details}

    Step 2:{delimiter} Use the information about the course to \
    generate the answer for the customer's query.
    You must only rely on the facts or information in the course information.
    Your response should be as detail as possible and \
    include information that is useful for customer to better understand the course.

    Step 3:{delimiter}: Answer the customer in a friendly tone.
    Make sure the statements are factually accurate.
    Your response should be comprehensive and informative to help the \
    the customers to make their decision.
    Provide learning roadmap for the job role with details such courses, link to the courses, ratings, pricing, and skills to be learnt.
    Use Neural Linguistic Programming to construct your response.

    Use the following format:
    Step 1:{delimiter} <step 1 reasoning>
    Step 2:{delimiter} <step 2 reasoning>
    Step 3:{delimiter} <step 3 response to customer>

    Make sure to include {delimiter} to separate every step.
    """

    messages =  [
        {'role':'system',
         'content': system_message},
        {'role':'user',
         'content': f"{delimiter}{user_message}{delimiter}"},
    ]

    response_to_user = llm.get_completion_by_messages(messages)
    response_to_user = response_to_user.split(delimiter)[-1]
    return response_to_user


def process_user_message(resume, interest, job_role):
    delimiter = "```"

    # Process 1: Identify skill gaps
    jobrole_n_skills = identify_skillgaps_for_jobrole(resume, interest, job_role)
    print("jobrole_n_skills : ", jobrole_n_skills)

    # Process 2: Suggest learning roadmap
    learning_roadmap = generate_learning_roadmap(interest, job_role, jobrole_n_skills)

    return learning_roadmap, jobrole_n_skills