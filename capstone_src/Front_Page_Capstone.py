import streamlit as st
from PIL import Image

image = Image.open("Coronavirus.jpg")

st.image(image, caption="Coronavirus")


st.title("2023 US Covid19 Trends")
st.text(
    "COVID19 statics for 2023: tests, cases, and deaths. This application used Pandas, Plotly,  Streamlit,SKLearn, MongoDB, and Python to create interactive COVID data "
)

st.header("Pages")

st.subheader("~Data Table View")
st.text("View columns and scan data sets")

st.subheader("~Data Visualization")
st.text("View times series and mean data points")

st.subheader(" ~Query")
st.text("Query: return data by month")

st.subheader("~ Summary")
st.text(
    "This data can be used to determine COVID19 trends including the relationship between new cases and new deaths. The data also standardizes the data to the size of population 1M to better reflect the scale. ETL was performed in Python using VS Code and then visualized using plotly"
)
