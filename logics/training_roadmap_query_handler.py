import os
import json
import openai
import pandas as pd
from helper_functions import llm


category_n_course_name = {'Programming and Development': ['Web Development Bootcamp',
                                                          'Introduction to Cloud Computing',
                                                          'Advanced Web Development',
                                                          'Cloud Architecture Design'],
                          'Data Science & AI': ['Data Science with Python',
                                                'AI and Machine Learning for Beginners',
                                                'Machine Learning with R',
                                                'Deep Learning with TensorFlow'],
                          'Marketing': ['Digital Marketing Masterclass',
                                        'Social Media Marketing Strategy'],
                          'Cybersecurity': ['Cybersecurity Fundamentals',
                                            'Ethical Hacking for Beginners'],
                          'Business and Management': ['Project Management Professional (PMP)Â® Certification Prep',
                                                      'Agile Project Management'],
                          'Writing and Literature': ['Creative Writing Workshop',
                                                     'Advanced Creative Writing'],
                          'Design': ['Graphic Design Essentials', 'UI/UX Design Fundamentals']}

# Load the JSON file
filepath = './data/jobsandskills-skillsfuture-skills-framework-dataset.xlsx'
sheetname = 'Job Role_TCS_CCS'
desired_cols = ['Job Role', 'TSC_CCS Title']

xls = pd.ExcelFile(filepath)
df_job_role_skills = pd.read_excel(xls, sheetname, usecols=desired_cols)

print(df_job_role_skills.head())

def identify_jobrole_and_skills(user_message):
    filtered_df = df_job_role_skills[df_job_role_skills['Job Role'].str.contains(user_message, case=False)]
    print(filtered_df.head())
    filtered_df
    return filtered_df


def generate_learning_roadmap(jobrole, skills):
    delimiter = "####"

    system_message = f"""
    You will be provided with learning roadmap. \
    The learner's job role is {jobrole} and the needed skills are {skills} {delimiter}.

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
    #jobrole_and_skill_response = json.loads(jobrole_and_skill_response_str)
    return jobrole_and_skill_response_str
    

#def get_skill_details(list_of_relevant_jobrole_n_skill: list[dict]):
def get_skill_details(jobrole):
    skills_list = []
    #for x in list_of_relevant_jobrole_n_skill:
    #    skills_list.append(x.get('course_name')) # x["course_name"]

    #list_of_course_details = []
    #for skill_name in skills_list:
    #    list_of_course_details.append(dict_of_courses.get(skill_name))
    return skills_list 


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
    Provide learning roadmap for the job role with details such rating, pricing, and skills to be learnt.
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


def process_user_message(user_input):
    delimiter = "```"

    # Process 1: If Courses are found, look them up
    df_jobrole_n_skills = identify_jobrole_and_skills(user_input)
    print("jobrole_n_skills : ", df_jobrole_n_skills)

    # Process 2: Get the Course Details
    learning_roadmap = generate_learning_roadmap(user_input, df_jobrole_n_skills['TSC_CCS Title'])

    # Process 3: Generate Response based on Course Details
    #reply = generate_response_based_on_course_details(user_input, skill_details)


    return learning_roadmap, df_jobrole_n_skills