import streamlit as st
from streamlit_lottie import st_lottie
import json
from neo4j import GraphDatabase
import pandas as pd

def doConfigAndSidebar(anim):
    with st.sidebar:
        st.sidebar.title("Learning Neo4j 3rd Edition")
        if len(anim)==0:
            anim = "anims/90021-graph-stats.json"
        with open(anim, "r") as f:
            data = json.load(f)
        st_lottie(data)

    if 'driver' not in st.session_state:
        try:
            driver = GraphDatabase.driver("neo4j://localhost:7687", auth=("neo4j", "password"))
            st.session_state.driver = driver
        except:
            st.error("Is your Neo4j server running ??")
    if 'driver' not in st.session_state:
        st.error("Is your Neo4j server running ???")
        st.stop()
def getDataFrameFromReadQuery(query):
    driver = st.session_state.driver
    if 'driver' not in st.session_state:
        st.error("🚨 Is your Neo4j server running ??")
    else:
        df = pd.DataFrame()
        with driver.session() as session:
            result = session.execute_read(query)
            for record in result:
                df = df.append(record.data(), ignore_index=True)
        session.close()
        return df

def get_movies(tx, name):
    result = tx.run("""
        MATCH (p:Person {name:$name})-[:ACTED_IN]->(m:Movie )
        RETURN m
        ORDER BY m.released
    """, name=name)
    return [record["m"] for record in result]
