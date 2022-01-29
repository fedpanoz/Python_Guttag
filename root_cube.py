# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 06:35:39 2022

@author: Fedex
"""
x = int(input('Gimme an int to cube:\n'))
tempo = 0
while tempo ** 3 < abs(x):
    tempo += 1
    
if (tempo ** 3) != abs(x):
    print(f'{x} has no perfect cubes')
elif x > 0:
    print(f'The cube root of {x} is {tempo}')
else:
    print(f'The cube of {x} is {-tempo}')
    