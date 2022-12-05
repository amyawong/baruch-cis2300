# Iterating over a tuple
letters = ('a', 'b', 'c', 'x', 'm', 'n', 'o')

# Method 1: Iteration with indexing
# This method assigns a dyanmic index to the elements in the tuple which can be accessed through square brackets []
str1 = ''
for i in range(0, len(letters)):  # i is the name of the variable for each index of each variable in range(0, len(letters))
    element = letters[i]  # the variable element is assigned to the value of each element of letters, letters[i] represents each index of the tuple letters
    print(element)    # prints: a b c x m n o
    # element is printed on separate indvidual line because the variable element is assigned to each individual index of the letters tuple, meaning that the variable element has more than one definition    
    str1 += element    # tmp1 += letters[i] also works
print(str1)  # prints: abcxmno
# str1 is printed on one line because it starts off as an empty string and each index of the tuple is gradually added to the empty string until there is nothing left to add
# print(str1) is done OUTSIDE of the for loop and not within it because you want the result of it when the loop is over
# if print(str1) is inside the for loop, it would print out each time a new letter is concatenated to the str1 string


# Method 2: Directly iterating over elements
# This method assigns a variable to each index of the tuple which can be referred to again
str2 = ''
for e in letters:
    print(e)    # prints: a b c x m n o
    # e is printed on separate individual lines for same reason above
    str2 += e
print(str2)     # prints: abcxmno
# print(str2) prints out in one line for same reason as above



# Iterating over a list
verbs = ['walk', 'run', 'swim', 'stroll', 'sprint']

# Method 1: Iteration with indexing
str1 = ''
for i in range(0, len(verbs)):
    element = verbs[i]
    print(element)    # prints: walk run swim stroll sprint
    # strings are printed on individual separate lines because element has more than one value
    str1 += element    # str1 += verbs[i] also works
print(str1)    # prints: walkrunswimstrollsprint
# print(str1) prints everything into one string because str1 += element is essentially saying
# str1 = 'walk' + 'run' + 'swim' + 'stroll' + 'sprint', making it walkrunswimstrollsprint

# Method 2: Directly iterating over elements
str2 = ''
for e in verbs:
    print(e)    # prints: walk run swim stroll sprint
    # strings are printed on individual separate lines for same reason as above
    str2 += e
print(str2)    # prints: walkrunswimstrollsprint
# print(str2) prints everything into one string for same reason as above



# Iterating over nested lists/tuples 
employees = [('John', 43), ('Sally', 45), ('Jerry', 25)]
# explanation: you have a list named employee that contains three tuples where the first index of the tuple is the employee's name and the second index of the tuple is the employee's age

# Method 1: Iteration with indexing
str1 = ''
tuple1 = ()
for i in range(0, len(employees)):
    individual_employee = employees[i]
    print(individual_employee)    # prints: ('John', 43) ('Sally', 45) ('Jerry', 25)
    # print(employees[i]) also works
    # each set is printed on separate lines because the variable element is assigned to each index of the employees list
    # since the value of i goes from 0 to the length of the employees list MINUS 1 (since the last index is EXCLUSIVE, this means that length of employees is 3 and that the index of the last set is the length - 1, making the i in range in line 60 go from 0 to 2)
    # the values of individual_employee (or employees[i]) in this case are:
    # individual_employee[0] = ('John', 43), individual_employee[1] = ('Sally', 45), individual_employee[2] = ('Jerry', 25)
    
    print(individual_employee[0])    # prints: John \n Sally \n Jerry
    # print(employees[i][0]) does the same since the value of individual_employee is assigned to each element of employees list
    # only the names of employees are printed out on separate lines because we are choosing to print the 0th index of each tuple

    print(individual_employee[1])    # prints: 43 \n 45 \n 25
    # print(employees[i][1]) also does the same
    # only the ages of employees are printed out on separate lines because we are choosing to print the 1st index of each tuple

    # print(individual_employee[0] + individual_employee[1])    # prints: TypeError: can only concatenate str (not "int") to str
    # can NOT concatenate strings with integers, hence the error
    # HOWEVER, this works because of type coercion in formatted strings
    print(f'{individual_employee[0]}, {individual_employee[1]}')    # prints: John, 43 \n Sally, 45 \n Jerry, 25

    # str1 += individual_employee
    # print(str1)    # prints: TypeError: can only concatenate str (not "tuple") to str

    tuple1 += individual_employee    # tuple1 += employees[i] also works
    print(tuple1)    # prints: ('John', 43) \n ('John', 43, 'Sally', 45) \n ('John', 43, 'Sally', 45, 'Jerry', 25)
    # tuple1 gets printed on three separate lines because each index of individual_employee is gradually concatenated to the empty tuple until it runs out of indices

    # To print individual element in nested list, use another for loop
    for j in range(0, len(individual_employee)):
        # employee_info = individual_employee[i]  # BE AWARE: doing this will print "IndexError: tuple index out of range" because i goes from 0 to 2 whereas j goes from 0 to 1
        employee_info = individual_employee[j]
        print(employee_info)    # prints: John \n 43 \n Sally \n 45 \n Jerry \n 25
        # print(employees[i][j]) also works
        # each element is printed on an individual line since the variable employee_info has different values


