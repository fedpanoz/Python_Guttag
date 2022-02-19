# Test if a number is prime and if not gives the max divisor
x = int(input('Give me an integer: \n'))
test = None
div = 2
while (div < x):
    if x % div == 0:
        print(f"{x} is not prime")
        test = False
        break
    else:
        div += 1
        test = True
if test:
    print(f"{x} is prime\n")


