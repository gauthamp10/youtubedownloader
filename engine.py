from __future__ import unicode_literals
from youtubesearchpython import SearchVideos
import youtube_dl
import json


def get_video_info(url):
    ydl_opts = {}
    print(url)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        meta = ydl.extract_info(url, download=False)
        vid_quality=list() 
        for quality in meta['formats']:
            vid_quality.append(quality)
        return meta['title'],meta['thumbnail'],vid_quality




def youtube_search(query):
    search = SearchVideos(query, offset = 1, mode = "json", max_results = 40)  
    data = json.loads(search.result())
    data = data['search_result']	
    ids = [item['id'] for item in data]
    titles = [item['title'] for item in data]  
    vid=dict(zip(ids, titles))
    return vid


