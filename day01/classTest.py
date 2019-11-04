#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'xiaokun·liu'

class A():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('init A')

    def __str__(self):
        return f'{self.name}+{self.age}'

    def __del__(self):
        print('del A')


class B(A):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self):
        return f'{self.name}+{self.age}+{self.sex}'

    def BA(self):
        super(B,self).__init__(name=self.name,age=self.age)
        return super(B,self).__str__()

    def __del__(self):
        print("del B")

b = B('b',2,1)

print(b.BA())
print(b)