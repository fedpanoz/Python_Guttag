def summa(a):
    
    if a == 1:
        return a
    else:
        return a + summa(a - 1)
    
print(summa(6))
