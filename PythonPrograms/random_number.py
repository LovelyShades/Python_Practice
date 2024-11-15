import random

while True:
    top_of_range = input("\nPlease type a number larger than 0\n")

    if top_of_range.isdigit():
        top_of_range = int(top_of_range)
    
        if top_of_range <= 0:
            print("\nPlease try again\n")
            continue
        else:
            break
    else:
        print("\nPlease try again\n")
        continue
    
random_number = random.randint(0, top_of_range)

numberOfGuess = 0

while True:
    user_guess = input("\nMake a guess from 0 - " + str(top_of_range) + ": \n")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("\nPlease type a number\n")
        continue
       
    if user_guess == random_number:
        print("\nYou got it!\n")
        print("That took you " + str(numberOfGuess) + " tries!")
        break

    else:
        print("\nYou got it wrong, try again")
        numberOfGuess += 1
        continue
        