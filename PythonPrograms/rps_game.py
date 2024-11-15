import random

# Initialize win counts
playerWinCount = 0
computerWinCount = 0
playagain = True

while playagain:

    # Player's choice
    playerchoice = input("\nChoose a number: \n1: Rock\n2: Paper\n3: Scissors\n\n")

    if playerchoice == '1':
        playerchoice = 'Rock'
    elif playerchoice == '2':
        playerchoice = 'Paper'
    elif playerchoice == '3':
        playerchoice = 'Scissors'
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        continue

    # Computer's choice
    computerchoice = random.choice(['1', '2', '3'])

    if computerchoice == '1':
        computerchoice = 'Rock'
    elif computerchoice == '2':
        computerchoice = 'Paper'
    else:
        computerchoice = 'Scissors'

    # Display choices to player
    print("\nYou chose: " + playerchoice)
    print("Computer chose: " + computerchoice + "\n")

    # Determine winner
    if playerchoice == 'Rock' and computerchoice == 'Scissors':
        print("You win")
        playerWinCount += 1
    elif playerchoice == 'Paper' and computerchoice == 'Rock':
        print("You win")
        playerWinCount += 1
    elif playerchoice == 'Scissors' and computerchoice == 'Paper':
        print("You win")
        playerWinCount += 1
    elif playerchoice == computerchoice:
        print("It's a tie")
    else:
        print("Computer wins!")
        computerWinCount += 1

    # Display win counts
    print("\nYour win count: " + str(playerWinCount))
    print("Computer win count: " + str(computerWinCount))

    # Ask to play again
    playagain_input = input("\nPlay again?\nY for Yes or \nQ to quit\n\n")

    # Determine if player wants to keep playing
    if playagain_input.lower() == 'q':
        print("\nThanks for playing!❤️")
        playagain = False
    elif playagain_input.lower() != 'y':
        print("\nInvalid input. Please enter Y or Q next time.")
        playagain = False
