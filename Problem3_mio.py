# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 05:38:35 2022

@author: zizza
"""

s = 'azcbobobegghakl'
c = s[0]
b = s[0]
n = 0

while n != len(s) - 1:
    if s[n] <= s[n + 1]:
        n += 1
        c += s[n:n + 1]

        if len(c) > len(b):
            b = c
    else:
        n += 1
        c = s[n]

print(b)