# Functions go here...
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()


        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer yes / no")


#  **** Main Routine *****

print("Welcome to the LU game")
print()

show_instructions = yes_no("Have you played the game before? ")
if show_instructions == "no":
    # replace with call to display instructions function
    print("display instructions")
    print()

# ask how much noney....

