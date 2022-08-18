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

        # Ask user for choice (and put choice in lowercase) 
        response = input(question).lower()

        
# Number checking function goes here    
def int_check(question, low=None, high=None, exit_code ="xxx"):

    while True:

        # sets up error messages
        if low is not None and high is not None:
            error = "Please enter an number between {} and {} (inclusive)".format(low, high)
        elif low is not None and high is None:
            error = "Please enter an number that is more than or equal to {}".format(low)
        elif low is None and high is not None:
            error = "Please enter an number that is less than or equal to {}".format(high)
        else:
            error = "Please enter an number"
        try:
            response = input(question)
            
            # check to see if response is the exit code and return it
            if response == exit_code:
                return response
            
            # change the response int_checko an int_checkeger
            else:
                response = int(response)

            # Checks response is not too low, not use of 'is not' keywords
            if low is not None and response < low:
                print(error)
                continue

            # Checks response is not too high
            if high is not None and response > high:
                print(error)
                continue

            return response

        # checks input is a int_checkeger
        except ValueError:
            print(error)
            continue


mode = "regular"

questions_played = 0


# Lists of vaild responses
yes_no_list = ["yes", "no"]

# instructions
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
played_before = yes_no("Have you played the quiz before?")

if played_before == "no":
    instructions () 

def check_questions():
    while True: 
        response = input ("How many questions would you like: ")

        question_error = "please type a number that is more than 0"

        try:
            response = int(response)

            if response < 1:
                print(question_error)
                continue 

        except ValueError:
            print(question_error)
            continue 

        return response


# Main routine goes here...

questions_played = 0 
choose_instruction = "please press enter to begin"

# Ask user for # of questions, <enter> for infinite mode
questions = check_questions ()

end_game="no"
while end_game == "no":


    # questions Heading
    print()
    if mode =="":
        heading = "continues Mode: question {}".format(questions_played + 1,)
        questions += 1
        print(heading)

    else:
        heading = "question {} of {}".format(questions_played + 1, questions)
        print(heading)
    
    if questions_played == questions - 1:
        end_game = "yes"

    questions_played += 1

# genarate questions 
    all_shapes = ["square","rectangle","triangle", "xxx"]
    shape = random.choice(all_shapes[:-1])

    if shape == "rectangle":

            number = random.randint(1, 20)
            number_2 = random.randint(1,10)
            answer = number * number_2
        
            question = int_check("What is the area of a rectangle with a width of {} and a length of {} ".format(number, number_2, exit_code="xxx"))
        

    if shape == "square":    

            # generate a single number
            number = random.randint(1, 10)
            answer = number * number
            
            question= int_check("What is the area of a square if the length is {}  ".format(number, exit_code="xxx"))

    if shape == "triangle":

                number = random.randint(1, 10)
                number_2 = random.randint(1,10)
                num_3 = random.randint(1, 5)
                answer = number * number_2 / 2 
                
                question = int_check("What is the area of a triangle if the base is {} and the height is {}  ".format(number, number_2, exit_code="xxx"))

    if question =="xxx":
             break

        # print answer 
    if question == int(answer):
        print("CORRECT!")

    else:
        question = "{}".format
        print("Incorrect!")
        print ("answer", int(answer))
    

print()
print ("***Thanks for playing the quiz***")