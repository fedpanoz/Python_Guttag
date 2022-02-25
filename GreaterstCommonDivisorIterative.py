def gcdIter(a, b):
    if a > b:

        for x in range(b, 1, -1):
            if a % x == 0 and b % x == 0:
                break
        return x


    else:

        for x in range(a, 1, -1):
            if a % x == 0 and b % x == 0:
                break

        return x


print(gcdIter(6, 12))
