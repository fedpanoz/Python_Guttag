print("Please think of a number between 0 and 100!")
low = 0
high = 100
half = 50
diff = (high + low) // 2
ans = ""
while ans != "c":
    ans = input("Is your secret number " + str(half) + "?")
    print("Enter 'h' to indicate the guess is too high." + " Enter 'l' to indicate the guess is too low." +
          " Enter 'c' to indicate I guessed correctly.")
    if ans == "l":
        low = half
        half = (high + low) // 2

    elif ans == "h":
        high = half
        half = (high + low) // 2

    elif ans == "c":
        print("Game over.Your secret number was: ", half)
    else:
        print("Sorry, I did not understand your input.")