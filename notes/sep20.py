# how to do complex math in Python:
import math # HAVE to import math library to use math function 

answer = 16 ** 0.5 # prints 4
print(answer)

answer = math.sqrt(16) # equivalent to Math.sqrt(16) in Javascript
print(answer)


president = 'Biden'
country = 'US'
currency = 'USD'
print(president, country, currency) # by default a single space is used as a separator
print(president, country, currency, sep=',') # using sep='' overrides; prints "Biden,US,USD"


print('This is CIS 2300 QTRA')
print('This\n is\n CIS\n 2300\n QTRA\n') # \n doesn't get printed out and is for putting things on a new line
print('This\t is\t CIS\t 2300\t QTRA\t') # \t doesn't get printed out and is for tab spacing


# can mix strings with variables in print statements
print('The president of', country, 'is', president, 'and its currency is', currency)
print(f'The president of {country} is {president} and its currency is {currency}') # Python formatted string (equivalent to template literal in Javascript)


# to print out binary or hex version of a number, wrap it in a bin() or hex()
my_num = 217
print(bin(my_num)) # --> prints 0b11011001
print(hex(my_num)) # --> prints 0xd9

my_bin_val = 0b1010 # a number in binary
print(bin(my_bin_val)) # --> prints 0b1010
print(my_bin_val) # --> converts into base 10 and prints 10 on its own

my_hex_val = 0xFF # hexadecimal value for 255
print(my_hex_val) # --> prints 255

my_oct_val = 0o17345 # octal value for 7909
print(my_oct_val) # prints 7909



# CONSTANTS
# constants are variables that are defined and cannot be changed (in Javascript: const string = "hello world")
# constants are not a thing in Python lol
# standard practice is to capitalize name of variable to indicate that you don't want the value to be changed and to consider it to be a constant; value can still be changed
tax_rate = 8.17 # by convention, this is a variable and is okay to change
tax_rate = 2
TAX_RATE = 8.17 # by convention, this is a constant
# bad practice to add this line after: TAX_RATE = 2
# note that tax_rate and TAX_RATE are two different variables (even tho they look the same) because variables are case sensitive



# Conditions
# = means an assignment
apples = 10
# assigning 10 to apples variable; putting value inside a variable

# == means asking the question are both sides equal to each other (equivalent to strictly equal === in Javascript)
apples == 10
# checks if the value of apples is equal to 10

# != means is not equal to each other (usually used in if else statements)
apples != 10
# means apples is not equal to 10

passing_signal = 'RED'
if passing_signal == 'RED':
    print('stop!') 
    print('wait') # anything indented within if or else condition is what will be executed
elif passing_signal == 'GREEN': # elif means else if (in this case, it means else if passing_signal is equal to green)
    print('gooooooooooo!')
elif passing_signal == 'YELLOW':
    print('cars slow down')
else: # else is used to specify what to do if passing_signal is not equal to'RED' or 'GREEN'
    print('uhhh figure something out')
# --> prints stop!

# In English: 
# passing_signal is a variable that has a value of 'RED'; 
# if the value of passing_signal is 'RED', print 'stop!' and 'wait'
# otherwise/else if the value of passing_signal is 'GREEN', print 'gooooooooooo!'
# otherwise/else if the value of passing_signal is 'YELLOW', print 'cars slow down'
# but if the value of passing_signal is not equal to 'RED' or 'GREEN' or 'YELLOW', print 'uhhh figure something out'

# another way of doing it is making individual if statements
if passing_signal == 'RED':
    print('stop!') 
    print('wait') 
if passing_signal == 'GREEN':
    print('gooooooooooo!')
if passing_signal == 'YELLOW':
    print('cars slow down')
if passing_signal != 'RED' & passing_signal != 'YELLOW' & passing_signal != 'GREEN'
    print('uhhh figure something out')