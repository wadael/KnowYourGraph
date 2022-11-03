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
st.title("Your KPIs")
st.write("## You will create them along reading the book.")

driver = st.session_state.driver

def get_movies_count(tx, name):
    result = tx.run("""
        MATCH (p:Person {name:$name})-[:ACTED_IN]->(m:Movie )
        RETURN count(m) as number
    """, name=name)
    return [record["number"] for record in result][0]




with driver.session() as session:
    moviesKeanu = session.execute_read(get_movies, name="Keanu Reeves")
    moviesMegRyan = session.execute_read(get_movies, name="Meg Ryan")

    movieCountAl = session.execute_read(get_movies_count, name="Al Pacino")
    movieCountClint = session.execute_read(get_movies_count, name="Clint Eastwood")

session.close()

col1, col2 = st.columns(2)
with col1:
    col1.header("Keanu")
    for record in moviesKeanu:
        st.write(record["title"] + " " + str(record["released"]))

with col2:
    col2.header("Meg Ryan")
    for record in moviesMegRyan:
        st.write(record["title"] + " " + str(record["released"]))

st.write("Al Pacino appeared in " + str(movieCountAl) + " movie(s)")
st.write("Clint Eastwood appeared in " + str(movieCountClint) + " movie(s)")
