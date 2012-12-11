#/usr/bin/python
# coding: utf-8
#!/usr/bin/python
 # coding: utf-8
 

import httplib
import json
import os
import sys
import subprocess
import time
import webbrowser
reload(sys)
sys.setdefaultencoding('utf-8')

while True:
    httpConnection = httplib.HTTPConnection('douban.fm')
    httpConnection.request('GET', '/j/mine/playlist?type=n&channel=0')
    song = json.loads(httpConnection.getresponse().read())['song']
    picture = 'images/' + song[0]['picture'].split('/')[4]
    if not os.path.exists(picture):
        subprocess.call([
             'wget',
             '-P',
             'images',
             song[0]['picture']])
    subprocess.call([
         'notify-send',
         '-i',
         os.getcwd() + '/' + picture,
         song[0]['title'],
         song[0]['artist'] + '\n' + song[0]['albumtitle']])
    webbrowser.open(song[0]['url'])
    time.sleep(song[0]['length']) 

