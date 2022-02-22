def iterPower(base, exp):
    sol = 1
    for x in range(1, exp + 1):
        sol = sol * base
    return sol
    
    
    
print(iterPower(2, 5))