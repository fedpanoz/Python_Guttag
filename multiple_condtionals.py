# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 13:53:16 2022

@author: Fedex
"""
x = 1
while True:
    if x % 11 == 0 and x % 12 == 0 and x % 5 == 0 and x % 7 == 0:
        break
    x += 1
print(f'The number divisible by 11 and 12 is {x}')