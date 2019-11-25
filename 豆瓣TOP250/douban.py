#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'xiaokun·liu'

import requests
from lxml import etree
import pandas as pd
import os

def get__html(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
    try:
        html = requests.get(url,headers=headers)
        html.encoding = html.apparent_encoding
        if html.status_code == 200:
            print('成功获取网页')
            # print(html.text)
    except Exception as e:
        print('获取网页失败:%s'% e)
    return  html.text


MOVIES = []
IMGURLS = []

def parse_html(html):
    html = etree.HTML(html)
    lis = html.xpath("//ol[@class='grid_view']/li")

    # print(lis)
    for li in lis:
        name = li.xpath(".//a/span[@class='title']/text()")[0]
        director_actor = li.xpath(".//div[@class='bd']/p/text()")[0].strip()
        info = li.xpath(".//div[@class='bd']/p/text()")[1].strip()
        rating_score = li.xpath(".//div[@class='star']/span[2]/text()")[0]
        rating_num = li.xpath(".//div[@class='star']/span[4]/text()")[0]
        introduce = li.xpath(".//p[@class='quote']/span/text()")
        # movie = {'name':name,'director_actor':director_actor,'info':info,'rating_score':rating_score,'rating_num':rating_num,'introduce':introduce}
        if introduce:
            movie = {'name': name, 'director_actor': director_actor, 'info': info, 'rating_score': rating_score,
                     'rating_num': rating_num, 'introduce': introduce[0]}
        else:
            movie = {'name': name, 'director_actor': director_actor, 'info': info, 'rating_score': rating_score,
                     'rating_num': rating_num, 'introduce': None}

        imgurl = li.xpath(".//img/@src")[0]
        MOVIES.append(movie)
        IMGURLS.append(imgurl)

    return MOVIES,IMGURLS


def downloadimg(url,movies):
    if 'movieposter' in os.listdir(r'F:\code\Python\豆瓣TOP250'):
        pass
    else:
        os.mkdir('movieposter')
    os.chdir('F:\code\Python\豆瓣TOP250\movieposter')
    img = requests.get(url).content

    with open(movies['name']+'.jpg','wb') as f:
        print(f'正在下载:%s',url)
        f.write(img)

if __name__     == '__main__':
    for i in range(10):
        url = 'https://movie.douban.com/top250?start=' + str(i * 25) + '&filter='
        html = get__html(url)
        movies = parse_html(html)[0]
        imgurls = parse_html(html)[1]

        MOVIES.extend(movies)
        IMGURLS.extend(imgurls)

    for i in range(250):
        downloadimg(IMGURLS[i],MOVIES[i])
        print(f'第{i}个')

    os.chdir(r'F:\code\Python\豆瓣TOP250')
    moviedata = pd.DataFrame(MOVIES)
    moviedata.to_csv('movies.csv')
    # print(moviedata)