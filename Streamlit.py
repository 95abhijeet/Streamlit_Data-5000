from re import template
from matplotlib.axis import YTick
from matplotlib.pyplot import figure, title, xticks
from sqlalchemy import Column
import streamlit as st
import streamlit.components.v1 as  components
import pandas as pd
import plotly
import plotly.express as px
import plotly.io as pio
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
from sklearn import tree
from PIL import Image

st.set_page_config(page_title='Data 5000 project', layout='wide') 
                                                #    menu_items={
                                                #                'Get Help': '<95abhijeet@gmail.com>',
                                                #                'Report a bug': "<95abhijeet@gmail.com>"})
                                                              #  'About': "# This is a header. This is an *extremely* cool app!"})
import time
with st.spinner('Wait for it...'):
    time.sleep(2)
st.success('Page loading complete')
st.balloons()

st.title('The Impact of COVID-19 on Labour Market')

container = st.container()



###         COMPARISON BY GENDER

with container:
    
    
    st.write("This page provides visualizations on various indicators to learn about the impact of Covid-19 on labour market.  \n"
             "There are about four indicators that can be examined along with observations listed below:  \n"
            "Section 1 : Gender  \n"
            "Section 2 : Age  \n"
            "Section 3 : Industries  \n"
            "Section 4 : Education  \n"
            "Section 5 : Machine learning model  \n"
            "Section 6 : Observations based on Google trends")
    st.markdown("___")

    with st.expander("Section 1 : Gender"):
    
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
        gender_males = ['Males']
        gender_females = ['Females']
        all_age = ['15 to 24 years','25 to 54 years','55 years and over']
        age_15_over = ['15 years and over']
        age_15_24 = ['15 to 24 years']
        age_25_54 = ['25 to 54 years']
        age_55_over = ['55 years and over']

        ## Dataframe filter/mask

        mask1 = (df['Geography'].isin(area_selection)) & (df['Labour force characteristics'].isin(characteristics_selection)) & (df['Sex'].isin(gender_selection)) & (df['Age group'].isin(age_group_selection))
        mask2 = (df['Geography'].isin(area_selection)) & (df['Labour force characteristics'].isin(characteristics_selection)) & (df['Age group'].isin(age_group_selection)) & (df['Sex'].isin(gender_males))
        mask14 = (df['Geography'].isin(area_selection)) & (df['Labour force characteristics'].isin(characteristics_selection)) & (df['Age group'].isin(age_group_selection)) & (df['Sex'].isin(gender_females))
        mask3 = (df['Geography'].isin(area_selection)) & (df['Labour force characteristics'].isin(characteristics_selection)) & (df['Age group'].isin(all_age)) & (df['Sex'].isin(gender_selection))
        mask4 = (df['Geography'].isin(area_selection)) & (df['Labour force characteristics'].isin(characteristics_selection)) & (df['Sex'].isin(gender_selection)) & (df['Age group'].isin(age_15_over))
        mask5 = (df['Geography'].isin(area_selection)) & (df['Labour force characteristics'].isin(characteristics_selection)) & (df['Sex'].isin(gender_selection)) & (df['Age group'].isin(age_15_24))
        mask6 = (df['Geography'].isin(area_selection)) & (df['Labour force characteristics'].isin(characteristics_selection)) & (df['Sex'].isin(gender_selection)) & (df['Age group'].isin(age_25_54))
        mask7 = (df['Geography'].isin(area_selection)) & (df['Labour force characteristics'].isin(characteristics_selection)) & (df['Sex'].isin(gender_selection)) & (df['Age group'].isin(age_55_over))
        mask8 = (df['Geography'].isin(area_selection)) & (df['Labour force characteristics'].isin(characteristics_selection))
        st.subheader("Gender classification")
        st.markdown("*Gender filter at top is not applicable for this section*")

        columns = st.columns((2,2))

        with columns[0]:
            fig1 = px.line(df[mask2], x = 'Date', y = 'Value', title = 'Males', template='xgridoff')
            fig1.update_layout( width=550, height = 425)
            # fig1.update_layout({#'plot_bgcolor':'rgba(250, 240, 230, 0.5)',
            #                     'paper_bgcolor':'#AFEEEE'})
            st.plotly_chart(fig1)

        with columns[1]:
            fig2 = px.line(df[mask14], x = 'Date', y = 'Value', title='Females' , template='xgridoff')
            fig2.update_layout( width=550, height = 425)
            # fig2.update_layout({'plot_bgcolor':'rgba(255, 0, 0, 0.2)'})
            st.plotly_chart(fig2)

