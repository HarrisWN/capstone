import pandas as pd
import streamlit as st
import os

file_path = os.path.abspath("../capstone_src/data/clean_covid_pythondata5.csv")
df = pd.read_csv(file_path)
df
