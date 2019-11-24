#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'xiaokun·liu'

import requests
from lxml import etree
# import pandas as pd

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

def parse_html(html):
    html = etree.HTML(html)
    lis = html.xpath("//ol[@class='grid_view']/li")
    movies = []
    # print(lis)
    for li in lis:
        name = li.xpath(".//a/span[@class='title']/text()")[0]
        director_actor = li.xpath(".//div[@class='bd']/p/text()")[0].strip()
        info = li.xpath(".//div[@class='bd']/p/text()")[1].strip()
        rating_score = li.xpath(".//div[@class='star']/span[2]/text()")[0]
        rating_num = li.xpath(".//div[@class='star']/span[4]/text()")[0]
        introduce = li.xpath(".//p[@class='quote']/span/text()")[0]

        movie = {'name':name,'director_actor':director_actor,'info':info,'rating_score':rating_score,'rating_num':rating_num,'introduce':introduce}
        movies.append(movie)

    return movies

if __name__     == '__main__':
    url = 'https://movie.douban.com/top250'
    html = get__html(url)
    movies = parse_html(html)
    for m in movies:
        print(m)
    # moviedata =