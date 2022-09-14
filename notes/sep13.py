# first part of class: went over ../homework/unofficial-hw-2.py questions and drew flowcharts for them

# python.org for all python information and documentation 
# python.org/shel to run brief python code on web

# python has a notion of row values and theyare called literals
10 
# any numeric value that isnt a decimal or fracrion is an integer (int) literal

10.5
# is a float (float) literal and means it can contain fractions

"hello"
# is a string (str) literal
# rule is that if you start with a double quote, you have to end with a double quote and vice versa for single quotes

# literals can be contained in a memory container called a variable
number_of_apples = 10
# variables use snake case, meaning that all letters are lowercase and each word is connected wirh an underscore
# this variable is holding an integer value (int) 10

# camel case (commonly used in JavaScript): 
numberOfApples = 10

# pascal case (commonly used in C): 
NumberOfApples = 10

# number_of_apples, numberOfApples, and NumberOfApples are three different variables

# to print variable, pass variable name into print function
print(number_of_apples)

# to print variable with a statement, pass in quote with comma and variable
print("We have", number_of_apples, "apples available")

# to print out quotataion marks, mix quotes
print("'hello world'") # --> prints 'hello world'
print('"HELLO WORLD"') # --> prints "HELLO WORLD"

# python can handle math with print statement 
number_of_oranges = 34
print(number_of_apple + number_of_apples) # --> prints 44

x = 27
y = 50
print( ((x + y) * x) / y) # --> prints out whatever this is equal to

w = ((x + y) * x) / y * 10.5 + 23.89
print("w:", w) # --> prints out "w: ___" (___ is whatever w is equal to, im just to lazy to igure it out lol)

# modulus also works with print
print(17 % 5) # --> prints 2


# string concatenation 
country_a = "USA"
country_b = "Canada"
result = country_a + country_b # will throw an error if you use a minus sufn
print(result) # --> prints "USACanada"
