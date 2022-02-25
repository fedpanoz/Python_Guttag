def isIn(char, aStr):
    middle = len(aStr) // 2
    if char == aStr[middle]:
        return True
    elif char < aStr[middle]:
        return isIn(char, aStr[0:middle])
    else:
        return isIn(char, aStr[middle:-1])
    
    
print(isIn("t", "adfijkmnooty"))
    
            