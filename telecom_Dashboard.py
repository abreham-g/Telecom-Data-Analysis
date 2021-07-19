import streamlit as st
import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="tellco Data Analysis", layout="wide")



def loadData():
    print("loading started ")
    dataframe = pd.read_csv("./Clean.csv")
    print("loading complleted")
    return dataframe

dataframe =  loadData()
def selectUseroverview():
    userview1 = "Our Data"
    st.markdown(f"## {userview1}")
    st.write(dataframe.sample(100))
    userview2 = "Top Handset Type"
    st.markdown(f"## {userview2}")
    topHandSet = pd.DataFrame(dataframe['Handset Type'].head(10).value_counts())
    topHandName = topHandSet.index

    fig = px.bar( topHandSet,x=topHandName,  y='Handset Type')
    st.plotly_chart(fig)
    userview3 = "Top Handset Manufacturer"
    st.markdown(f"## {userview3}")
    topManufacture =  pd.DataFrame(dataframe['Handset Manufacturer'].value_counts().head(3))
    manu = topManufacture.index

    fig = px.bar( topManufacture,x=manu,  y='Handset Manufacturer')
    st.plotly_chart(fig)





    return 
  

def UserEngagement():
    engage = "User Engagement analysis"

    re_dataframe=dataframe.rename(columns = {'Total DL (Bytes)' : 'totalDL','Total UL (Bytes)' : 'totalUL','Dur. (ms)' : 'dur','MSISDN/Number':'msisdn','Last Location Name':'location','Handset Manufacturer':'manufacturer','Handset Type':'handset'})

    sum_column = re_dataframe["totalUL"] + re_dataframe["totalDL"]


    google = re_dataframe['Google DL (Bytes)']+ re_dataframe['Google UL (Bytes)']
    email = re_dataframe['Email DL (Bytes)']+ re_dataframe['Email UL (Bytes)']
    gaming = re_dataframe['Gaming DL (Bytes)']+ re_dataframe['Gaming UL (Bytes)']
    youtube = re_dataframe['Youtube DL (Bytes)']+ re_dataframe['Youtube UL (Bytes)']
    netflix = re_dataframe['Netflix DL (Bytes)']+ re_dataframe['Netflix UL (Bytes)']
    social = re_dataframe['Social Media DL (Bytes)']+ re_dataframe['Social Media UL (Bytes)']

    re_dataframe['google']=google
    re_dataframe['email']=email
    re_dataframe['gaming']=gaming
    re_dataframe['youtube']=youtube
    re_dataframe['netflix']=netflix
    re_dataframe['social']=social

    DataFrame=re_dataframe[['msisdn', 'google','email','gaming','youtube','netflix','social']]
    DataFrame["totalData"] = sum_column
    DataFrame.groupby('msisdn')['totalData'].sum()


    sumApplicationsDF = DataFrame.groupby('msisdn')[['google','youtube','netflix','social','email','gaming']].sum()
    argestApps=sumApplicationsDF[['google','youtube','netflix','social','email','gaming']].sum().nlargest(10)
    userviewre = "relationship between each application the total DL+UL data"
    st.markdown(f"## {userviewre}")
    
    fig = px.bar(argestApps,x=argestApps.index , y=argestApps.values)
    st.plotly_chart(fig)

    corr_df = DataFrame[['email','gaming','youtube','social','netflix']].corr(method ='pearson').corr()
    
    print(corr_df)
    userviewcor = "Correlation Analysis"
    st.markdown(f"## {userviewcor}")
    fig = px.imshow(corr_df)
    st.plotly_chart(fig)
    return 
def ExperienceAnalytics():
    exper = "Experience Analytics"
    return exper

def SatisfactionAnalysis():
    sat = "Satisfaction Analysis"
    return sat


st.sidebar.title("Telleco-Data-Analysis")
option = st.sidebar.selectbox('select result',('User Overview',
'User Engagement analysis',' Experience Analytics','Satisfaction Analysis'))
if option =='User Overview':
    selectUseroverview()
elif option == 'User Engagement analysis':

    UserEngagement()
elif option == 'Experience Analytics':
    ExperienceAnalytics()
elif option == 'Satisfaction Analysis':
    SatisfactionAnalysis()


#st.title(option)

