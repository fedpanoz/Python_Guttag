def gcdIter(a, b):
    
    
    if a > b:
      ans = b
    else:
      ans = a
    while ans > 1:
        if b%ans == 0 and a%ans ==0:
          break
        ans -= 1
    return ans

print(gcdIter(9, 12))