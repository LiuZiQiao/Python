##a, b = 0,1
##while b<10:
##    print(b)
##    a,b = b,a+b
##def area(width,height):
##    return width*height
##
##def print_welcome(name):
##    print("welcome",name)
##
##
##    print_welcome("1223")
##    w = 4
##    h = 5
##    print("width=",w,"height=",h,"area=",area(w,h))


#import urllib2

from urllib.request import urlopen 
response = urlopen('http://www.baidu.com')

##print response.getcode()

cont = response.read()
print(cont)
