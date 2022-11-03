import streamlit as st
import pandas as pd
from kygcommon.kygcommon import *

doConfigAndSidebar("anims/99430-statistics.json")

st.title("Relations")
"""
See the different relations available in the graph.

Data comes from the procedure call in 'Graph in a glance' page
There is redundancy.

It is shown as a sorted Pandas dataframe
 
"""

stats = st.session_state.stats['relTypes'] # its a dict
toshow=dict(sorted(stats.items()))
df=pd.DataFrame.from_dict(toshow, orient='index')   # , columns=['Relation','Count']
df
