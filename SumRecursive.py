def prova(a, b):
    if b == 1:
        return a
    else:
        return a + prova(a, b - 1)


print(prova(6, 5))
