import random

# Ask user if they have played before
def yes_no(question):
    valid = False

    while not valid:

        response = input(question).lower()

        if response == "yes" or response == "y": 
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please answer yes/no")


    response = input (question).lower()
def choice_checker(question, error): 


    valid = False
    while not valid:

        # check for exit code... 
        print()

def instructions():
    print()
    print("You will be shown the height, base and width of a shape")
    print("The shapes you will get is (Square, Triangle and rectangle)")
    print("Your goal will be to find the area of that shape")
    print()
    print("The formula to finding areas of a rectangle is  (length x width).")
    print()
    print("The formula to for a triangle is (base x height / 2)")
    print()
    print("The formula to find the area of a square is (side x side)^2 ")
    print()
    print("You may also use a Calculator if needed")
    print()

# Show instructions
print("*** Welcome to Math quiz *** ")
print()
played_before = yes_no("Have you played the game before?")

if played_before == "no":
    instructions () 
# Function used to check input is valid


def check_rounds():
    while True:
        response = input("How many questions would you like: ")

        round_error = "please type either <enter> or an integer that is more than 0"

        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


# Main routine goes here...

rounds_played = 0


# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

if rounds == "":
    mode = "infinite"
    rounds = 10

end_game = "no"
while end_game == "no":

    # Rounds Heading
    print()
    if rounds == "infinite":
        heading = "continues Mode: Question {}".format(rounds_played + 1)
        print(heading)
        choose = input("{} or 'xxx' to end: ".format)
        if choose == "xxx":
            break

    else:
        heading = "Question {} of {}".format(rounds_played + 1, rounds)
        print(heading)
        if rounds_played == rounds + 1:
            end_game = "yes"
# Ask user for choice and check it's vaild 


    # rest of loop / game

    rounds_played += 1

# Genarate questions 

question = input("A rectangle with a side of 4cm and a side of 3cm has an area of ___ cm squared")
if question == "12":
    print("CORRECT ")
else: 
    question = "{}".format
    print("INCORRECT!  the correct answer is 12")

question = input("A triangle has a base of 3 and a height of 6.  The area is ___ cm squared.")
if question == "9":
    print("CORRECT!")
else:
    question = "{}".format
    print("INCORRECT! the correct answer is 9")

question = input("A Square has sides of 5. The area is ___ cm squared")
if question == "25":
    print("CORRECT!")
else:
    question = "{}".format
    print("INCORRECT! the correct answer is 25")
      






    print("Thank you for doing the Quiz")
