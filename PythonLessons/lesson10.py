def parent_function(person):
    coins = 3

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n " + person + " has " + str(coins)+ " coins left.\n")
        elif coins == 1:
            print("\n " + person + " has " + str(coins)+ " coin left.\n")
        else:
            print("\n " + person + " is out of coins\n")

    return play_game
    
tommy = parent_function("Tommy")
jenny = parent_function("Jenny")

tommy()
tommy()

jenny()