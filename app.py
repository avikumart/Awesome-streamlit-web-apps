import streamlit as st
from pytube.__main__ import YouTube
st.title("Youtube Video Downloader")
st.subheader("Enter the URL:")
url = st.text_input(label='URL')
if url != '':
    yt = YouTube(url)
    st.image(yt.thumbnail_url, width=300)
    st.subheader('''
    {}
    ## Length: {} seconds
    ## Rating: {} 
    '''.format(yt.title , yt.length , yt.rating))
    video = yt.streams
    if len(video) > 0:
        downloaded , download_audio = False , False
        download_video = st.download_button("Download Video", data=video)
        if yt.streams.filter(only_audio=True):
            download_audio = st.download_button("Download Audio Only", data=video.filter(only_audio=True))
        if download_video:
           # video.get_lowest_resolution().download()
            downloaded == True
        if download_audio:
           # video.filter(only_audio=True).first().download()
            downloaded == True
        if downloaded:
            st.subheader("Download Complete")
            import subprocess
            subprocess.run(["ls"])
    else:
        st.subheader("Sorry, this video can not be downloaded")
