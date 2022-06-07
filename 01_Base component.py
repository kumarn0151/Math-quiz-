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
print("*** Welcome to Math quiz game *** ")
print()
played_before = yes_no("Have you played the game before?")

if played_before == "no":
    instructions()


def check_rounds():
    while True: 
        response = input ("How mnay Questions would you like?")

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
choose_instruction = "please choose a Shape out of these options (square, rectangle and triangle)"

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds ()

end_game="no"
while end_game == "no":

    # start of Game play loop 

    # Round Heading 
    print()
    if rounds == "": 
        heading = "continues Mode: Round {}".format(rounds_played + 1)
    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)
        print(heading)

    print(heading) 
    choose = input("{} or 'xxx' to end: ".format(choose_instruction))

    # End game if exit code is typed 
    if choose == "xxx":
        break 
 