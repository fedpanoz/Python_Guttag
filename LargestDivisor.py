x = int(input("Gimme an integer lease: \n"))
smallest_divisor = None
largest_divisor = None
for guess in range(2, x):
    if x % guess == 0:
        smallest_divisor = guess
        break
if smallest_divisor != None:
    largest_divisor = x // smallest_divisor
    print(f"Largest divisor of x is {largest_divisor}")
else:
    print(f"{x} , is prime")
