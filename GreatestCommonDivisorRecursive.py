def gcd(a, b):
    smallest = min(a, b)
    largest = max(a, b)
    if smallest == 0:
        return largest
    else:
        return gcd(smallest, largest % smallest)


print(gcd(9, 12))

