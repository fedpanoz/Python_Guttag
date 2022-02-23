def prova(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

print(prova(6,4))
