import streamlit as st
from scrape import getData

info = {}
repo_info = {}

st.title("Github Scraper")
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
        st.subheader(" Recent Repositories")
        st.table(repo_info)
    except:
        st.subheader("User doesn't exist")