# Method 2: Directly iterating over elements
str2 = ''
tuple2 = ()
for individual_employee in employees:
    print(individual_employee)    # prints: ('John', 43) \n ('Sally', 45) \n ('Jerry', 25)
    # prints each set onto an individual separate line since individual_employee directly references each set
    
    # str2 += individual_employee
    # print(str2)    # prints: TypeError: can only concatenate str (not "tuple") to str

    tuple2 += individual_employee
    print(tuple2)    # prints: ('John', 43) \n ('John', 43, 'Sally', 45) \n ('John', 43, 'Sally', 45, 'Jerry', 25)
    # tuple2 gets printed on three separate lines for the same reason as why tuple1 does

    for employee_info in individual_employee:
        print(employee_info)    # prints: John \n 43 \n Sally \n 45 \n Jerry \n 25
        # prints each element onto a separate line since employee_info directly references each string within the nested list

        # str2 += employee_info
        # print(str2)    # prints: TypeError: can only concatenate str (not "int") to str

        # tuple2 += employee_info
        # print(tuple2)    # prints: TypeError: can only concatenate tuple (not "str") to tuple


# Method 3: Accessing specific index of a list without for loop
# Alternatively, to print a specific element of a nested list, access it through indices as numbers
print(employees[1])    # prints: ('Sally', 45)
print(employees[1][0])    # prints: Sally
print(type(employees[1][1]))    # prints: <class 'int'>
print(employees[len(employees) - 1][0])    # prints: Jerry



# Iterating over sets (reminder: sets are used for when order does NOT matter)
"""
# Method 1: Iteration with indexing
# Access using indices for sets does NOT work
letters = set({'a', 'b', 'c', 'x', 'm', 'n', 'o'})
print(letters[2])   # prints: TypeError: 'set' object is not subscriptable

tmp1 = ''
for i in range(0, len(letters)):
    element = letters[i]
    # print('e', element)     # prints: TypeError: 'set' object is not subscriptable
    tmp += element
print(tmp)   # prints: TypeError: 'set' object is not subscriptable
"""

# Method 2: Directly iterating over elements
# Sets should be iterated using a direct for loop
letters = set({'a', 'b', 'c', 'x', 'm', 'n', 'o'})
tmp2 = ''
for letter in letters:
    print(letter)    # prints each index of set in a random order on individual line
    tmp2 += letter
print(tmp2)    # prints each index of set as a single string in a random order



# Type Coercion
set_of_planets = set({'Mercury', 'Venus', 'Earth', 'Mars'})
print(set_of_planets)    # prints: {'Mercury', 'Venus', 'Earth', 'Mars'}
print(type(set_of_planets))    # prints: <class 'set'>