#         st.markdown("*We can write some description here*")
#         st.write("An exploratory analysis of unemployment by gender in the labour market shows that there is a sharp increase from January to May 2020  \n"
#                  "for both males and females. This may be influenced by the initial increase at COVID-19 that led to restrictions on labour mobility and  \n"
#                  "the cessation of economic activity in the Ontario region.")

###         COMPARISION BY AGE
with container:

    with st.expander("Section 2 : Age"):
        st.subheader("Age classification")
        st.markdown("*This section uses same filter as Section 1*  \n"
                    "*Age filter at top is not applicable for this section*")
        
#         columns = st.columns((3,2))

#         with columns[0]:
        # st.markdown("___")
       
        fig4=px.line(df[mask4], x='Date', y='Value',title ='Age 15 and above', template='xgridoff')
        fig4.update_layout( width=800, height=450)
        st.plotly_chart(fig4)

        fig3=px.line(df[mask3], x='Date', y='Value', facet_col='Age group', template='xgridoff')
        fig3.update_layout( width=800, height=350)
        st.plotly_chart(fig3)

#         with columns[1]:
#             st.markdown("The plot shows a sudden increase in unemployment in the 15-24 age group between January to May 2020 compared to other groups.  \n"
#                         "The age of 15-24 is a transition from school to work, which means that they are inexperienced in the labour market and  \n"
#                         "cannot obtain jobs with high security during the pandemic.")

    
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
    with st.expander("Section 3 : Industries"):
        st.subheader("Industry classification")
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

        columns = st.columns((1,6,1))
        with columns[0]:
          st.markdown("")
        with columns[1]:
          fig7 = px.line(df2[mask11], x='Date', y='Value', color='NAICS', title= "Goods VS Services",color_discrete_sequence=px.colors.qualitative.Dark2, template ='ygridoff')
          fig7.update_layout(title_x=0.5, title_y=0.9, width = 900, height=500)
          # fig7.update_layout({'plot_bgcolor':'rgba(0,0,0,0)'})
          fig7.update_layout(xaxis=dict(tickmode = 'linear',
                                          tick0 = 2017,
                                          dtick = 1))

          st.plotly_chart(fig7)
        with columns[2]:
          st.markdown("")
          
          
          
        columns = st.columns((2,2))
        with columns[0]:
            fig8 = px.line(df2[mask9], x='Date', y='Value', color='NAICS', title= "Goods", template='ygridoff')
            fig8.update_layout(title_x=0.5, title_y=0.85, width = 550, height=500)
            # fig8.update_layout({'plot_bgcolor':'rgba(0,0,0,0)'})
            fig8.update_layout(xaxis=dict(tickmode = 'linear',
                                            tick0 = 2017,
                                            dtick = 1))
#                             yaxis=dict(tickmode = 'linear',
#                                             tick0 = 0,
#                                             dtick = 100))
            fig8.update_layout(legend=dict(yanchor="top", y=0.9, xanchor="left", x=1.0))
            st.plotly_chart(fig8)

        with columns[1]:
            fig9 = px.line(df2[mask10], x='Date', y='Value',#, facet_col='NAICS',facet_col_wrap=3, 
                            color ='NAICS', title= "Services",template='ygridoff')
            fig9.update_layout(title_x=0.5, title_y=0.85, width = 550, height=500)
            # fig9.update_layout({'plot_bgcolor':'rgba(0,0,0,0)'})
            fig9.update_layout(xaxis=dict(tickmode = 'linear',
                                            tick0 = 2017,
                                            dtick = 1))
