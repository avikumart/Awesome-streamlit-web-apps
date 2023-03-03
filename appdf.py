# streamlit editable dataframe experiment
import pandas as pd
import streamlit as st

# read the csv
df = pd.read_csv("bank.csv")


# editable dataframe
st.markdown(<h1>"Edit the dataframe to update customers' data"</h1>)
edit_df = st.experimental_data_editor(df)
