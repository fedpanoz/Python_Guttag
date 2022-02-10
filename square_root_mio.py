# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 14:38:23 2022

@author: zizza
"""

x = int(input("Gimme the the square of which i 've to find the root:\n"))
num_guesses = 0
high = x
low = 1.0
precision = 0.00001
ans = (high + low) / 2.0
while abs((ans ** 2) - x) >= precision:
    if (ans ** 2) > x:
        high = ans
    else:
        low = ans
    num_guesses += 1    
    ans = (high + low) / 2
    print(f'{ans} , {num_guesses}')
        
