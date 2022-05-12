# Creating a leaderboard using python
import pandas as pd
import streamlit as st

# Read the data
df = pd.read_csv("test.csv")
df = df.dropna()

# Sort the dataframe by Accuracy column
df = df.sort_values(by="Accuracy", ascending=False)
df["Mobile Number"] = df["Mobile Number"].astype(str)

# Remove the duplicates
df = df.drop_duplicates(subset="Mobile Number", keep="first")

# Create a table
st.title("Leaderboard")
st.table(df)
