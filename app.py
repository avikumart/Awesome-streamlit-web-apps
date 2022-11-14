import streamlit as st
from scrape import getData
import pandas as pd

info = {}
repo_info = {}

st.title("Awesome Github Profile Scraper")
userName = st.text_input('Enter Github Username')

if userName != '':
    try:
        info, repo_info = getData(userName)
        for key , value in info.items():
            if key != 'image_url':
                st.subheader(
                '''
                {} : {}
                '''.format(key, value)
                )
            else:
                st.image(value)
        st.subheader("Recent Repositories")
        st.table(repo_info)
    except:
        st.subheader("User doesn't exist")
        
df = pd.DataFrame(repo_info)

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(df)

if userName != '':
    st.download_button(label="Download profile data as CSV",
    data=csv,
    file_name='Gh_profile_df.csv',
    mime='text/csv')
