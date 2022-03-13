from email import header
from email.policy import default
from re import template
from matplotlib.pyplot import title
from sqlalchemy import Column
import streamlit as st
import streamlit.components.v1 as  components
import pandas as pd
import plotly
import plotly.express as px
import plotly.io as pio

st.set_page_config(page_title='Data 5000 project', layout='wide')
import time
with st.spinner('Wait for it...'):
    time.sleep(3)
st.success('Page loading complete')
st.balloons()

st.title('Covid impact on labour market')

df=pd.DataFrame(pd.read_csv('CleanedV2.1.csv'))


## Data filter options
st.markdown("Please select the filters below:")
characteristics = df['Labour force characteristics'].unique().tolist()
age_group = df['Age group'].unique().tolist()
gender = df['Sex'].unique().tolist()
area = df['Geography'].unique().tolist()

columns = st.columns((2,2,2,2))

with columns[0]:
    characteristics_selection = [st.radio("Characteristics",
                                        characteristics)]
with columns[1]:
    age_group_selection = [st.radio('Age Groups',
                                        age_group)]
with columns[2]:
    gender_selection = [st.radio('Gender',
                                    gender)]                              
with columns[3]:
    area_selection = [st.radio('Geography',
                                    area)]

gender_males = ['Males']
gender_females = ['Females']
age_15_over = ['15 years and over']
age_15_24 = ['15 to 24 years']
age_25_54 = ['25 to 54 years']
age_55_over = ['55 years and over']

## Dataframe filter/mask

mask1 = (df['Geography'].isin(area_selection)) & (df['Labour force characteristics'].isin(characteristics_selection)) & (df['Sex'].isin(gender_selection)) & (df['Age group'].isin(age_group_selection))
mask2 = (df['Geography'].isin(area_selection)) & (df['Labour force characteristics'].isin(characteristics_selection)) & (df['Age group'].isin(age_group_selection)) & (df['Sex'].isin(gender_males))
mask3 = (df['Geography'].isin(area_selection)) & (df['Labour force characteristics'].isin(characteristics_selection)) & (df['Age group'].isin(age_group_selection)) & (df['Sex'].isin(gender_females))
mask4 = (df['Geography'].isin(area_selection)) & (df['Labour force characteristics'].isin(characteristics_selection)) & (df['Sex'].isin(gender_selection)) & (df['Age group'].isin(age_15_over))
mask5 = (df['Geography'].isin(area_selection)) & (df['Labour force characteristics'].isin(characteristics_selection)) & (df['Sex'].isin(gender_selection)) & (df['Age group'].isin(age_15_24))
mask6 = (df['Geography'].isin(area_selection)) & (df['Labour force characteristics'].isin(characteristics_selection)) & (df['Sex'].isin(gender_selection)) & (df['Age group'].isin(age_25_54))
mask7 = (df['Geography'].isin(area_selection)) & (df['Labour force characteristics'].isin(characteristics_selection)) & (df['Sex'].isin(gender_selection)) & (df['Age group'].isin(age_55_over))
mask8 = (df['Geography'].isin(area_selection)) & (df['Labour force characteristics'].isin(characteristics_selection))


## comparison by gender
st.markdown("___")
container = st.container()

with container:
    st.subheader("Comparison by gender")
    st.markdown("Gender filter at top is NA for this section")
    columns=st.columns((2,2))

    with columns[0]:
        fig1 = px.line(df[mask2], x = 'Date', y = 'Value', color_discrete_sequence=["red"], title="Characteristics for Males", template='simple_white')
        fig1.update_layout(title_x=0.5, title_y=0.85)
        fig1.update_layout({'plot_bgcolor':'rgba(0, 0, 0, 0)'})
        st.plotly_chart(fig1)

    with columns[1]:
        fig2 = px.line(df[mask3], x='Date', y='Value', color_discrete_sequence=["blue"], title="Characteristics for Females", template='plotly_white')
        fig2.update_layout(title_x=0.5, title_y=0.85)
        fig2.update_layout({'plot_bgcolor':'rgba(0, 0, 0, 0)'})
        st.plotly_chart(fig2)


##  comparison by age
with container:
    st.subheader("Comparison by age")
    st.markdown("Age filter at top is NA for this section")
    columns = st.columns((2,2))

    with columns[0]:
        fig3 = px.line(df[mask4], x='Date', y='Value', color_discrete_sequence=["black"], title="Age 15 and over", template='plotly')
        fig3.update_layout(title_x=0.5, title_y=0.85)
        fig3.update_layout({'plot_bgcolor':'rgba(0, 0, 0, 0)'})
        st.plotly_chart(fig3)

        fig5 = px.line(df[mask5], x='Date', y='Value', color_discrete_sequence=["purple"], title="Age 15-24", template='presentation')
        fig5.update_layout(title_x=0.5, title_y=0.85)
        fig5.update_layout({'plot_bgcolor':'rgba(0, 0, 0, 0)'})
        st.plotly_chart(fig5)
        
    
    with columns[1]:
        fig4 = px.line(df[mask7], x='Date', y='Value', color_discrete_sequence=["indigo"], title="Age 55 and over", template='ggplot2')
        fig4.update_layout(title_x=0.5, title_y=0.85)
        fig4.update_layout({'plot_bgcolor':'rgba(0, 0, 0, 0)'})
        st.plotly_chart(fig4)

        fig6 = px.line(df[mask6], x='Date', y='Value', color_discrete_sequence=["green"], title="Age 25-54", template='gridon')
        fig6.update_layout(title_x=0.5, title_y=0.85)
        fig6.update_layout({'plot_bgcolor':'rgba(0, 0, 0, 0)'})
        st.plotly_chart(fig6)

## google job search trend
with container:
    st.subheader("Google trends on Job search")
    htmlfile=open("Google trend.html", 'r', encoding ='utf-8')
    source_code = htmlfile.read()
    print(source_code)
    components.html(source_code, height = 1000, width = 1000)

##  dataset
with container:
    st.subheader("Filtered Dataset")
    st.dataframe(df[mask1])
    

