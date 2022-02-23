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


#  **** Main Routine *****

print("Welcome to the LU game")
print()

show_instructions = yes_no("Have you played the game before? ")
if show_instructions == "no":
    print()
    # replace with call to display instructions function
    print("display instructions")
    print()

# ask how much money....
how_much = num_check("How much would you like to play with? ", 0 , 10)

print()

print("You will be spending ${}".format(how_much))