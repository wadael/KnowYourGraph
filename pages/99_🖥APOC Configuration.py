import streamlit as st
import os
from neo4j import GraphDatabase
import pandas as pd
from kygcommon.kygcommon import *

doConfigAndSidebar("anims/24117-hub-computer.json")

st.title("APOC Environment variables (and more)")
st.write("### Those are for the machine Neo4j is running on")

st.write("Click the columns for sorting")
driver = GraphDatabase.driver("neo4j://localhost:7687", auth=("neo4j", "password"))
df = pd.DataFrame(columns=["Key","Value"])
with driver.session() as session:
    result = session.run("CALL apoc.config.list()")

    for record in result:
        df = df.append({"Key": record["key"], "Value": record["value"]}, ignore_index=True)

session.close()
df