# To change planets into a list, pass it into list()
list_of_planets = list(set_of_planets)
print(list_of_planets)    # prints: ['Earth', 'Venus', 'Mercury', 'Mars']
print(type(list_of_planets))    # prints: <class 'list'>



# To add an element to planets set, use .add()
set_of_planets.add('Jupiter')
print(set_of_planets)    # prints: {'Mars', 'Jupiter', 'Venus', 'Mercury', 'Earth} *
# * since ordering of sets doesn't matter, 'Jupiter' will be added anywhere into the set and the order will change each time program runs


# To add an element to list_of_planets, use .append()
list_of_planets.append('Saturn')
print(list_of_planets)    # prints: ['Mars', 'Earth', 'Venus', 'Mercury', 'Saturn']
# 'Saturn' will always only added to the end of list because that is what .append() does; to specify where to insert 'Saturn', use .insert() and pass in specified index of where you want to insert 'Saturn' into as first argument followed by 'Saturn' as second argument


# Sets and lists can be turned into strings
print(type(set_of_planets))    # prints: <class 'set'>
string_of_set_planets = str(set_of_planets)
print(string_of_set_planets)    # prints: {'Mercury', 'Jupiter', 'Venus', 'Earth' 'Mars'} *
## * since order of sets doesn't matter, order of printing changes each time string_of_set_planets is run; string coercion still works as proven by:
print(type(string_of_set_planets))    # prints: <class 'str'>

print(type(list_of_planets))    # prints: <class 'list'>
string_of_list_planets = str(list_of_planets)
print(string_of_list_planets)    # prints: ['Earth', 'Venus', 'Mercury', 'Mars', 'Jupiter] *
## * order will of elements will also change each time line 193 is ran because the internal prototype of string_of_list_planets is set
print(type(string_of_list_planets))    # prints: <class 'str'>


# Sets and lists can also be turned into tuples
print(type(set_of_planets))    # prints: <class 'set'>
tuple_of_set_planets = tuple(set_of_planets)
print(tuple_of_set_planets)    # prints: ('Jupiter', 'Mercury', 'Earth', 'Venus', 'Mars') *
## * order of elements in tuple_of_planets will also change each time line 201 is ran
print(type(tuple_of_set_planets))    # prints: <class 'tuple'>

print(type(list_of_planets))    # prints: <class 'list'>
tuple_of_list_planets = tuple(list_of_planets)
print(tuple_of_list_planets)    # prints: ('Earth', 'Venus', 'Mercury', 'Mars', 'Saturn') *
## * order of elements in tuple_of_list_planets will also change each time line 207 is ran
print(type(tuple_of_list_planets))    # prints: <class 'tuple'>


# A single list or set can be converted into a set by passing it into set() (if done properly)
set_a = set({'red', 'blue', 'orange'})
set_b = set({17, 19})
print(set(set_a))    # prints: {'orange', 'blue', 'red'} *
print(set(set_b))    # prints: {17, 19} *
# print(set({set_a}))    # prints: TypeError: unhashable type: 'set'

list_a = ['red', 'blue', 'orange']
list_b = [17, 19]
print(set(list_a))    # prints: {'blue', 'orange', 'red'} *
print(set(list_b))    # prints: {17, 19} *
print(type(set(list_a)))    # prints: <class 'set'>
print(type(set(list_b)))    # prints: <class 'set'>
# print(set({list_a}))    # prints: TypeError: unhashable type: 'list'

## * order of elements printed in set changes whenever respective line is run

# HOWEVER, it is NOT possible to convert multiple sets or multiple lists into a single set
# print(set({set_a, set_b})) # prints: TypeError: unhashable type: 'set'
# print(set({list_a, list_b}))    # prints: TypeError: unhashable type: 'set'
# print(set(list_a, list_b))    # prints: TypeError: set expected at most 1 argument, got 2



# Slicing
# - makes a shallow copy of a portion of a list/tuple/string into a new list/tuple/string at specified beginning and ending indices
# - used to extract specific elements of a list/tuple/string
# - important to note that the ORIGINAL list/tuple/string is NOT mutated


