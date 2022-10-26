# Python has the least performance but is easy to understand
# Python is an interpretted language


# Turtle demo 1
import turtle

for i in range(0, 10):
  turtle.forward(100)
  turtle.left(90)
  turtle.forward(100)


# Turtle demo 2
import turtle
import random

for i in range(0, 10):
  turtle.forward(100)
  # turtle.left(90)
  turtle.left(random.randint(15, 90))
  turtle.forward(100)

# Turtle demo 3
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()



# Functions
# - think of them as a small mini program
# - to define a function, use def keyword followed by nam of function
# - parentheses are there to demonstrate that it is a function; arguments go inside the parentheses
# - need to be called to be ran
# - calling a function is synonymous with "invoking a function", "executing a function", "running a function", etc
# - can be called as many times as you want; any time it is called, it goes back to the function and runs the code
# - every function MUST have a unique name and cannot be redefined
def my_first_function ():
    print("hello")

my_first_function()
my_first_function()

# - functions can be called using a for loop
for i in range(0, 10):
    my_first_function()

# - pass keyword means do nothing
def trivial_useless_function():
    pass

trivial_useless_function()


# what goes inside parentheses are arguments (think of them as a variable that hasn't been defined yet)
# give arguments whatever name you want
# parameters are the defined value of an argument
def draw_box_1():
    print("******")
    print("*    *")
    print("******")
draw_box_1()

def draw_box_2(length):
    print(f'I am about to draw a box of length: {length}')
draw_box_2(4) # 4 is the parameter that is passed into the function

def draw_box_3(length):
    for col in range(1, length + 1): 
        #  same as: for col in range(0, length)
        print("*", end = "")
draw_box_3(3)

def draw_box_4(length):
    print("*" * length)
    print("*" * length)
draw_box_4(4)

def draw_box_5(length):
    print('*' * length)
    for i in range(0, length - 2):
        print('*   *')
    print('*' * length)
draw_box_5(5)

#  works on any length less than 2 to make an actual rectangle
def draw_box_6(length):
    print('*' * length)
    for i in range(0, length - 2):
        print('*' + ' ' * (length - 2) + '*')
    print('*' * length)
draw_box_6(6)
draw_box_6(20)
draw_box_6(2) # edge case of 2

# return keyword exits out of a function (pass does nothing)
# return is NOT the same as print
def draw_box_7(length):
    if length <= 1:
        return
    print('*' * length)
    for i in range(0, length - 2):
        print('*' + ' ' * (length - 2) + '*')
    print('*' * length)
draw_box_7(2)


def add_two_nums(a, b):
    sum = a + b
    return sum # return a + b does not work, MUST assign something as a variable and pass to return command
sum_1 = add_two_nums(2, 3) # to see value of function, assign to a variable and pass into print
print(sum_1) # --> prints 5
# print(add_two_nums(2,3)) also works


def get_average(a, b, c):
    result = (a + b + c)/3
    return result
print(get_average(3, 4, 5)) # --> prints 4.0
print(get_average(17, 19, 91)) # --> prints 42.333...6

def get_max(a, b):
    max_num = max(a, b)
    return max_num
print(get_max(99, 10)) # --> prints 99