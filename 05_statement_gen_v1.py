
def statement_generator(statement, decoration):
    
    sides = "*" * 3

    greeting = "{} {} {}".format(sides, statement, sides)

    top_bottom = "*" * len(greeting)

    print(top_bottom)
    print(greeting)
    print(top_bottom)

    return ""


# Main routine goes here:
statement_generator("welcome to the Lucky Uncorn Game", "*")
print()
statement_generator("Congratulations you got a Unicorn!", "!")