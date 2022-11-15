import streamlit as st
from transcribe import *
import time

# streamlit UI

st.header("Transcribe Your Audio Files")
fileObject = st.file_uploader(label = "Please upload your file" )


if fileObject:
    token, t_id = upload_file(fileObject)
    result = {}
    #polling
    sleep_duration = 1
    percent_complete = 0
    progress_bar = st.progress(percent_complete)
    st.text("Currently in queue")
    while result.get("status") != "processing":
        percent_complete += sleep_duration
        time.sleep(sleep_duration)
        progress_bar.progress(percent_complete/10)
        result = get_text(token,t_id)
    sleep_duration = 0.01
    for percent in range(percent_complete,101):
        time.sleep(sleep_duration)
        progress_bar.progress(percent)
        # streamlit UT
        st.balloons()
        st.header("Transcribed Text")
        st.subheader(result['text'])

# further scope:
#1) AssemblyAI lets the user specify the acoustic model and/or language model. 
# You could use Streamlit’s selectbox to build a drop-down-like feature.

#2) Add a feature that lets the user record their voice and transcribe it.
# This might be slightly complicated since Streamlit doesn’t have any built-in components to record voice.
# However, you can use HTML and JavaScript to build such a feature.


