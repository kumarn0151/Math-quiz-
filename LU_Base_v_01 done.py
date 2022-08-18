import random
from select import select

# Functions go here...

# checks for yes / no response
def yes_no(question):

    valid = False 

    while not valid:

        response = input (question).lower()

        if response == "yes" or response =="y":
            return "yes" 
        elif response == "no" or response =="n":
            return "no" 
        else:     
            print("please answer yes/ no ")


# Show instructions
def instructions():
    print()
    print("Instructions go here")
    print()
    print("select a amount between 1 and 10 and press enter to play if you get A UNICORN you basically win")
    return ""


# checks for numbers between low and high
def num_check(question, low, high):
    error = "please enter an whole number betwwen 1 and 10\n"

    valid = False
    while not valid:
        try:

            # ask the qustion
            response = int (input(question) )
            # if the amount is too low / too high give
            if low < response <= high:
                return response

            # output an error
            else:
                print (error)

        except ValueError:
            print(error)

            # Main Routine goes here...


# decorates statements with symbols above and below
def statement_generator (statement, decoration, style):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    if style == 3:

        print(top_bottom)
        print(statement)
        print(top_bottom)

    else:
        print(statement)

    return ""

# ****** Main  Routine Starts here *******

statement_generator("Welcome to the Lucky Unicorn Game", '-', 3)
print()

played_before = yes_no("have you played the game before? ")

if played_before == "no":
    instructions()

print()

# Ask user how much thye want to play with...
how_much = num_check ("How much would you like to play with? ", 0, 10)

print ("you will be spending ${}".format(how_much))

balance = how_much

rounds_played =0

play_again = input("press <Enter> to play..."). lower()
while play_again == "":

    # increase # of rounds played
    rounds_played += 1

    # print round number
    print()
    rounds_heading = "*** Round #{} ***".format(rounds_played)
    statement_generator(rounds_heading, "-", 1)

    chosen_num = random.randint(1, 100)

    # Adjust balance
    # if the random # is between 1 and 5,
    # user gets a unicorn (add $4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4

        # if the random # is between 1 and 5 ,
        # user gets a unicorn (add $ to balance)
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1
    # The token is either a horse or zebra...
    # in both cases, subtract $0.50 from the balance
    else:
        # if number is even, it's a horse
        if chosen_num % 2 == 0:
            chosen = "horse"

        # if number is odd, it's a zebra
        else:
            chosen = "zebra"
        balance -= 0.5

    feedback = "You got a {}.  Your balance is ${:.2f}".format(chosen, balance)
    print(feedback)

    if balance < 1:
        play_again = "xxx"

        print("***balance*** $0")

        print("sorry you have run out of money, Thanks for playing")
    else:
         play_again = input("Press Enter to play again "
                            "or 'xxx' to quit")

# Ask user how much they want to play with...

