# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 13:17:27 2022

@author: Fedex
"""

s = input("Gimme a string to count vowels: \n")
vowels_counted = 0
for letter in (s):
    if letter == 'a':
        vowels_counted += 1
    elif letter == 'e':
        vowels_counted += 1
    elif letter == 'i':
        vowels_counted += 1
    elif letter == 'o':
        vowels_counted += 1
    elif letter == 'u':
        vowels_counted += 1
print(f'Number of vowels: {vowels_counted}')