# List Slicing
my_list = [11, 13, 17, 19, 23, 29, 31, 37]
# index:    0   1   2   3   4   5   6   7

# Method 1: square brackets
my_list_2_v1 = my_list[0:3]
# first index (optional) is inclusive and is starting integer where slicing begins, second index (optional) is exclusive and ends one less than mentioned
print(my_list_2_v1)    # prints: [11, 13, 17]

# If first parameter is omitted, everything before second index parameter excluding itself is kept
my_list_3_v1 = my_list[:5]
print(my_list_3_v1)    # prints: [11, 13, 17, 19, 23]

# If second parameter is omitted, everything after first index parameter including itself is kept
my_list_4_v1 = my_list[2:]
print(my_list_4_v1)    # prints: [17, 19, 23, 29, 31, 37]

# If both paramters are omitted, arguments default to 0:0 (essentially makes a new copy of the list)
my_list_5_v1 = my_list[:]
print(my_list_5_v1)    # prints: [11, 13, 15, 17, 19, 31, 37]
print(my_list_5_v1 == my_list)    # prints: True (however, both have different reference values)
print(id(my_list) == id(my_list_5_v1))  # prints: False


# A third argument (optional, defaults to 0) serves as a step which determines the increment between each index for slicing
my_list_6_v1 = my_list[0:6:2]
print(my_list[0:6])    # prints: [11, 13, 17, 19, 23, 29] (these are my_list indices 0 to 5)
print(my_list_6_v1)    # prints: [11, 17, 23] (these are every other index from indices 0 to 5 from my_list)

# Omitting first and second arguments and including a third argument prints out every specified index (i.e. every second, third, fourth, fifth, etc. index)
my_list_7_v1 = my_list[::3]
print(my_list_7_v1)    # prints: [11, 19, 31]
## can use also for loop to do this but does NOT print as a list
for i in range(0, len(my_list)):
    if i % 3 == 0:
        print(my_list[i])    # prints: 11 19 31 (on individual line as an integer)

# Passing in a negative integer as a second argument cuts the list short by the positive value of the integer
my_list_8_v1 = my_list[:-2]
print(my_list_8_v1)    # prints: [11, 13, 17, 19, 23, 29] (last two elements are not there)
## using a for loop:
for i in range(0, len(my_list)):
    if i >= 0 and i < len(my_list) - 2:
        print(my_list[i]) # prints: 11 13 17 23 29 (on individual line as an integer)

# Passing in -1 as a third argument reverses the list
my_list_9_v1 = my_list[::-1]
print(my_list_9_v1)    # prints: [37, 31, 29, 23, 19, 17, 13, 11]
## using a for loop:
for i in range(len(my_list) - 1, -1, -1):
    print(my_list[i])    # prints: 37 31 29 23 19 17 13 11 (on individual line as an integer)

# Passing in -1 as first argument gives last element of list as a list
my_list_10_v1 = my_list[-1:]
print(my_list_10_v1)    # prints: [37]
# my_list_10_v1 = my_list[-1:][0] can be used to get it as an integer


# Method 2: slice() function
my_list = [11, 13, 17, 19, 23, 29, 31, 37]
# index:    0   1   2   3   4   5   6   7

my_list_2_v2 = my_list[slice(0,3)]
# first argument (optional, default is 0) is inclusive and is starting integer where slicing begins, second argument is exclusive and ends one less than mentioned
print(my_list_2_v2)    # prints: [11, 13, 17]
# print(my_list[slice(0, 3)]) also works

# If first argument is omitted, first argument defaults to 0 and slices from index 0 to specified index
my_list_3_v2 = my_list[slice(2)] # can also be: my_list_3_v2 = my_list[slice(None, 2)] or my_list_3_v2 = my_list[slice(0, 2)]
print(my_list_3_v2)    # prints: [11, 13]
# print(my_list[slice(2)]) also works

# If only 0 is passed in, an empty list is made
my_list_4_v2 = my_list[slice(0)] # means the same as: my_list_4_v2 = my_list[slice(0, 0)
print(my_list_4_v2)    # prints: []
# print(my_list[slice(0)]) also works

