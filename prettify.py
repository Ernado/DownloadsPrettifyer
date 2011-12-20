# -*- coding: utf-8 -*-
__author__ = 'Ernado'

import os, re, shutil
#regex for categories
#'categoryName" : 'regex"
categorize = {'images':"^.*\.(?i)(jpg|png|gif|bmp|ttf|psd)$",
              'archives':"^.*\.(?i)(zip|rar|7z|gz)$",
              'torrents':"^.*\.(?i)(torrent)$",
              'videos':"^.*\.(?i)(mpg|avi|)$",
              'documents':"^.*\.(?i)(djvu|pdf|doc|txt|docx|log|ppt|mht|html)$",
              'executable':"^.*\.(?i)(exe|msi)$",
              'music':"^.*\.(?i)(mp3|ogg|m3u|pls|plc)$",
              'code':'^.*\.(?i)(pas|py|cpp)$'}

#check for files
os.chdir('C:\Users\Ernado\Downloads')
curDir = os.curdir
files = os.listdir(curDir)
if file is None:
    exit()

print os.path.realpath(curDir)

#compile regex
categorize_compiled  = {}
for x in categorize:
    categorize_compiled.update({x:re.compile(categorize.get(x))})


#creating dirs for files if not exist
for x in categorize:
    if not os.path.exists(x):
        os.mkdir(x)

#move to subdirs
for file in files:
    for category in categorize_compiled:
        if os.path.isfile(file) and re.match(categorize_compiled.get(category),file):
            shutil.copy(file,category+'/'+file)
            os.remove(file)
            break
