# Review for test
# Chapter 1
# - interpreter (i.e. Python) vs compilier
# - interpreters don't run as fast as compilier langauges



# Chapter 2
# algorithm definition



# Chapter 3
# Data output
# print function
# \ --> escape character
# \n --> new line
# \t --> tab
# \r --> carriage return
print('\\')  # --> prints out one \



# Chapter 4
# - Boolean expressions are either always True or False
# - cannot assign a value to a value but can assign a value to a variable
    # i.e. this would not work: 10 = 10
    # but this works: apples = 10

# - comparitive operators work with strings
# - compares ascii code of strings
# in Terminal: 
'a' == 'a'  # --> prints True
'a' > 'a'  # --> prints False
'z' > 'a'  # --> prints True because z comes later on in the alphabet

# Logical Operators
# - and, or, not

# Short Circuit Evaluation
x = 10
y = 500
if x > 15 and y < 100:
    print('True')
else:
    print('False')
# --> prints False beacuse the first condition is not matched so it will not bother to evaluate the second part since it is an `and` expression

# For and while loops
# look in loops.txt


# the loop below is infinite but gets interrupted with a break statement
counter = 0
while True:
    counter += 1
    print(counter)
    if counter > 10:
        break
"""
prints:
1 2 3 4 5 6 7 8 9 10 11
"""

# Sentinel
# - "marker variables"/"flag variables" that holds the state

# Nested loops
# - loop inside a loop

# `break` keyword
for i in range(1, 10):
    print('hello', i)
    if i > 5:
        break
    print('moving to the next number...')

"""
prints:
hello 1
moving to the next number...
hello 2
moving to the next number...
hello 3
moving to the next number...
hello 4
moving to the next number...
hello 5
moving to the next number...
"""


# `continue` keyword
for i in range(1, 10):
    print('hello', i)
    if i > 5:
        continue
    print('moving to the next number...')

"""
prints:
hello 1
moving to the next number...
hello 2
moving to the next number...
hello 3
moving to the next number...
hello 4
moving to the next number...
hello 5
moving to the next number...
hello 6
hello 7
hello 8
hello 9
"""


# Problem to attempt: is it possible to create an infinite loop using a for loop