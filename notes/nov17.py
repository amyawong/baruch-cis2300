# Data Structures
# - Basic data types: str, int, float, bool
# - Programs = algorithms (if...else, divide and conquer) + data structures



# Lists
# - can be named like a variable, need to be enclosed within square brackets, and each item needs to be separated by a comma
# - each item in a list is called an element
# - element can be an integer, string, boolean, or a mix, and values can be repeated
# - first element starts at index 0, second element starts at index 1, third element starts at index 2, etc.
# - last index will always be length - 1

numbers = [1, 2, 3, 5, 7, 0, 3]
print(numbers)          # prints: [1, 2, 3, 5, 7, 0, 3]
print(type(numbers))    # prints: <class 'list'>

countries = ["USA", "Canada", "Mexico"]
print(countries)        # prints: ['USA', 'Canada', 'Mexico']
print(type(countries))  # prints: <class 'list'>


basket = [1, 2, "xyz", 45, 92, False]
print(basket)           # prints: [1, 2, 'xyz', 45, 92, False]
print(type(basket))     # prints: <class 'list'>


# - can find length of a list by passing it into the len() function
print(len(numbers))     # prints: 7
print(len(countries))   # prints: 3
print(len(basket))      # prints: 6


# - can loop through a list with a for loop
for c in countries:
  print(c)              # prints: USA Canada Mexico

# - can access certain element of a list by passing in index number in square brackets
print(basket[0])                # prints: 1
print(basket[1])                # prints: 2
print(basket[len(basket) - 1])  # prints: False


# it is possible to extract elements and work with them as values
result = basket[0] + basket[1]
print(result)           # prints: 3

# - can replace the value of a list
fruits = ["apple", "orange", "grape", "mango"]
print('before changing fruits: ', fruits)   # prints: before changing fruits:  ['apple', 'orange', 'grape', 'mango']
fruits[0] = "banana"
print('after changing fruits:', fruits)     # prints: after changing fruits: ['banana', 'orange', 'grape', 'mango']


# - can delete using del keyword
del fruits[2]
print('fruits after deleting', fruits)      # prints: fruits after deleting ['banana', 'orange', 'mango']

# - can add a new element to tne end using append()
fruits.append('avocado')
print('fruits after appending to the end:', fruits)     # prints: fruits after appending to the end: ['banana', 'orange', 'mango', 'avocado']

# - can insert an element at a specified element using insert()
fruits.insert(2, "cherry")  # insert "cherry" at index 2
print('fruits after inserting at index 2', fruits)      # prints: fruits after inserting at index 2 ['banana', 'orange', 'cherry', 'mango', 'avocado']



# Tuples
# Dictionaries
# Sets
