import streamlit as st
from PIL import Image

image = Image.open("dashboard.jpg")

st.image(image, caption="Covid Dashboard")


st.title("Summary")


st.text(
    "This data can be used to determine COVID19 trends including the relationship between new cases and new deaths. The data also standardizes the data to the size of population 1M to better reflect the scale. ETL  was performed in Python using VS Code and then visualized using plotly. The streamlit app was used to make these data accessible and promote interaction"
)
