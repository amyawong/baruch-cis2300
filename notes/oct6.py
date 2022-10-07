# Often times loops are used to either count things or sum up numbers

# Calculate sum of numbers in loop
total = 0  # 1. set counter variable at 0
for x in range(1, 15+1):  # 2. adding the +1 makes it so that 15 is included
  total = total + x  # 3. can also do total += x, both mean total = total + 1 + 2 + 3...+ 15  
print(total)  # 4. print outside of for loop so that not every value is printed
              # --> prints 120


# Count how many numbers between 1 and 15 are divisible by 3
# following same logic as example above:
numbers_divisible_by_3 = 0
for x in range(1, 15 + 1):
  if x % 3 == 0:
    numbers_divisible_by_3 += 1
print(numbers_divisible_by_3) # --> prints 5


# Print numbers divisible by 3
for x in range(1, 15 + 1):
  if x % 3 == 0:
    print(x) # --> prints 3 6 9 12 15


# Calculate the product of a sequence of numbers (same as factorial)
# trying to calculate product of 1 * 2 * 3 ... * 15
product = 1  # set initial value of product to 1 because if you set to 0, it will basically be doing 0 * 1 * 2 ... * 15, and any number multipled by 0 will be 0
for x in range(1, 15 + 1):
  product *= x
print(product) # --> prints 1307674368000



# While loops

# Formatting:
# defined_variable = some_value
# while a_condition_that_is_true:
#  run this code block

# Dangers of using while loops: infinite loops
# infinite loops do not stop running until computer runs out of power
"""
# EXAMPLE:
i = 14
while i < 15:
  print(i)
"""


# Display numbers 1 - 10 using a while loop
n = 1
while n <= 10:
# can also do while n < 11:
  print(n)
  n = n + 1

# same idea using a for loop
for n in range(1, 11):
  print(n)



# For loops vs While loops
# For loops are used when we have a good idea of initializer, stop condition, and incrementer
# While loops are used if we don't know how many iterations there will be


# To generate random numbers, need to import random library
import random
random_number = random.randint(1, 6)  # randint comes from random library; first argument is starting number and second argument is ending number; we are setting x to a random number between 1 to 6
print(random_number) # prints a random number between 1 to 6


# Print out temperature while it is below or equal to 60
temp = 15
while temp <= 60:
  print('Reading temperature from thermostat')
  temp = random.randint(32, 70)  # resetting the value of temp by assigning it to a random number between 32 to 70
  print(f'The temperature was {temp}')
# this while loop will run and continue to print as long as the value of temp is less than or equal to 60 after being reset



# nothing gets changes because value for i never changes and does not meet while loop condition, so it never enters the while loop
i = 15
while i < 15:
  print(i)