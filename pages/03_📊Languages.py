import streamlit as st
from streamlit_lottie import st_lottie
from neo4j import GraphDatabase
import json
import pandas as pd
import plotly_express as px
from kygcommon.kygcommon import *


# 📊 📊


doConfigAndSidebar("")
st.title("📊 Languages")
df = getDataFrameFromReadQuery("""
MATCH (s:Smurf)-[:WRITTEN_IN]->(l:Language)
RETURN l.code as code, coalesce(l.K_LangName, l.TWB_LangName,l.Google_LangName, l.FB_LangName) as lang, count(s) as smurfs 
ORDER BY smurfs DESC""")

st.write("## Distribution by language, showing nodes volumes")
treemap = px.treemap(df, path=[px.Constant("all"), "code"], values=df["smurfs"] )
treemap.update_traces(root_color="lightgrey")
treemap.update_layout(margin=dict(t=50, l=25, r=25, b=25))
st.plotly_chart( treemap )

with st.expander("The data"):
    df
