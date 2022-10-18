import streamlit as st
from streamlit_lottie import st_lottie
import json
from neo4j import GraphDatabase
import pandas as pd

def doConfigAndSidebar(anim):
    with st.sidebar:
        st.sidebar.header("🎉 Welcome")
        st.sidebar.title("Learning Neo4j 3rd Edition")
        if len(anim)==0:
            anim = "anims/90021-graph-stats.json"
        with open(anim, "r") as f:
            data = json.load(f)
        st_lottie(data)

    if 'driver' not in st.session_state:
        driver = GraphDatabase.driver("neo4j://localhost:7687", auth=("neo4j", "password"))
        st.session_state.driver = driver

def getDataFrameFromReadQuery(query):
    driver = st.session_state.driver
    df = pd.DataFrame()
    with driver.session() as session:
        result = session.run(query)
        for record in result:
            df = df.append(record.data(), ignore_index=True)
    session.close()
    return df