num = int(input("Gimme an integer please: \n"))
if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
result = ""
if num == 0:
    result = '0'
while num > 0:
    result = str(num % 2) + result
    num //= 2
    print(result)
