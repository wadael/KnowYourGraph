import streamlit as st
import plotly_express as px
import pandas as pd
from kygcommon.kygcommon import *

doConfigAndSidebar("anims/99430-statistics.json")

st.write("# Distribution by label")
labelz = st.session_state.labels.keys()
valuez = st.session_state.labels.values()
df = pd.DataFrame(dict(labs=labelz, nbr=valuez))

col1, col2 = st.columns([3,1])
with col1:
    st.write("## Distribution by label, showing nodes volumes")
    treemap = px.treemap(df, path=[px.Constant("all"), "labs"], values=df["nbr"] )
    treemap.update_traces(root_color="lightgrey")
    treemap.update_layout(margin=dict(t=50, l=25, r=25, b=25))
    st.plotly_chart( treemap )

    st.write("## Same but rounder :)")
    sunburst = px.sunburst(df, path=[px.Constant("all"), "labs"], values=df["nbr"])
    st.plotly_chart( sunburst )

with col2:
    st.write("## The data")
    df

st.write("# Distribution, considering a pivotal value")
st.write("""
Set the pivot value. 
On the left the labels with less nodes than the chosen value.\n
On the right, the labels with more nodes than the selected value.
""")
limit = st.slider('Where is comparison limit', min_value=0, max_value=max(df["nbr"]), value = 1000, step=10)
dfUnderLimit = df[df["nbr"] < limit]
dfAboveLimit = df[df["nbr"] >= limit]

under, above = st.columns(2)
with under:
    st.write("## under " + str(limit) + " nodes")
    treemapU = px.treemap(dfUnderLimit, path=[px.Constant("all"), "labs"], values=dfUnderLimit["nbr"])
    treemapU.update_traces(root_color="lightgrey")
    treemapU.update_layout(margin=dict(t=50, l=25, r=25, b=25))
    st.plotly_chart(treemapU)
with above:
    st.write("## above " + str(limit) + " nodes")
    treemapA = px.treemap(dfAboveLimit, path=[px.Constant("all"),  "labs"], values=dfAboveLimit["nbr"])
    treemapA.update_traces(root_color="lightgrey")
    treemapA.update_layout(margin=dict(t=50, l=25, r=25, b=25))
    st.plotly_chart(treemapA)

