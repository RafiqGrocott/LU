import random

# Functions go here...
from tkinter import Y


def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()


        if response == "yes" or response == "y":
            print()
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
        
            print("Please answer yes / no")

def num_check(question, low, high):
    error = "Please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))
            # if the amount is too low / too high give
            if low < response <= high:
                return response

            # output an error
            else:
                print(error)

        except ValueError:
            print(error)

def statement_generator(statement, decoration, style):
    
    sides = decoration * 3

    greeting = "{} {} {}".format(sides, statement, sides)

    row = len(greeting) * decoration

    if style == 3:

        print(row)
        print(greeting)
        print(row)

    else:
        print(greeting)

    return ""


#  **** Main Routine *****

statement_generator("Welcome to the LU game", "-", 3)
print()

show_instructions = yes_no("Have you played the game before? ")
if show_instructions == "no":
    print()
    # replace with call to display instructions function
    print("display instructions")
    print()

# ask how much money....
how_much = num_check("How much would you like to play with? ", 0 , 10)

balance = how_much

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()
while play_again == "":

    # increase # of rounds played
    rounds_played += 1

    # print round number
    print()
    print ("*** ROUND #{} ***".format(rounds_played))

    chosen_num = random.randint(1,100)

    # Adjust balance
    # if the random # is between 1 and 5,
    # user gets a unicorn (add $4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        decoration = "-"
        balance +=4

    #if the random # is between 6 and 36
    #user gets donkey which subtracts $1 from balance
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        decoration = "D"
        balance -= 1

    # the token is either a horse or zebra...
    # which subtracts $0.50 from balance
    else:
        # if number = even, set the chosen item to horse
        if chosen_num % 2 == 0:
            chosen = "horse"
            decoration = "H"

        # otherwise set to zebra
        else:
            chosen = "zebra"
            decoration = "Z"
        balance -= 0.5
    
    # output outcome

    feedback ="You got a {}, your balance is ${:.2f}".format(chosen, balance)
    statement_generator(feedback, decoration, 1)
    
    if balance < 1:
        play_again = "xxx"
        print ("Sorry, you have run out of money :(")

    else:
        play_again = input("Press <Enter> to play again or 'xxx' to quit")

print()
print("Final Balance", balance)

print("You will be spending ${}".format(how_much))