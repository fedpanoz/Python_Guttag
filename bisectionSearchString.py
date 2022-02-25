def isIn(char, aStr):
    middle = len(aStr) // 2
    if aStr == "":
        return False
    elif len(aStr) == 1 and char != aStr:
        return False
    elif char == aStr[middle]:
        return True
    elif char < aStr[middle]:
        return isIn(char, aStr[:middle])
    else:
        return isIn(char, aStr[middle:])


print(isIn("x", "ghikmy"))

