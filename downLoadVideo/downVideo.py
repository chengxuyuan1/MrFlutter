# -*- coding: utf-8 -*
import re, os, requests

url = r"https://www.youtube.com/playlist?list=PLXO45tsB95cK7G-raBeTVjAoZHtJpiKh3"    #youtube播放列表
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
html = requests.get(url, headers=headers).text
videoIds = re.findall('"videoId":"([A-Za-z0-9_-]{11})","thumbnail"', html)
for videoId in videoIds:
    download_link = "https://youtu.be/" + videoId  # 构造下载地址
    os.chdir(r"/Users/ptc/Downloads")
    os.system("youtube-dl " + download_link)  # 用youtube-dl下载视频