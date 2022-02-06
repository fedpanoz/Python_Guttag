# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 14:30:26 2022

@author: Fedex

"""

s = input("Gimme a sequence of character to work with: \n")

c = s[0]
b = s[0]
n = 0
while n != len(s) -1:
    if s[n] <= s[n+1]:
        n+= 1
        c += s[n:n+1]
        if len(c) > len(b):
            b = c
    else:
        n += 1
        c = s[n]   
print("Longest substring in alphabetical order is: "  + b)