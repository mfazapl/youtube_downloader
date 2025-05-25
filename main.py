import streamlit as st
import yt_dlp
import os


def video_donwloader(url):
    try:
        os.makedirs('./Downloads', exist_ok=True)
        progress_bar= st.progress(0)

        def progress_hook(d):
            if d['status'] == 'downloading':
                total_bytes= d.get('total_bytes') or d.get('total_bytes_estimate')
                download_bytes= d.get('download_bytes', 0)
                if total_bytes:
                    progress = int(download_bytes/total_bytes *100)
                    progress_bar.progress(progress)
            elif d['status'] =='finished':
                progress_bar.progress(100)

        ydl_opts={
            'outtmpl':'./Downloads/%(title)s.%(ext)s',
            'format':'bestvideo+bestaudio/best',
            'merge_output_format':'mp4',
            'progress_hook': [progress_hook],
            'noplaylist':True,
            }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info= ydl.extract_info(url, download=True)

  
        st.success(info.get('title', 'Complete'))
    except Exception as e:
        st.error('Download Failed')
        

def url_yutub():
    st.title("Youtube Donwloader")
    url= st.text_input("Enter Youtube URL")
    if st.button("Download"):
        if not url:
            st.warning("Please enter a valid URL")
        else:
            video_donwloader(url)

if __name__ == '__main__':
    url_yutub()

