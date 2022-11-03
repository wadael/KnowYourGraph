import streamlit as st
from streamlit_lottie import st_lottie
from neo4j import GraphDatabase
import json
from kygcommon.kygcommon import *
import plotly_express as px
import pandas as pd

st.set_page_config( layout='wide', initial_sidebar_state="expanded")
# 📊 📊
doConfigAndSidebar("")
st.title("Emil")
st.header("Statistics about Emil's carreer")

driver = st.session_state.driver

def emil_filmography_kpis(tx):
    result = tx.run("""
            MATCH (k:KPI{id:'EmilFilmCount'})
            RETURN toString(datetime({ epochSeconds:k.when/1000, nanosecond: 23})) AS w, k.value as v
            ORDER BY k.when ASC
        """)
    return [[record["w"], record["v"]] for record in result]

with driver.session() as session:
    moviesEmil = session.execute_read(get_movies, name="Emil Eifrem")
    for record in moviesEmil:
        st.write(record["title"] + " " + str(record["released"]))

    kpis = session.execute_read(emil_filmography_kpis)
    session.close()

    df = pd.DataFrame(kpis)
    lineplot = px.line(kpis, x=0, y=1, labels={'0': "Time", '1': "Film count"})

col1, col2 = st.columns([2, 1])
with col1:
    lineplot
with col2:
    df

