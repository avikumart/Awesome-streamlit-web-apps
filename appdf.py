# streamlit editable dataframe experiment
import pandas as pd
import streamlit as st

# read the csv
df = pd.read_csv("bank.csv")


# editable dataframe
st.markdown("<h1 style='text-align: center;'>Edit the dataframe to update customer data</h1>", unsafe_allow_html=True)
edit_df = st.experimental_data_editor(df)
