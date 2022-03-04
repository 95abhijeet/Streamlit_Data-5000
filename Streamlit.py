import streamlit as st
import streamlit.components.v1 as components

header = st.container()


with header:
    st.title('Covid impact on labour market')

    htmlfile=open("Google trend.html", 'r', encoding ='utf-8')
    source_code = htmlfile.read()
    print(source_code)
    components.html(source_code, height = 800, width = 1000)
