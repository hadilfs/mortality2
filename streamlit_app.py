import plotly.express as px
import pandas as pd
import streamlit as st
st.title("Visualization mortality rate in Lebanon")
st.subheader("Using a Bar Chart")
show_barchart=st.button("Click to Show Bar Chart")
if show_barchart:
    df = pd.read_csv("https://raw.githubusercontent.com/hadilfs/mortality2/main/lebanon_mortality_2.csv")
    fig = px.bar(df,x='Year',y='Deaths',color="Year")
    st.plotly_chart(fig)
    st.caption("***This bar chart shows the mortality rate in lebanon from 1960 to 2021***")
st.markdown("---")
st.title("Visualization mortality rate in Lebanon")
st.subheader("Using a Scatter plot")
show_scatterplot=st.button("Click to Show Scatter Plot")
if show_scatterplot:
    df = pd.read_csv("https://raw.githubusercontent.com/hadilfs/mortality2/main/lebanon_mortality_2.csv")
    fig1 = px.scatter(df, x="Year", y="Deaths",color="Deaths",color_continuous_scale="Reds")
    st.plotly_chart(fig1)
    st.caption("***This scatter plot shows the mortality rate in lebanon from 1960 to 2021***")
