# Fundamentals of Programming: CRUD
# CRUD - Create, Retreieve, Update, Delete

# Data structures are used to hold sets of values


# Lists
# - can be read and changed

# 1. Creating empty lists
my_list_1 = []  # one way
my_list_2 = list()  # another way
print('my_list_1:', my_list_1)      # prints: my_list_1: []
print('num of items in my_list_1:', len(my_list_1))     # prints: num of items in my_list_1: 0


# 2. Creating pre-populated lists
fruits = ["apples", "oranges"]
print("fruits:", fruits)        # prints: ["apples", "oranges"]
print("num of items in fruits:", len(fruits))           # prints: num of items in fruits: 2


# 3. Accessing specific elements within the list
primes = [2, 3, 5, 7, 11, 13, 16]
print(primes[2])                # prints: 5
#  this accesses element at index 2
# the first index in a list/tuple is ALWAYS 0, meaning that first element in primes would be accessed with primes[0]


# 4. Appending elements to an existing list
fruits.append("bananas")
print("fruits:", fruits)        # prints: fruits: ["apples", "oranges", "bananas"]


# 5. Update existing elements within a list
fruits[1] = "grapes"
print("fruits:", fruits)        # prints: fruits: ["apples", "grapes", "bananas"]


# 6. Deleting particular elements
del fruits[0]
print("fruits:", fruits)        # prints: fruits: ["grapes", "bananas"]


# 7. Insert elements within 
fruits.insert(0, "mangoes") # push everything to the right to set "mangoes" as 0th index
fruits.insert(0, "mangoes") # repeat it another three times
fruits.insert(0, "mangoes")
fruits.insert(0, "mangoes")
print("fruits:", fruits)        # prints: fruits: ["mangoes", "mangoes", "mangoes", "mangoes", "grapes", "bananas"]
# Keep in mind that lists can have duplicates and values do NOT have to be unique


# Lists can contain lists within it
basket = ["USA", ["red", "blue"], ["Alaska", "Alabama", "Colorado"]]
print(len(basket))                      # prints: 3
print("basket[0]:", basket[0])          # prints: basket[0]: USA
print("basket[1]:", basket[1])          # prints: basket[1]: ["red", "blue"]
print("basket[2]:", basket[2])          # prints: basket[2]: ["Alaska", "Alabama", "Colorado"]
print("basket[1][0]:", basket[1][0])    # prints: basket[1][0]: red
print("basket[1][1]:", basket[1][1])    # prints: basket[1][1]: blue
print("basket[2][1]:", basket[2][1])    # prints: basket[2][1]: Alabama





# Tuples
# - are only read-only containers
# - can be created but can NEVER be modified
# - parentheses instead of square brackets
# - used for efficiency and when object won't change
# - faster to iterate through than lists

# 1. Creating empty tuples
my_tuple_1 = ()
my_tuple_2 = tuple()
print("my_tuple_1:", my_tuple_1)        # prints: my_tuple_1: ()
print("my_tuple_2:", my_tuple_2)        # prints: my_tuple_2: ()
print(len(my_tuple_1))                  # prints: 0


# 2. List methods do NOT work on tuples
my_tuple_1.insert(0, "mangoes")
print(my_tuple_1)                       # prints: "tuple object has no attribute 'insert'"


# 3. Creating pre-populated tuples
fruits = ("apples", "oranges")
print("fruits:", fruits)                        # prints: ("apples", "oranges")
print("num of items in fruits:", len(fruits))   # prints: 2


# 4. Accessing specific elements in tuples
primes = (2, 3, 5, 7, 11, 13, 17)
print(primes[4])                        # prints: 11


# 5. Tuples can contain tuples within them
basket = (19, ["a", "b"], (True, True, False, False))
print(basket[2][3])                     # prints: False





# Sets
# - behaves like a list but can NOT contain duplicates
# - can NOT control where to add element to list
# - index positions do NOT matter

# 1. Creating empty sets (only one way)
my_set_1 = set()
print('my_set_1', my_set_1)


# 2. Appending elements to a list
my_set_1.add("apples")
my_set_1.add("bananas")
my_set_1.add("cherries")
print("my_set_1:", my_set_1)         # prints: my_set_1: {"cherries", "apples", "bananas"}

my_set_1.add("mangoes")
my_set_1.add("mangoes")
my_set_1.add("mangoes")
print("my_set_1:", my_set_1)         # prints: my_set_1: {"cherries", "apples", "bananas", "mangoes"}
# error won't be thrown and "mangoes" is only added in once


# 3. Create a pre-populated set by invoking set function and filling in parentheses
num_set_1 = set({1, 3, 5, 7, 9, 11})
num_set_2 = set({2, 3, 5, 7, 11})


# 4. Getting intersection/union of sets
num_set_3 = num_set_1.intersection(num_set_2)
print("num_set_3", num_set_3)       # prints: {11, 3, 5, 7}


# 5. Check if something is in a set with the in command
print(3 in num_set_1)        # prints: True
print(333 in num_set_1)      # prints: False
print(6 in num_set_2)        # prints: False

if "Biden" in fruits:
    print("blue")
else:
    print("red")
# prints: red

if "apples" in fruits:
    print("blue")
else:
    print("red")
# prints: red