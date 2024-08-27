import streamlit as st
import pandas as pd

# Load the dataset
st.title("Iris Dataset")
data = pd.read_csv(
    "https://raw.githubusercontent.com/dataprofessor/data/master/iris.csv"
)
st.write(data)
