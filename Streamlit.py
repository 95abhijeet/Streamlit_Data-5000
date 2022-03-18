from email import header
from email.policy import default
from re import template
from matplotlib.axis import YTick
from matplotlib.pyplot import title, xticks
from sqlalchemy import Column
import streamlit as st
import streamlit.components.v1 as  components
import pandas as pd
import plotly
import plotly.express as px
import plotly.io as pio

st.set_page_config(page_title='Data 5000 project', layout='wide')
                                                   # menu_items={
                                                               # 'Get Help': '<email-id>',
                                                               # 'Report a bug': "<email-id>",
                                                              #  'About': "# This is a header. This is an *extremely* cool app!"})
import time
with st.spinner('Wait for it...'):
    time.sleep(2)
st.success('Page loading complete')
st.balloons()

st.title('Covid impact on labour market')

container = st.container()



###         COMPARISON BY GENDER

with container:
    
    
    st.write("Below are different categories for data analysis  \n"
            "Option 1 : Comparison by Gender  \n"
            "Option 2 : Comaprison by Age  \n"
            "Option 3 : Comparison by Industries  \n"
            "Option 4 : Comparison by Education  \n"
            "Option 5 : Additional info using Google trends")
    st.markdown("___")

    with st.expander("Option 1 : Comparison by Gender"):
    
        df=pd.DataFrame(pd.read_csv('Cleaned_Labour force_V1.1.csv'))
        # datset for labour force


        st.markdown(" ")
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

        gender_both = ['Males','Females']
        all_age = ['15 years and over','15 to 24 years','25 to 54 years','55 years and over']
        age_15_over = ['15 years and over']
        age_15_24 = ['15 to 24 years']
        age_25_54 = ['25 to 54 years']
        age_55_over = ['55 years and over']

        ## Dataframe filter/mask

        mask1 = (df['Geography'].isin(area_selection)) & (df['Labour force characteristics'].isin(characteristics_selection)) & (df['Sex'].isin(gender_selection)) & (df['Age group'].isin(age_group_selection))
        mask2 = (df['Geography'].isin(area_selection)) & (df['Labour force characteristics'].isin(characteristics_selection)) & (df['Age group'].isin(age_group_selection)) & (df['Sex'].isin(gender_both))
        mask3 = (df['Geography'].isin(area_selection)) & (df['Labour force characteristics'].isin(characteristics_selection)) & (df['Age group'].isin(all_age)) & (df['Sex'].isin(gender_selection))
        mask4 = (df['Geography'].isin(area_selection)) & (df['Labour force characteristics'].isin(characteristics_selection)) & (df['Sex'].isin(gender_selection)) & (df['Age group'].isin(age_15_over))
        mask5 = (df['Geography'].isin(area_selection)) & (df['Labour force characteristics'].isin(characteristics_selection)) & (df['Sex'].isin(gender_selection)) & (df['Age group'].isin(age_15_24))
        mask6 = (df['Geography'].isin(area_selection)) & (df['Labour force characteristics'].isin(characteristics_selection)) & (df['Sex'].isin(gender_selection)) & (df['Age group'].isin(age_25_54))
        mask7 = (df['Geography'].isin(area_selection)) & (df['Labour force characteristics'].isin(characteristics_selection)) & (df['Sex'].isin(gender_selection)) & (df['Age group'].isin(age_55_over))
        mask8 = (df['Geography'].isin(area_selection)) & (df['Labour force characteristics'].isin(characteristics_selection))


        columns = st.columns((2,1))

        with columns[0]:

            st.subheader("Comparison by gender")
            st.markdown("Gender filter at top is NA for this section")
            

            fig1 = px.line(df[mask2], x = 'Date', y = 'Value', facet_col='Sex', template='gridon')
            fig1.update_layout( width=1000, height = 500)
            #fig1.update_layout({'plot_bgcolor':'rgba(0, 0, 0, 0)'})
            st.plotly_chart(fig1)

        with columns[1]:
            st.markdown("*We can write some description here*")
            st.write("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa  \n"
                        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa  \n"
                            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

###         COMPARISION BY AGE
with container:

    with st.expander("Option 2 : Comaprison by Age"):

        # st.markdown("___")
        st.subheader("Comparison by age")
        st.markdown("Age filter at top is NA for this section")
        
        fig2=px.line(df[mask3], x='Date', y='Value', facet_col='Age group', template='gridon')
        fig2.update_layout( width=1200, height=500)
        st.plotly_chart(fig2)
    
        # columns = st.columns((2,2))

        # with columns[0]:
        #     fig3 = px.line(df[mask4], x='Date', y='Value', color_discrete_sequence=["black"], title="Age 15 and over", template='plotly')
        #     fig3.update_layout(title_x=0.5, title_y=0.85)
        #     fig3.update_layout({'plot_bgcolor':'rgba(0, 0, 0, 0)'})
        #     st.plotly_chart(fig3)

        #     fig5 = px.line(df[mask5], x='Date', y='Value', color_discrete_sequence=["purple"], title="Age 15-24", template='presentation')
        #     fig5.update_layout(title_x=0.5, title_y=0.85)
        #     fig5.update_layout({'plot_bgcolor':'rgba(0, 0, 0, 0)'})
        #     st.plotly_chart(fig5)
            
        
        # with columns[1]:
        #     fig4 = px.line(df[mask7], x='Date', y='Value', color_discrete_sequence=["indigo"], title="Age 55 and over", template='ggplot2')
        #     fig4.update_layout(title_x=0.5, title_y=0.85)
        #     fig4.update_layout({'plot_bgcolor':'rgba(0, 0, 0, 0)'})
        #     st.plotly_chart(fig4)

        #     fig6 = px.line(df[mask6], x='Date', y='Value', color_discrete_sequence=["green"], title="Age 25-54", template='gridon')
        #     fig6.update_layout(title_x=0.5, title_y=0.85)
        #     fig6.update_layout({'plot_bgcolor':'rgba(0, 0, 0, 0)'})
        #     st.plotly_chart(fig6)

###     INDUSTRY

df2 = pd.DataFrame(pd.read_csv('Cleaned_Industry_V1.1.csv'))
# dataset for industries

with container:
    # st.markdown("___")
    with st.expander("Option 3 : Comparison by Industries"):
        st.subheader("Industry characteristics")
        st.markdown("Please use below Filters")

        characteristics2 = df2['Labour force characteristics'].unique().tolist()
        age_group2 = df2['Age group'].unique().tolist()
        gender2 = df2['Sex'].unique().tolist()
        area2 = df2['Geography'].unique().tolist()
        industry = df2['NAICS'].unique().tolist()

        

        columns = st.columns((2,2,2,2))

        with columns[0]:
            characteristics_selection2 = [st.radio("Industry Characteristics",
                                                characteristics2)]
        with columns[1]:
            age_group_selection2 = [st.radio('Industry Age Groups',
                                                age_group2)]
        with columns[2]:
            gender_selection2 = [st.radio('Industry Gender',
                                            gender2)]                              
        with columns[3]:
            area_selection2 = [st.radio('Industry Geography',
                                            area2)]
        # with columns[4]:
        #     industry_selection = [st.multiselect('Types of industries',
        #                                         industry,industry)]
        

        goods_industry = [ 'Agriculture', 'Forestry, fishing, mining, quarrying, oil and gas',
                            'Forestry and logging and support activities for forestry', 'Fishing, hunting and trapping', 'Mining, quarrying, and oil and gas extraction',
                            'Utilities', 'Construction', 'Manufacturing', 'Durables', 'Non-durables']
        services_industry = ['Wholesale and retail trade', 'Wholesale trade', 'Retail trade', 'Transportation and warehousing',
                            'Finance, insurance, real estate, rental and leasing', 'Finance and insurance', 'Real estate and rental and leasing',
                            'Professional, scientific and technical services', 'Business, building and other support services',
                            'Educational services', 'Health care and social assistance', 'Information, culture and recreation', 'Accommodation and food services',
                            'Other services (except public administration)', 'Public administration']
        industry2 = ['Services-producing sector','Goods-producing sector','Total, all industries','Unclassified industries']
        
        
        mask9 =  (df2['NAICS'].isin(goods_industry)) & (df2['Geography'].isin(area_selection2)) & (df2['Labour force characteristics'].isin(characteristics_selection2)) & (df2['Sex'].isin(gender_selection2)) & (df2['Age group'].isin(age_group_selection2))
        mask10 = (df2['NAICS'].isin(services_industry)) & (df2['Geography'].isin(area_selection2)) & (df2['Labour force characteristics'].isin(characteristics_selection2)) & (df2['Age group'].isin(age_group_selection2)) & (df2['Sex'].isin(gender_selection2))
        mask11 = (df2['NAICS'].isin(industry2)) & (df2['Geography'].isin(area_selection2)) & (df2['Labour force characteristics'].isin(characteristics_selection2)) & (df2['Age group'].isin(age_group_selection2)) & (df2['Sex'].isin(gender_selection2))



        fig7 = px.line(df2[mask11], x='Date', y='Value', color='NAICS', title= "Goods VS Services", template='simple_white')
        fig7.update_layout(title_x=0.5, title_y=0.9, width=900, height= 600)
        fig7.update_layout({'plot_bgcolor':'rgba(0,0,0,0)'})
        fig7.update_layout(xaxis=dict(tickmode = 'linear',
                                        tick0 = 2017,
                                        dtick = 1),
                            yaxis=dict(tickmode = 'linear',
                                        tick0 = 0,
                                        dtick = 2000))
        st.plotly_chart(fig7)

        fig8 = px.line(df2[mask9], x='Date', y='Value', color='NAICS', title= "Goods", template='simple_white')
        fig8.update_layout(title_x=0.5, title_y=0.9, width=900, height= 600)
        fig8.update_layout({'plot_bgcolor':'rgba(0,0,0,0)'})
        fig8.update_layout(xaxis=dict(tickmode = 'linear',
                                        tick0 = 2017,
                                        dtick = 1),
                        yaxis=dict(tickmode = 'linear',
                                        tick0 = 0,
                                        dtick = 100))
        fig8.update_layout(legend=dict(yanchor="top", y=0.9, xanchor="left", x=1.0))
        st.plotly_chart(fig8)


        fig9 = px.line(df2[mask10], x='Date', y='Value', facet_col='NAICS',
                            facet_col_wrap=3, title= "Services", template='gridon')
        fig9.update_layout(title_x=0.5, title_y=1.0, width=1200, height= 700)
        fig9.update_layout({'plot_bgcolor':'rgba(0,0,0,0)'})
        st.plotly_chart(fig9)

###         EDUCATION

df3 = pd.read_csv('Cleaned_Education_V1.1.csv')

with container:

    with st.expander("Option 4 : Comparison by Education"):

        st.subheader("Education characteristics")
        st.markdown("Please use below Filters")

        types_standards = df3['ISCED'].unique().tolist()
        types_gender = df3['Gender'].unique().tolist()
        types_status = df3['Status of student in Canada'].unique().tolist()
        types_geo = df3['Geography'].unique().tolist()
        
        columns =  st.columns((1,2))

        with columns[0]:    
            st.markdown(" ")
            st.markdown(" ")
            genders_selection  = [st.radio("Gender",
                                            types_gender)]
            standards_selection = [st.radio("Types of standards",
                                            types_standards)]
      
            status_selection = [st.radio("Status of student",
                                            types_status)]
        # with columns[3]:
        #     geo_selection = [st.multiselect("Geography",
        #                                 types_geo)]
        mask13 = (df3['Status of student in Canada'].isin(status_selection)) & (df3['Gender'].isin(genders_selection)) & (df3['ISCED'].isin(standards_selection))

        with columns[1]:
            fig10 = px.bar(df3[mask13], x='Geography', y='Value', color='Date', title='Education')
            fig10.update_layout(xaxis={'categoryorder':'total descending'})
            fig10.update_layout(title_x=0.5, title_y=0.9, width=900, height= 600)
            # fig10.update_layout({'plot_bgcolor':'rgba(0,0,0,0)'})
            st.plotly_chart(fig10)
            
            
        


        #mask12 = (df3['Status of student in Canada'].isin(status_selection)) & (df3['Geography'].isin(geo_selection)) & (df3['Gender'].isin(genders_selection)) & (df3['ISCED'].isin(standards_selection))
        
        

        # fig10 = px.bar(df3[mask13], x='Geography', y='Value', color='Date', title='Education')
        # fig10.update_layout(xaxis={'categoryorder':'total descending'})
        # fig10.update_layout(title_x=0.5, title_y=0.9, width=900, height= 600)
        # # fig10.update_layout({'plot_bgcolor':'rgba(0,0,0,0)'})
        # st.plotly_chart(fig10)


###     GOOGLE TRENDS
with container:
    # st.markdown("___")
    with st.expander("Option 5 : Additional info using Google trends"):

        st.subheader("Google trends on Job search")
        htmlfile=open("Google trend.html", 'r', encoding ='utf-8')
        source_code = htmlfile.read()
        print(source_code)
        components.html(source_code, height = 900, width = 1000)

##  dataset
# with container:
#     st.subheader("Filtered Dataset")
#     st.dataframe(df[mask1])
    
##   CREDITS
with container:
    st.markdown(" ")
    st.subheader('*Credits*')
    st.markdown("This project was created by Abhijeet Singh, Yinuo Liu and Zakayo Kisava for course Data-5000 at Carleton University taught by Prof. Majid Komeili.")