#                             yaxis=dict(tickmode = 'linear',
#                                             tick0 = 0,
#                                             dtick = 100))
            st.plotly_chart(fig9)


#         st.markdown("The plot shows the impulsive decline in all industries in the goods and services sector at the beginning of COVID-19.  \n"
#                     "The decline is due to COVID-19, which led to the shutdown of economic activities and the restriction of labour mobility  \n"
#                     "and the cessation of trade between countries.")



###         EDUCATION

df3 = pd.read_csv('Cleaned_Education_V1.1.csv')

with container:

    with st.expander("Section 4 : Education"):

        st.subheader("Education classification")
        st.markdown("Please use below Filters")

        types_standards = df3['ISCED'].unique().tolist()
        types_gender = df3['Gender'].unique().tolist()
        types_status = df3['Status of student in Canada'].unique().tolist()
        types_geo = df3['Geography'].unique().tolist()
        
        columns =  st.columns((2,2,2,2))

        with columns[0]:    
            standards_selection = [st.radio("Types of standards",
                                            types_standards)]
            
        with columns[1]:
            genders_selection  = [st.radio("Gender",
                                            types_gender)]
    
        with columns[2]:
            status_selection = [st.radio("Status of student",
                                        types_status)]
        with columns[3]:
            st.markdown(" ")
        
        geography1 = ['Canada']
        geography2 = ['Alberta','British Columbia','Manitoba','New Brunswick','Newfoundland and Labrador','Nova Scotia','Ontario','Prince Edward Island','Quebec','Saskatchewan','Territories']
        geography = ['Canada', 'Alberta','British Columbia','Manitoba','New Brunswick','Newfoundland and Labrador','Nova Scotia','Ontario','Prince Edward Island','Quebec','Saskatchewan','Territories']
        # with columns[3]:
        #     geo_selection = [st.multiselect("Geography",
        #                                 types_geo)]
        #mask12 = (df3['Status of student in Canada'].isin(status_selection)) & (df3['Geography'].isin(geo_selection)) & (df3['Gender'].isin(genders_selection)) & (df3['ISCED'].isin(standards_selection))
        
        mask13 = (df3['Status of student in Canada'].isin(status_selection)) & (df3['Gender'].isin(genders_selection)) & (df3['ISCED'].isin(standards_selection)) & (df3['Geography'].isin(geography))
        mask14 = (df3['Status of student in Canada'].isin(status_selection)) & (df3['Gender'].isin(genders_selection)) & (df3['ISCED'].isin(standards_selection)) & (df3['Geography'].isin(geography2))
        

        fig10 = px.bar(df3[mask13], x='Value', y='Geography', color='Date', title='Education',
                            color_discrete_sequence=px.colors.qualitative.Set3, template ='ygridoff')
        fig10.update_layout(yaxis={'categoryorder':'total ascending'})
        fig10.update_layout(title_x=0.5,yaxis_title=None, width=1150, height= 550)
        fig10.update_yaxes(tickangle=0,ticklabelposition="inside top")
        fig10.update_layout(legend=dict(
                            yanchor="bottom",
                            y=0.01,
                            xanchor="right",
                            x=0.9))
        # fig10.update_layout({'plot_bgcolor':'rgba(0,0,0,0)'})
        st.plotly_chart(fig10)

        # fig11 = px.bar(df3[mask14], x='Value', y='Geography', color='Date', title='Education', 
        #     color_discrete_sequence=px.colors.qualitative.Set3, template ='ygridoff')
        # fig11.update_layout(yaxis={'categoryorder':'total ascending'})
        # fig11.update_layout(title_x=0.5,yaxis_title=None, width=1700, height= 800)
        # fig11.update_yaxes(tickangle=0,ticklabelposition="inside top")
        # fig11.update_layout(legend=dict(
        #                     yanchor="bottom",
        #                     y=0.01,
        #                     xanchor="right",
        #                     x=0.8))
        # # fig11.update_layout({'plot_bgcolor':'rgba(0,0,0,0)'})
        # st.plotly_chart(fig11)
        
        st.markdown(" ")

                        
