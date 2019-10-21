#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'xiaokun·liu'

"""
注释写法3
"""
# 注释1
print('...')  # 注释2

# tuple
l1 = (1,2,3,4)
print(type(l1))
# list
l2 = [1,2,3,4]
l2.sort()
print(l2)
print(type(l2))

# set
l3 = {1,2,3,4}
s = set([1,2,3,4])
print(type(l3))
print(type(s))
# dict
d = {'name':'tom','age':18}
print(d)
print(type(d))


for i in s:
    print(i)

if True:
    print("main")