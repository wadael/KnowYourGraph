import streamlit as st
from kygcommon.kygcommon import *

st.set_page_config( layout='wide', initial_sidebar_state="expanded" )

st.title("Learning Neo4j 3rd Edition - Know your graph")

doConfigAndSidebar("")

driver = st.session_state.driver
with driver.session() as session:
    result = session.run("CALL apoc.meta.stats()")
    for record in result:
        labelCount = (record["labelCount"])
        relTypeCount = (record["relTypeCount"])
        propertyKeyCount = (record["propertyKeyCount"])
        nodeCount = (record["nodeCount"])
        relCount = (record["relCount"])
        st.session_state.labels = (record["labels"])
        relTypes = (record["relTypes"])
        relTypesCount = (record["relTypesCount"])
        st.session_state.stats = (record["stats"])
session.close()

st.write("# Your graph in a glance")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("How many nodes ?", nodeCount)
with col2:
    st.metric("How many labels ?", labelCount)
with col3:
    st.metric("How many relations Types?", relTypeCount)
with col4:
    st.metric("How many relations (total) ?", relCount)

