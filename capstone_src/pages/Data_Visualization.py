import pandas as pd
import streamlit as st
import os

file_path = os.path.abspath("../capstone_src/data/clean_covid_pythondata5.csv")
df = pd.read_csv(file_path)


import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Sample data (replace this with your data)


# Create a new column to group by year and month

# Streamlit UI
vis_to_use = [
    "Line graph for Time Series Data",
    "Box Plot of Annual Mean Data",
    "Bar Chart of Monthly Averages",
]
type_vis = st.selectbox(
    "Select the type of visualization you would like to see:", options=vis_to_use
)

if type_vis == "Line graph for Time Series Data":
    answer1 = st.selectbox(
        "Select a Column for Line 1 (Y-axis)", options=sorted(list(df.columns))
    )
    answer2 = st.selectbox(
        "Select a Column for Line 2 - optional(Y-axis)",
        options=sorted(list(df.columns)),
    )

    if answer1 or answer2:
        try:
            # Create a line chart
            st.subheader("Time Series Covid Data")
            fig1 = px.line(df, x="time", y=[answer1, answer2], title="Covid Over Time")
            st.plotly_chart(fig1)
        except BaseException:
            st.write("Error visualizing the lines!")

elif type_vis == "Box Plot of Annual Mean Data":
    answer1 = st.selectbox(
        "Select a Column for Y-axis", options=sorted(list(df.columns))
    )
    if answer1:
        try:
            st.subheader(f"Box Plot of {answer1}")
            plt.figure(figsize=(10, 6))
            sns.boxplot(y=answer1, data=df)
            plt.title(f"Box Plot of {answer1}")
            plt.ylabel(f"2023 {answer1}")
            st.pyplot(plt)
        except BaseException:
            st.write("Error visualizing the box plot!")

elif type_vis == "Bar Chart of Monthly Averages":
    answer1 = st.selectbox(
        "Select a Category for Y-axis", options=sorted(list(df.columns))
    )
    if answer1:
        try:
            st.subheader(f"Bar Chart of Monthly Averages for {answer1}")
            # Group the DataFrame by day_and_year and calculate the mean
            grouped_data = df.groupby("monthly")[answer1].mean().reset_index()

            # Create a bar chart using seaborn
            plt.figure(figsize=(10, 6))
            sns.barplot(x="monthly", y=answer1, data=grouped_data)
            plt.title(f"Bar Chart of Monthly Averages for {answer1}")
            plt.xlabel("Month")
            plt.ylabel(f"Monthly Average {answer1}")
            plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
            plt.tight_layout()

            # Display the bar chart
            st.pyplot(plt)
        except BaseException:
            st.write("Error visualizing the bar chart!")
