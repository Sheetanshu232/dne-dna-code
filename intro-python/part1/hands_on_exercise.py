"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
print(pi)

# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
if i < 50:
    print("i is less than 50 ," + str(i))
else:
    print("i is greater than or equal to 50 ,"+  str(i))

# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])
if picked_fruit == 'orange':
    print("The colour of " + picked_fruit + "is orange")
elif picked_fruit == 'strawberry':
    print("The colour of " + picked_fruit + "is pink")
else:
    print("The colour of " + picked_fruit + "is yellow")

# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.
def product(num1,num2):
    return num1*num2


# TODO: Now call the function a few times to calculate the following answers

print("12 x 96 =", product(2,3))

print("48 x 17 =",product(48,17))

print("196523 x 87323 =",product(196523,87323))
