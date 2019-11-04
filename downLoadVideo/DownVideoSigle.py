# -*- coding: utf-8 -*
import locale
import re, os, requests
from PyQt5 import QtCore
#download_link = "https://youtu.be/" + videoId  # 构造下载地址
#locale.setlocale(locale.LC_ALL,'en')
class countNum():
        count = 0

def handle_camsave(self):
    # download_link = "https://www.youtube.com/watch?v=zxaI2v7ZqDk"  # 构造下载地址
    countNum.count+=1
    if 1:
        #download_link = self.plainTextEdit.document().findBlockByNumber(0).text()
        download_link=self.textEdit.toPlainText()
        print(download_link)
        if len(download_link):
            self.webEngineView.setUrl(QtCore.QUrl(download_link))
            os.chdir(r"/Users/ptc/Downloads")
            os.system("youtube-dl " + download_link)  # 用youtube-dl下载视频