with container:
    with st.expander("Section 5 : Machine learning model"):
        df4= pd.DataFrame(pd.read_csv("ML combined Can.csv"))   

        #Normalization
        sc= MinMaxScaler()
        first = sc.fit_transform(df4)
        scaled = pd.DataFrame(first, columns = df4.columns)
        

        X = scaled.drop(['Unemployment rate','Employment', 'Employment rate', 'Unemployment', 
                'Part time employment', 'Full time employment' ], axis=1)
        y = scaled["Unemployment rate"]

        if st.button('Click the button to run the model'):
            st.subheader("Random Forest Regressor Model")
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

            regressor = RandomForestRegressor()
            yoyo = regressor.fit(X_train, y_train)
            y_pred = regressor.predict(X_test)

            mae = metrics.mean_absolute_error(y_test, y_pred)
            
            mse = metrics.mean_squared_error(y_test, y_pred)
            
            rmse = np.sqrt(metrics.mean_squared_error(y_test, y_pred))
            
            r2 = r2_score(y_test, y_pred)

            columns = st.columns((1,1,1,1))

            with columns[0]:
                st.markdown("Mean absolute error: " + str(mae))
            with columns[1]:
                st.markdown("Mean squared error: " + str(mse))
            with columns[2]:
                st.markdown("Root mean squared error: " + str(rmse))
            with columns[3]:
                st.markdown("Coefficient of determination (R2): " + str(r2))

            feature_list = list(X.columns)
            st.markdown(" ")
            st.caption("One decision tree from the random forest regressor model")
            fn=X.columns
            cn=['Unemployment rate']
            fig12 =plt.figure(dpi=1200, figsize=(4,2))
            tree.plot_tree(yoyo.estimators_[0],
                            feature_names = fn, 
                            class_names=cn,
                            filled = True,
                                fontsize=4)
                           
            st.pyplot(fig12)
            

            # st.markdown(" ")

            # image = Image.open('random forest1.png')
            # st.image(image, caption = 'Random Forest Regressor Estimators',  output_format='PNG')

            # fig11 = plt.figure(figsize=(5,5))
            # plt.scatter(y_test,y_pred,color='g', alpha=0.5)
            # plt.ylabel("Predicted Values")
            # plt.xlabel("Actual Values")
            # plt.title("Figure 6: Decision Tree Regressor Prediction")
            # st.pyplot(fig11)

        else:
            st.write(' ') #space with no statement
        
        

        


###     GOOGLE TRENDS
with container:
    # st.markdown("___")
    with st.expander("Section 6 : Additional information using Google trends"):

#         st.subheader("Google trends on Job search")
        htmlfile=open("Google trend.html", 'r', encoding ='utf-8')
        source_code = htmlfile.read()
        print(source_code)
        components.html(source_code, height = 900, width = 1000)
        
        st.markdown("")
#         st.markdown("The line chart illustrates the comparison between Canadian emergency response benefits and job search interest.  \n"
#                     "At the beginning of COVID-19 in April 2020, there is a gradual drop in job search interest, which is influenced  \n"
#                     "by the availability of CERB weekly benefits.")
##  dataset
# with container:
#     st.subheader("Filtered Dataset")
#     st.dataframe(df[mask1])
    
##   CREDITS
with container:
    st.markdown(" ")
    st.subheader('*Credits*')
    st.markdown("This project was created by Abhijeet Singh, Yinuo Liu and Zakayo Kisava for course Data-5000 at Carleton University taught by Prof. Majid Komeili.")
