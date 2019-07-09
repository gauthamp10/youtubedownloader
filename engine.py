from __future__ import unicode_literals
import youtube_dl
import urllib
import requests
from bs4 import BeautifulSoup
import json

def get_video_info(url):
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        meta = ydl.extract_info(url, download=False)
        vid_quality=list() 
        for quality in meta['formats']:
            vid_quality.append(quality)
        return meta['title'],meta['thumbnail'],vid_quality




def youtube_search(query):
    query = urllib.parse.quote(query)
    url = "https://www.youtube.com/results?search_query=" + query
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    headers = {'User-Agent': user_agent}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    vid_list=list()
    title_list=list()
    for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
        if vid['href'].startswith('/watch'):
            vid_list.append('https://www.youtube.com' + vid['href'][:20])
            title_list.append(vid.text)
        else:
            pass
    vid=dict(zip(vid_list, title_list))
    return vid


