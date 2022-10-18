import streamlit as st
from streamlit_lottie import st_lottie
from neo4j import GraphDatabase
import json
from kygcommon.kygcommon import *

# 📊 📊
doConfigAndSidebar("")
st.title("Your KPIs")
st.write("## You will create them along reading the book.")