# To make a new copy of the list using slice(), pass in 0 and the length of the list
# Even though the last index of a list is the length of the list minus 1, the second argument to slice() is exclusive, meaning that it slices 1 before that index
my_list_5_v2 = my_list[slice(0, len(my_list))]
print(my_list_5_v2)    # prints: [11, 13, 15, 17, 19, 31, 37]
print(my_list_5_v2 == my_list)    # prints: True (however, both have different reference values)
print(id(my_list) == id(my_list_5_v2))  # prints: False
print(id(my_list_5_v1) == id(my_list_5_v2))  # prints: False

# A third argument (optional, defaults to 0) serves as a step which determines the increment between each index for slicing
my_list_6_v2 = my_list[slice(0, 6, 2)]
print(my_list[slice(0, 6)])    # prints: [11, 13, 17, 19, 23, 29] (these are my_list indices 0 to 5)
print(my_list_6_v2)    # prints: [11, 17, 23] (these are every other index from indices 0 to 5 from my_list)

# Setting first argument to 0, second argument to length of list, and including a third argument prints out every specified index (i.e. every second, third, fourth, fifth, etc. index)
my_list_7_v2 = my_list[slice(0, len(my_list), 3)]
print(my_list_7_v2)    # prints: [11, 19, 31]
## can use also for loop to do this
for i in range(0, len(my_list)):
    if i % 3 == 0:
        print(my_list[i])    # prints: 11 19 31 (on individual line as an integer)

# Passing in a negative integer as a second argument cuts the list short by the positive value of the integer
my_list_8_v2 = my_list[slice(0, -2)]
print(my_list_8_v2)    # prints: [11, 13, 17, 19, 23, 29] (last two elements are not there)
## using a for loop:
for i in range(0, len(my_list)):
    if i >= 0 and i < len(my_list) - 2:
        print(my_list[i]) # prints: 11 13 17 23 29 (on individual line as an integer)

# Use .reverse() to reverse a list
my_list_9_v2 = my_list.reverse()
print(my_list_9_v2)    # prints: [37, 31, 29, 23, 19, 17, 13, 11]
## using a for loop:
for i in range(len(my_list) - 1, -1, -1):
    print(my_list[i])    # prints: 37 31 29 23 19 17 13 11 (on individual line as an integer)

# Pass in -1 as first argument and length of list to get last element of a list
my_list_10_v2 = my_list[slice(-1, len(my_list))]
print(my_list_10_v2)    # prints: [37]
# easier way:
print(my_list[len(my_list) - 1])    # prints: 37 (on an individual line as an integer)



# Tuple Slicing
fruits = ('apples', 'mangoes', 'pears', 'oranges')
# index:      0         1         2         3

print(fruits[1:3])    # prints: ('mangoes', 'pears')
print(fruits[:-2])    # prints: ('apples', 'mangoes')
print(fruits[2:])    # prints: ('pears', 'oranges')
print(fruits[:])    # prints: ('apples', 'mangoes', 'pears', 'oranges')
print(fruits[0:4:3])    # prints: ('apples', 'oranges')
print(fruits[::2])    # prints: ('apples', 'pears')
print(fruits[:-3])    # prints: ('apples',)
print(fruits[::-1])    # prints: ('oranges', 'pears', 'mangoes', 'apples')
print(fruits[-1:])    # prints: ('oranges',)



# String Slicing
name = 'John Doe'
# index: 0 = 'J', 1 = 'o', 2 = 'h', 3 = 'n', 4 = ' ', 5 = 'D', 6 = 'o', 7 = 'e'

print(name[3])    # prints: n
print(name[2:5])    # prints: hn
print(name[:4])    # prints: John
print(name[6:])    # prints: oe
print(name[:])    # prints: John Doe
print(name[1:7:4])    # prints: oD
print(name[::2])    # prints: Jh o
print(name[:-3])    # prints: John
print(name[::-1])    # prints: eoD nhoJ
print(name[-1:])    # prints: e