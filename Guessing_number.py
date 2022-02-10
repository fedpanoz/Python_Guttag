print("Please think of a number between 0 and 100!")
low = 0
high = 100
half = 50
diff = (high + low) / 2
ans = ""
while ans != "c":
    ans = input(f"Is your secret number {half}?\nEnter 'l' to indicate the guess is too low."
                f"Enter 'c' to indicate I guessed correctly.")
    if ans == "h":
        low = half
        half = (high + low) // 2

    elif ans == "l":
        high = half
        half = (high + low) // 2

    elif ans == "c":
        print(f"Game over.Your secret number was: {ans}")
    else:
        print("Sorry, I did not understand your input.")
