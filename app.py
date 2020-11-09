from flask import Flask
from flask import request, send_from_directory
from flask import render_template
import os
import youtube_dl
from engine import *
import re

port = int(os.environ.get("PORT", 5000))
app = Flask('app')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


@app.route("/")
def home():
    return render_template('index.html',link="#")

@app.route("/",methods=['GET','POST'])
def home_post():
    url = request.form['url']
    if(re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', url)):
        title,thumbnail,video_data=get_video_info(url)
        return render_template('index.html',title=title,thumbnail=thumbnail,data=video_data,link='#')
    else:
        vid=youtube_search(url)
        if vid == None:
            return render_template('404.html'), 404
        return render_template('results.html',vid=vid)
        
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=port)





if __name__ == '__main__':
    app.run(debug=True)
