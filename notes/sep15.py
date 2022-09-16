# this is a single line comment (equivalent to // in JavaScript)

"""
this
is
a
multiline/block
comment
(equivalent to /* */ in JavaScript)
"""


# Variable names are case-sensitive
world = 45.56
World = 17
WORLD = 7
wor1D = 78909
# all these variables have different values
print(world, World, WORLD, wor1D) # <-- prints 45.56 17 7 78909

# Variable names can NOT be named after built-in values
True = 45.56 # <-- this does NOT work
True_ = 45.56 # <-- this is okay
# another example is print = 10 (even though it works, it is BAD PRACTICE)

# Variable names can NOT start with numbers
list_of_50_states = "NY, NJ, CA..." # <-- valid variable name
50states = "NY, NJ, CA..." # <-- INVALID variable name (because it starts with a number)


# to get the type of a variable, put variable in type function
print(type(list_of_50_states)) # prints <class 'str'>

# values of variables can be redeclared (meaning that variables can be reused and the old value of variable is overwritten with the new value)
list_of_50_states = 75.56
print(type(list_of_50_states)) # prints <class 'int'>

list_of_50_states = True
print(type(list_of_50_states)) # prints <class 'bool'>


# it is also possible to get types of different values
print(type(10)) # <-- prints <class 'int'>
print(type('Hello')) # <-- prints <class 'str'>
print(type(False)) # <-- prints <class 'bool'>


# Converting 71F to C
F = 71
C = (F - 32) * (5 / 9)
print(C) # <-- prints 21.666...

# Coverting F to C based off user input
F = input("Enter temp in F: ") # NOTE: input has to be entered as a string for this to work OR you can include the next line
F = int(F)
# OR can combine the two lines together as F = int(input("Enter temp in F: "))
C = (F - 32) * (5 / 9)
print(C)

# Input function allows input to based off user input
name = input("Enter your name: ")
print('Hello', name, 'how are you?')
# Terminal asks user to enter a name
# when Enter is put, the value of name is put into print

# Instead of asking for user's input, we can hard code the value by declaring the variable
name = "Jane"
print("Hello", name, "how are you?")


# Type conversion: float to integer
X = int(78.87) # 78.87 is a float but if it is passed into int(), it converts it from a float to an integer
print(X) # <-- prints out 78; it basically chops off the decimal



# Type conversion: string to float
X = float("85.5") # "85.5" is a string but it is passed into float(), it converts it from a string to a float; it works because there is nothing else in the string
print(X) # <-- prints out 85.5

X = float("-1.5") # -1.5 is a valid float even though it is negative
print(X) # <-- prints out -1.5

X = float("85.5f")
print(X) # <-- will print out an error saying "could not convert string to float"


# Type conversion: float to string
S = str(1000.5) # take this input and convert it into a string and store it as a variable S
print(S) # <-- prints "1000.5"
# to get the type of S, do:
print(type(S)) # <-- prints <class 'str'>


# single assignments
a = 1
b = 2
c = 3
d = 4
print(a, b, c, d) # <-- prints 1 2 3 4

# multiple assignments (same as above, just less lines)
a, b, c, d = 1, 2, 3, 4
print(a, b, c, d) # <-- prints 1 2 3 4


# math in python works as expected
x = 10 + 5
x = 10 - 5
x = 10 * 5
x = 10 / 3
print(x) # <-- prints out 3.33... because it is the last read line

x = 10 // 3
print(x) # <-- prints out 3 because it is the integer

# exponents in python use ** instead of ^
x = 3 ** 3
print(x) # <-- prints 27

# modulus operator (%) prints out the remainder of a division operation
x = 15 % 4
print(x) # <-- prints 3

# Python follows PEMDAS
x = 7 + 6 * 3 - 2 % 5
print(x) # <-- prints 23

# easier to rewrite expression with parentheses to coerce which operations take place first; this can change the result
x = ((7 + 6) * (3 - 2)) % 5
print(x) # <-- prints 4.9