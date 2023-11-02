import pandas as pd
import os

file_path = os.path.abspath("../capstone_src/data/clean_covid_pythondata5.csv")
df = pd.read_csv(file_path)
df

# FORMAT QUERY
import streamlit as st

st.title("Query Data By Month and Case Type")

# Input widgets in the sidebar

month_filter = st.multiselect("Filter by month", df["month"].unique())

with st.sidebar:
    # Create widgets for user input
    new_cases_filter = st.slider(
        "Filter by Reported New Cases", min_value=0, max_value=5000, step=100, value=0
    )
    active_cases_filter = st.slider(
        "Filter by Reported Active Cases",
        min_value=0,
        max_value=1500000,
        step=10000,
        value=0,
    )
    critical_cases_filter = st.slider(
        "Filter by Reported Critical Cases",
        min_value=0,
        max_value=3500,
        step=100,
        value=0,
    )
    recovered_cases_filter = st.slider(
        "Filter by Reported Recovered Cases",
        min_value=0,
        max_value=1500000,
        step=10000,
        value=0,
    )


# Perform data filtering based on user input
filtered_data = df
if new_cases_filter is not None:
    filtered_data = filtered_data[filtered_data["new_cases"] >= new_cases_filter]
""""""


""""""

if active_cases_filter is not None:
    filtered_data = filtered_data[filtered_data["active_cases"] >= active_cases_filter]
""""""


""""""
if critical_cases_filter is not None:
    filtered_data = filtered_data[
        filtered_data["critical_cases"] >= critical_cases_filter
    ]
""""""


""""""
if recovered_cases_filter is not None:
    filtered_data = filtered_data[
        filtered_data["recovered_cases"] >= recovered_cases_filter
    ]


# Display the filtered data
st.write(f"Filtered Data (count: {len(filtered_data)}):")
st.write(filtered_data)

st.line_chart()
