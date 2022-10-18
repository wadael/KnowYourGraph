import streamlit as st
from streamlit_lottie import st_lottie
from neo4j import GraphDatabase
import json
from kygcommon.kygcommon import *

st.title("Learning Neo4j 3rd Edition - Know your graph")
st.write("")

doConfigAndSidebar("")
driver = st.session_state.driver

with driver.session() as session:
    result = session.run("CALL apoc.meta.stats()")
    for record in result:
        st.session_state.labelCount = (record["labelCount"])
        st.session_state.relTypeCount = (record["relTypeCount"])
        st.session_state.propertyKeyCount = (record["propertyKeyCount"])
        st.session_state.nodeCount = (record["nodeCount"])
        st.session_state.relCount = (record["relCount"])
        st.session_state.labels = (record["labels"])
        st.session_state.relTypes = (record["relTypes"])
        st.session_state.relTypesCount = (record["relTypesCount"])
        st.session_state.stats = (record["stats"])
session.close()

st.write("# Your graph in a glance")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("How many nodes ?", st.session_state.nodeCount)
with col2:
    st.metric("How many labels ?", st.session_state.labelCount)
with col3:
    st.metric("How many relations Types?", st.session_state.relTypeCount)
with col4:
    st.metric("How many relations ?", st.session_state.relCount)

