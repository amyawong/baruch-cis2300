if passing_signal == "RED"

# WRONG way
if passing_singal == "AMBER":
    print('slow down, be cautious')
else:
    print: 


#  more concise way: 







# Conditional Branching
# Scenario: college admissions checking for one criteria
gpa = 2.7
sat = 1250
is_accepted = False # whenever you have boolean values, it is customary to name variable is_ followed by what is checked

if gp > 2.5 or sat > 1150:
    is_accepted = True
else: # it would be redundant to add this else because is_accepted is already set to False
    is_accepted = False

# INCORRECT approach (using and)
if gp > 2.5 and sat > 1150:
    is_accepted = True
else: # it would be redundant to add this else because is_accepted is already set to False
    is_accepted = False

print(f'gpa = {gpa}, sat = {sat}, accepted = {is_accepted}') # uses a template literal
print('gpa = ', gpa, 'sat = ', sat, 'accepted = ', is_accepted) # same as print statement above but without literal


# Scenario: college admissions checking for different criteria
gpa = 2.4
sat = 1250
essay = 75
is_accepted = False

if (gpa == 4.0) or (gpa > 2.5 and sat > 1150) or (gpa > 2.0 and sat > 900 and essay > 75): # wrap combined conditions in parentheses
    is_accepted = True
print(is_accepted) # --> prints false


# Short-circuit evaluation
gpa = 1.9
sat = 901

if gpa > 2.0 and sat > 800: # if first condition does not match (gpa > 2.0 in this case), python interpreter will not check the rest of the conditions (sat > 800) because this is an and expression
    print('accept') # --> will NOT print accept

gpa = 2.5
if gpa > 2.0 or sat > 800: # with or expressions, if the first condition (gpa > 2.0) is true, the rest of the conditions will not run
    print('accept') # --> prints accept



# For loops
# first argument is the starting condition
# second argument is ending condition that is exclusive to the for loop
# third argument is the incrementer

for num in range(1, 10): # last number is exclusive, meaning that it is NOT inclusive and does NOT include last number
    print(num) # --> prints 1 2 3 4 5 6 7 8 9

for num in range(1, 16):
    print('hello world') # --> prints hello world
    print('++++') # --> prints +++++
    print('!' * 20) # --> prints !!!!!!!!!!!!!!!!!!!!
    # print repeats itself 15 times

for x in range(17, 20): 
    print('test') # --> prints test 2 times because the difference between 17 and 20

# passing in 3 parameters into range function:
for y in range(0, 10, 2):
    print(y) # --> prints 0 2 4 6 8 (but not 10 because 10 is not inclusive to the for loop)

for z in range(0, 100, 10):
    print(z) # --> prints 0 10 20 30 40 50 60 70 80 90 (but not 100 because 100 is not inclusive)

for x in range(99, 0, -1):
    print(f'{x} bottles of beer on the wall, {x} bottles of beer,')
    print(f'Take one down and pass it around, {x - 1} bottles of beear on the wall\n')
    # --> prints the lyrics of the 99 bottles of beer on the wall but with grammatical errors towards the end of the song and doesn't include last line of song

# HOMEWORK: fix loop above to match lyrics in 99 bottles of beer on the wall