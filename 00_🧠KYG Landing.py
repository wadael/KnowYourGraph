import streamlit as st
from kygcommon.kygcommon import *

st.set_page_config(
    page_title="Know Your Graph w/ Learning Neo4j 3rd Edition ",
    page_icon="🧠",
    layout='wide',
    initial_sidebar_state="expanded"
)

doConfigAndSidebar("")

st.title("Learning Neo4j 3rd Edition - Know your graph")
st.write("## A book by Jérôme Bâton and Rik Van Bruggen")
st.write("🎉 Welcome")

st.write("""
This application needs to connect to a Neo4j server.

The default is using localhost as server, with neo4j user and password as password 
""")
st.write("""
Have you installed the APOC plugin on your server ? You should, it is necessary.

If you read:    ServiceUnavailable: Unable to retrieve routing information     then your Neo4j is not accessible :/

Configure it in kygcommon.py
""")
