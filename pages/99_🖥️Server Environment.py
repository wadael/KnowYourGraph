import streamlit as st
import os
import pandas as pd
from kygcommon.kygcommon import *

doConfigAndSidebar("anims/24117-hub-computer.json")
st.title("Environment variables")

# printing environment variables
st.write("### Those are for the machine Streamlit is running on")
st.write("Click the columns for sorting")

df = pd.DataFrame(columns=["Key","Value"])

for k, v in os.environ.items():
    df = df.append({"Key": k, "Value": v}, ignore_index=True)

df