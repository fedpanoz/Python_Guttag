# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 13:53:16 2022

@author: Fedex
"""

count = 0
s = 'yvobobbncobobboobdbqzbozombobobobobob'


for i in range(len(s)):
    if s[i: (i + 3)] == 'bob':
        count += 1
print("Number of times bob occurs is: " + str(count))
