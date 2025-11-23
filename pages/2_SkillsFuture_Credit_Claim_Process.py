import streamlit as st
import pandas as pd
import json
from logics.training_roadmap_query_handler import generate_sfc_claim_process


sfc_claim_process = generate_sfc_claim_process()
st.write(sfc_claim_process)
st.divider()