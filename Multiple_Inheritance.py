#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 13:24:49 2018

@author: monica
"""

        
class Father:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def gardening(self):
        print("I enjoy gardening")
        
class Mother:
    def __init__(self, c, d):
        self.c = c
        self.d = d
        
    def cooking(self):
        print("I love cooking")
        
class Child(Father, Mother):
    def __init__(self, a, b, c, d, e, f):
        Father.__init__(self,a,b)
        Mother.__init__(self,c,d)
        self.e = e
        self.f = f
        
    def sport(self):
        print("I love playing cricket")
        
c1 = Child(1,2,3,4,5,6)        
print(c1.d)