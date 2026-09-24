import streamlit as st
import pandas as pd

st.title("Student Performance Prediction and Clustering")

df = pd.read_csv("student_performance.csv")
st.subheader("Dataset")
st.dataframe(df)

st.subheader("Cluster Distribution")
st.bar_chart(df["Cluster"].value_counts())
