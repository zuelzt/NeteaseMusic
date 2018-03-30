#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 14:25:25 2018

@author: Rorschach
@mail: 188581221@qq.com
"""
import warnings
warnings.filterwarnings('ignore')

import re
import urllib.request
import urllib.error
import urllib.parse
import json

def get_all_hotSong():
    url = 'http://music.163.com/discover/toplist?id=3778678'
    header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'}
    request = urllib.request.Request(url=url, headers=header)
    html = urllib.request.urlopen(request).read().decode('utf8')  #打开url
    html = str(html)
    
    pat1 = r'<ul class="f-hide"><li><a href="/song\?id=\d*?">.*?</a></li></ul>'   #提取行
    result = re.compile(pat1).findall(html)
    result = result[0]  #List 提取 str
    
    pat2 = r'<li><a href="/song\?id=\d*?">(.*?)</a></li>'   #歌名
    pat3 = r'<li><a href="/song\?id=(\d*?)">.*?</a></li>'   #ID
    hot_song_name = re.compile(pat2).findall(result)
    hot_song_id = re.compile(pat3).findall(result)
    return hot_song_name, hot_song_id


def get_hotComments(hot_song_name, hot_song_id):
    url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_' + hot_song_id + '?csrf_token=6f5ba69387e105d69a27bf54b22e80a2'
    header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'}
    
    data = {'params':'Ma0J8Mg6KkT3AZeSsDnG+ZxOUrHTfrqgMz5Yugfzx4QMliPKp4K/yMqSJMvK+MrO/iOf00nJkThbO3ziszltGHuuDR5qn/tGf5PPTp7oBJAZl2U9/jBChAWHKWNaNLAdFeA4po4oVHVLzX+trqvTxC0C9A09ts+6MwrnzTtzBO44qgMpU6WHVhPwT2NC6AvzFAGSCl5svCk6CuRqj8LdF9zYaNIwQoXOLxQHR/RO0Og=',
            'encSecKey':'4328773733c1b0ee240b007b0f92728b0b1acb313a6fc81a9943c4a5e47cdec879e8f5d6166860b0726074d745cd75e13245003411a58314479630223fa8ad021a13ee8be413d1a6741695a68cb45246e49b90d06f7baa00bc5794d11a88b0b598014477de771d0a79d14b36d2fa0e4c67ce6d1e9c53ea42471c28df28f2cfba'}
    postdata = urllib.parse.urlencode(data).encode('utf8')   #不知道编什么码
    request = urllib.request.Request(url, headers=header, data=postdata)
    reponse = urllib.request.urlopen(request).read().decode('utf8')
    json_dict = json.loads(reponse)  #获取json
    hot_commit = json_dict['hotComments']
    
    #写入文件
    num = 0
    fhandle = open('./song_comments', 'a')
    fhandle.write(hot_song_name + ':' + '\n')
    
    for i in hot_commit:
        num += 1
        fhandle.write(str(num) + '.' + i['content'] + '\n')
    
    fhandle.write('\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n\n')
    fhandle.close()
    


#测试
hot_song_name, hot_song_id = get_all_hotSong()
    
num = 0
while num < len(hot_song_name):
    print('正在抓取第{}首歌的热评...'.format(num + 1))
    get_hotComments(hot_song_name[num], hot_song_id[num])
    print('φ(0￣*)啦啦啦_φ(*￣0￣)′')
    num += 1
    
    
    
    
    
    
    
    
    

































































































