#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 17:10:07 2018

@author: Rorschach
@mail: 188581221@qq.com
"""
import warnings
warnings.filterwarnings('ignore')



import urllib.request
import urllib.error
import urllib.parse
import json


##detail........
def get_Song():
    url = 'http://music.163.com/weapi/v3/playlist/detail?csrf_token=96a4ade298c2d7895fd9e6205b673459'
    header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'}
    data = {'params':'uRWE6HGsgPGYdCdKZRF4mHBfHg5PcCxnhN7XV5smAZjWXWs6sOQRogq8KDDxML7H+Bd/RNTrwcacyMHIhCy1U/b8OTnBxsjEDEtJJEaF0ST90vlRkD030djJardklRlFVxIl5mhSe77PC7mDBLWSDY2IIaIcIXcOovrkIS9Pf8HugRwpfdmfmdB0CGiAKC4NK5Rl0Nb2i03+8i86gKB+MLmqyLiv7v3iXW3HIldtcZQ=',
            'encSecKey':'92c2065af2d27643e78d66f261a4a189451c90f82a5bdd3abab938d9fbd1e30164a41d90cb51e544f5b72e5db7d94f4198d4083d822c36fbb09f1d941ca1a8f6b6a6441e8112064341c9399c644d493aaa1be644f3411f1d5682ede720bb7a17dfb1d7f38219d3826ef35bbebfb7410a1d61d4a76a5df112bc87b7a2a54f2f1f'}
    postdata = urllib.parse.urlencode(data).encode('utf8')   #不知道编什么码
    request = urllib.request.Request(url, headers=header, data=postdata)
    reponse = urllib.request.urlopen(request).read().decode('utf8')
    json_dict = json.loads(reponse)  #获取json
    
    song_id = []
    song_name = []
    for item in json_dict['playlist']['tracks']:
        song_id = song_id + [str(item['id'])]
        song_name = song_name + [str(item['name'])]
    return song_name, song_id

def get_hotComments(song_name, song_id):
    url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_' + song_id + '?csrf_token=6f5ba69387e105d69a27bf54b22e80a2'
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
    fhandle = open('./my_song_comments', 'a')
    fhandle.write(song_name + ':' + '\n')
    
    for i in hot_commit:
        num += 1
        fhandle.write(str(num) + '.' + i['content'] + '\n')
    
    fhandle.write('\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n\n')
    fhandle.close()
    


#测试
song_name, song_id = get_Song()
    
num = 0
while num < len(song_name):
    print('正在抓取第{}首歌的热评...'.format(num + 1))
    get_hotComments(song_name[num], song_id[num])
    print('φ(0￣*)啦啦啦_φ(*￣0￣)′')
    num += 1
    







