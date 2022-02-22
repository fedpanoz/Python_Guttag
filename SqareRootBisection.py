x = int(input("Gimme an integer of which you want to find the square root:\n"))
epsilon = 0.01
num_guesses = 0
high = max(1, x)
low = 1
ans = (high + low) / 2
while abs(ans ** 2 - x) >= epsilon:
    print(f"low is {low}, high is {ans}")
    num_guesses += 1
    if ans ** 2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2
print(f"Number of guesses = {num_guesses}")
print(f"{ans}, is close to the square root of {x}")


