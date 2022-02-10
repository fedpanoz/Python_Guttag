# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 21:40:16 2022

@author: zizza
"""

print("Think of a number between 0 and 100")
low = 0
high = 100
guess = 0
number_guess = 0
half = 50
diff = (high - low) / 2
ans = ""
move = 0
while ans != "c":
    ans = input(f"Is your number {half} ?\nEnter 'h' or 'l' or 'c'")
    if ans == "h":
        low = half
        half = (high - low) / 2
        move += 1
    elif ans == "l":
        high = half
        diff = (high - low) / 2
        move += 1
        
print(move)