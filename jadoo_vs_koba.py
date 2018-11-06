#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 12:51:34 2018

@author: monica

HackerEarth Practice - Jadoo vs Koba
Jadoo, the space alien has challenged Koba to a friendly duel. 
He asks Koba to write a program to print out all numbers from 70 to 80. 
Knowing perfectly well how easy the problem is, the Jadoo adds his own twist 
to the challenge. He asks Koba to write the program without using a single 
number in his program and also restricts the character limit to 100.

"""

def __main__():
    n1 = int("70")
    n2 = int("80")
    print(n1, n2)
    
    i = n1
    while (i <= n2):
        print(i)
        i = i + int("1")

__main__()