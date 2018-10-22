import urllib2

def geturl() :
    html = urllib.urlopen('https://www.bilibili.com/video/av18201121/').read()
    return html


print geturl()




