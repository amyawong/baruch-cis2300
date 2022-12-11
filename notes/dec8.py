# Dictionaries
# - A dictionary is a set of key-value pairs
# - also referred to as objects (in Javascript), maps, hashmaps, hashtables
# - Formatting
    # { key1: value1, key2: value2, key3: value3 }
# - first part is the key (what comes before the :), second part is value (what comes after the :)
# - keys MUST be unique and can NOT be duplicates
# - keys can only be strings or integers
# - key strings can NOT contain any spacing
# - each key MUST have a value
# - values can be strings, integers, lists, or tuples
# - values do not have to be unique and can be duplicates
# - each key-value pair is separated by a comma

# Create an empty dicitonary by using dict()
capitals = dict()       # here, an empty dictionary named capitals is created

print(capitals)             # prints: {}
print(type(capitals))       # prints: <class 'dict'>


# Setting up key-value pairs
capitals['USA'] = 'Washington, DC'
capitals['Canada'] = 'Ottawa'
capitals['Japan'] = 'Tokyo'

print(capitals)                 # prints: {'USA': 'Washington, DC', 'Canada': 'Ottawa', 'Japan': 'Tokyo'}     
print(len(capitals))            # prints: 3


# To access the value of a key, pass the key in [] as a string
print(capitals['Japan'])        # prints: Tokyo

# Since 'Mexico' is not a defined key in capitals, a key error prints
print(capitals['Mexico'])       # prints: KeyError: 'Mexico'



leaders = {'USA': 'Biden', 'Canada': 'Trudeau', 'Russia': 'Putin'}
print(leaders['Russia'])        # prints: Putin

leaders['Mexco'] = 'Obrador'
print(leaders)                  # prints: {'USA': 'Biden', 'Canada': 'Trudeau', 'Russia': 'Putin', 'Mexco': 'Obrador'}


# To delete a key-value pair for a specific key, use del keyword
del leaders['Canada']
print(leaders)                  # prints: {'USA': 'Biden', 'Russia': 'Putin', 'Mexco': 'Obrador'}
print(leaders['Canada'])        # prints: KeyError: 'Canada'
    # this generates an exception since the key no longer exists


# To check if something is in a dictionary
if leaders['Canada']:
    print('Canada was found in the dictionary')
else:
    print('Canada was NOT found in the dictionary')
# prints: KeyError: Canada

# Another way to check if a key is in a dictionary
if 'Canada' in leaders:
    print('Canada was found in the dictionary')
else:
    print('Canada was NOT found in the dictionary')
# prints: Canada was NOT found in the dictionary


# To change a value of a specific key that already has been defined, access it and reassign it
leaders['USA'] = 'Trump'
print(leaders)              # prints: {'USA': 'Trump', 'Russia': 'Putin', 'Mexco': 'Obrador'}


# Dictionary values can be the same, but keys MUST be unique and can NOT contain spacing
leaders['Trump_Tower'] = 'Trump'
print(leaders)              # prints: {'USA': 'Trump', 'Russia': 'Putin', 'Mexco': 'Obrador', 'Trump_Tower': 'Trump Tower'}


# Dictionary values can also be a list
leaders['Dreamland'] = ['Leader1', 'Leader2', 'Leader3']
print(leaders)              # prints: {'USA': 'Trump', 'Russia': 'Putin', 'Mexco': 'Obrador', 'Trump_Tower': 'Trump', 'Dreamland': ['Leader1', 'Leader2', 'Leader3']}

list_of_leaders = leaders['Dreamland']
print(list_of_leaders[0])   # prints: Leader1


# To only get the keys or values of a dictionary, loop with a for loop
for keys in leaders:
    print(keys)
    # prints: USA \n Russia \n Mexico \n Trump_Tower \n Dreamland

for values in leaders:
    print(leaders[values])
    # prints: Trump Putin Obrador Trump ['Leader1', 'Leader2', 'Leader3']
    print(f'The leader of {values} is {leaders[values]}')
    # prints: The leader of USA is Trump \n The leader of Russia is Putin \n The leader of Mexco is Obrador \n The leader of Trump_Tower is Trump \n The leader of Dreamland is ['Leader1', 'Leader2', 'Leader3']


# To clear a dictionary, use .clear()
leaders.clear()
print(leaders)              # prints: {}


# how to use type in if statements
if type(leaders) == str:
    print('leaders is a string')
elif type(leaders) == dict:
    print('leaders is a dictionary')
# prints: leaders is a dictionary



students = {'Jane': 90, 'David': 85, 'Sadat': 71}

# Use .get() to set a default value
score = students.get('Jane2', 70)   # if a key is not found, then return 70 as the default value
print(score)            # prints: 70


# To get key-values as a list
students_items = students.items()   # Object.entries() in Javascript
print(students_items)   # prints: dict_items([('Jane', 90), ('David', 85), ('Sadat', 71)])


# To get keys in a list
names = students.keys()     # Object.keys() in Javascript
print(names)            # prints: dict_keys(['Jane', 'David', 'Sadat'])


# To get values in a list
grades = students.values() # Object.values() in Javascript
print(grades)           # prints: dict_values([90, 85, 71])