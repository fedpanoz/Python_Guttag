# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 05:48:05 2022

@author: Fedex
"""

x = int(input('Gimme th enumber to square:\n'))
itersLeft = x
squaring = 0
while itersLeft != 0:
    squaring += x
    itersLeft -= 1
print(f'The sqaure of {x} is : {squaring} \n')