import random
def num_check(question):
    while True:
        response = input(question)

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

num_round = num_check("How many questions?: ")



all_shapes = ["square", "rectangle", "triangle"]


for shape in all_shapes:

    if shape == "rectangle":

        number = random.randint(1, 20)
        number_2 = random.randint(1,10)

        answer = number * number_2

        # replace with number checker in due course
        question = int(input("What is the area of a rectangle with a width of {} and a length of {} ".format(number, number_2)))
    



    if shape == "square":
        

        # generate a single number
        number = random.randint(1, 10)

        answer = number * number

        question= int(input("What is the area of a square if the length is {}  ".format(number)))
    if shape == "triangle":

        for shape in all_shapes:





            if shape == "triangle":

             number = random.randint(1, 10)
             number_2 = random.randint(1,10)
             num_3 = random.randint(1, 5)
             answer = number * number_2 / 2 

             question = int(input("What is the area of a triangle if the base is {} and the height is {}   ".format(number, number_2)))


        # print answer 
    if question == int(answer):
        print("CORRECT!")

    else:
        question = "{}".format
        print("Incorrect!")

        print("answer", int(answer))
