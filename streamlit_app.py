import plotly.express as px
import pandas as pd
import streamlit as st
df = pd.read_csv("https://raw.githubusercontent.com/hadilfs/mortality2/main/lebanon_mortality_2.csv")
st.title("Visualization mortality rate in Lebanon")
selectedchart = st.sidebar.selectbox("Select a Visualization", ["Bar Chart", "Scatter Plot"])
slider = st.slider("Select a Year Range:", min_value=1960, max_value=2021, value=(1960,2021), step=1)
filtered_df =  df[(df['Year'] >= slider[0]) & (df['Year'] <= slider[1])]
if selectedchart == "Bar Chart":
    st.subheader("Using a Bar Chart")
    fig = px.bar(filtered_df,x='Year',y='Deaths')
    highest_value = st.checkbox("Highlight Highest Value")
    st.caption("***This bar chart shows the mortality rate in lebanon from 1960 to 2021. Each bar refers to a year and its height represents the rate of death in that year. Picking a certain time period using the range slider above, allows for a thorough analysis of the data.***")
    st.caption("***Checking on the 'Highlight Highest Value' box allows you to observe the bar which refers to the highest death rate in the year range you chose. Notably, the bar chart shows that in the year 1982 there was a sudden increase in the death rate which could be explained by the fact that in this year, the Israel Defense forces invaded the country in the midst of the Civil War. Also, a gradual increase is observed between the years 2019 and 2021 due to the COVID-19 pandemic.***")
    if highest_value:
          max_death = filtered_df[filtered_df['Deaths'] == filtered_df['Deaths'].max()]
          max_year = max_death['Year'].values
          fig.update_traces(marker=dict(color=['red' if year == max_year else 'blue' for year in filtered_df['Year']]))
    
elif selectedchart == "Scatter Plot":
        st.subheader("Using a Scatter plot")
        fig = px.scatter(filtered_df, x="Year", y="Deaths")
        highest_value = st.checkbox("Highlight Highest Value")
        st.caption("***This scatter plot shows the mortality rate in lebanon from 1960 to 2021. The X-coordinate of each point refers to a year and the Y-coordinate represents the rate of death in that year. Picking a certain time period using the range slider above, allows for a thorough analysis of the data.***")
        st.caption("***Checking on the 'Highlight Highest Value' box allows you to observe the point which refers to the highest death rate in the year range you chose. Notably, the scatter plot that in the year 1982 there was a sudden increase in the death rate which could be explained by the fact that in this year, the Israel Defense forces invaded the country in the midst of the Civil War. Also, a gradual increase is observed between the years 2019 and 2021 due to the COVID-19 pandemic.***")
        if highest_value:
          max_death = filtered_df[filtered_df['Deaths'] == filtered_df['Deaths'].max()]
          max_year = max_death['Year'].values
          fig.update_traces(marker=dict(color=['red' if year == max_year else 'blue' for year in filtered_df['Year']]))
        
st.plotly_chart(fig)
