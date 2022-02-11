num_to_sqaure_root = float(input('Gimme a number to square root, please: \n'))
precision = 0.01
guess = num_to_sqaure_root / 2
num_guesses = 0
while abs(guess ** 2 - num_to_sqaure_root) >= precision:
    num_guesses += 1
    guess = guess - ((guess ** 2) - num_to_sqaure_root) / (2 * guess)
print("The guess is : " + str(guess) + " num of guesses is : " + str(num_guesses))