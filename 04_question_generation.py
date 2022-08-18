# set up list with shapes....
import random

all_shapes = ["square", "rectangle", "triangle"]

for shape in all_shapes:

    if shape == "square":
        pass

        # generate a single number
number = random.randint(1, 10)

answer = number * number

# generate the question
question= int(input("What is the area of a square if the length is {}  ".format(number)))

print(question)

#check if answer correct or wrong

if question == answer:
   print("CORRECT!")
                
else:
    question = "{}".format
    print("INCORRECT!")

# generate the answer
    print("answer", answer)