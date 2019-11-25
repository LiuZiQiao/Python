import requests
from lxml import etree

def get__html(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
    try:
        html = requests.get(url,headers=headers)
        html.encoding = html.apparent_encoding
        if html.status_code == 200:
            print('成功获取网页')
            print(html.text)
    except Exception as e:
        print('获取网页失败:%s'% e)
    return  html.text

def parse_html(html):
    # html = etree.HTML(html)
    pass

if __name__     == '__main__':
    url = 'https://movie.douban.com/top250'
    html = get__html(url)
    # moves = parse_html(html)