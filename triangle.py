import random

all_shapes = ["square", "rectangle", "triangle"]


for shape in all_shapes:

    if shape == "triangle":
        pass

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

    