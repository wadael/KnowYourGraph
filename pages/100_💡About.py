import streamlit as st
import plotly_express as px
from scipy.integrate._ode import dop853

from kygcommon.kygcommon import *

doConfigAndSidebar("anims/8586-rocket-in-space.json")

st.write("# 💡 About")
st.write("## ❓ What is that ?")
st.write("""
Made for the third edition of Learning Neo4j , edited by Pakt Publishing http://packtpub.com, this web application uses 
Streamlit and Python to give you some insights about the content of your graph.\n
THe book will teach you how to add your own indicators.
Source code is available on Github : https://github.com/wadael/KnowYourGraph
""")

col0, col1, col2 = st.columns([1,4,4])
with col0:
    st.image("https://yt3.ggpht.com/ytc/AMLnZu8oL48Yh2b0qLdKpygdG9oUC6NLjKPSNk9j57Lwcg=s88-c-k-c0x00ffffff-no-rj")
with col1:
    st.write("## 🧍 Author")

    st.write('''
    Jérôme BATON \n
    \n
    https://www.linkedin.com/in/jeromebaton/ \n
    https://github.com/wadael
    ''')
    st.write("Open for business")

with col2:
    st.write("## 🏢 Editor")
    st.write("Packt Publishing https://www.packtpub.com/")

st.write("## 🌍 Kamusi")
st.write(" https://kamusi.org/")
st.write("Kamusi means dictionary in Swahili, an African language. We want to preserve the languages under represented on the web")

with st.expander("More about Kamusi", False):
    st.write("""
Our motto is our goal, "Every Word in Every Language". Completely fulfilling this mission is impossible, but it sets the target toward which we aim.\nWe aspire to merge all that is known and all that is knowable about language, in one data system that is free to everyone.\n
\nMore than 7000 different languages are spoken around the world.\n\n
Some languages have hundreds of millions of speakers and many dialects.\n
Hundreds of endangered languages, meanwhile, might disappear in a generation. Fully documenting every expression from every language variation would require thousands of researchers and decades of work.
\n\nAt Kamusi, we concentrate on ways to collect as much data for as many languages as possible, arrange that data precisely, and put the information at the service of students, the public, and the technology we use to communicate. We have games and other tools for people worldwide to systematically share what they know about their language, and we have a global partner network for experts to contribute their knowledge. We also integrate existing datasets whenever possible, though most languages do not have any meaningful available digital resources.
The Kamusi architecture supports, in principle, a complete matrix of human expression across time and space. 
\n\nThis is a mission to Mars, an ambition to be attempted by pulling together people and resources in a concerted international collaboration. It is a hard, hard road ahead. We seek every word in every language, but we cannot even really say what is a word or what is a language, much less how we can pay for it all. However, we have the core systems in place, or ready to release when we can afford to manage the data influx, and additional components that are fully specified and just need funds to implement.
Please join us in turning our Quixotic quest into a reality that creates and unites as much information as possible for the world's languages! 
\nWe greatly appreciate your financial contributions, and eagerly anticipate your participation as we roll out our language games to reach for the stars, one word at a time, toward every word in every language.     
    """);


st.write("### Streamlit links")
st.write("Learn more about Streamlit at http://streamlit.io")
cphoto,clink = st.columns([1,9])
with cphoto:
        st.image("https://yt3.ggpht.com/u9fmBHRs3P8pMdyvMcgJ8K4ewEn4zh65oD0-2BWzeIneAlokFDsi7AtwCM1fBU7i7ldXwRat=s88-c-k-c0x00ffffff-no-rj")
with clink:
        st.write("* Youtube : Fanilo Andrianasolo : https://www.youtube.com/c/FaniloAndrianasolo")
        st.write("* Fanilo is a core developer for several Streamlit extensions and a Community Ambassador for Streamlit itself")


st.write("### Credits")
st.write("The Lottie animation, found on lottiefiles.com are "
         "\n* from Suhayra Sarwar   https://lottiefiles.com/90021-graph-stats"
         "\n* from Nirdhum Narayan  https://lottiefiles.com/99430-statistics"
         "\n* from Nirdhum Narayan  https://lottiefiles.com/99500-company-statistic-graph"
         "\n* from Ilya Pavlov   https://lottiefiles.com/8586-rocket-in-space"
         )
