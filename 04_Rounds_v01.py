# set balance for testing purpose
balance = 5

rounds_played = 0

play_again = input("Press <Enter> to play...")
while play_again == "":

    # increase # of rounds played
    rounds_played += 1

    # print round number
    print (rounds_played)
    balance -= 1
    print("Balance: ", balance)
    print()

    play_again = input("Press Enter to Play again or 'xxx' to quit")
    