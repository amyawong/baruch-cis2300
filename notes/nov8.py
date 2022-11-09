# 0) Function categories
# 1) Positional vs Named arguments (parameters)
# 2) Exceptions
# 3) Recursion


# Void Functions
# - do NOT return any values
def hello():
    tmp = "Hi, how are you?s
    
    print(tmp)

# all functions HAVE to be defined before they can be invoked
# to invoke hello(), do this:
hello()



# Non-Void (Value-returning) Functions
def get_hello_message():
    tmp = "Hello, how are you?"
    return tmp

# to invoke get_hello_message(), it has to be passed in a print function
print(get_hello_message()):



# Paramterized valule-returning function
def average(a, b):
    return (a + b)/2

print(average(5, 10))
# print(average('ten', 'twelve'))   # this will fail to execute and will throw a type error exception since you CANT pass in strings because even though it is possible to dd two strings together, it isn't possible to divide them by 2
    # Errors and Exceptions in Pyton are the same thing



# It is possible to customize error handling using a try/except block (Javascript version would be try/catch/finally)
def safe_average(a, b):
    try:
        result = (a + b)/2
        return result
    except:     # For any error, do the following
        print('The parameters must be integers')
        return None

print(safe_average(10, 12))     # prints: 11
print(safe_average('ten', 'twelve'))    # prints in Terminal: The parameters must be integers None



def my_division(param1, param2):
    return param1/param2

print(my_division(1, 2))     # prints: 0.5
print(my_division('1', 2))      # prints a TypeError because a string is being passed in and string can't be divided by 2
print(my_division(1, 0))        # prints a ZeroDivisionError


# It is possible to specify customized error handling
def my_division_2(param1, param2):
    try:
        return param1/param2
    except TypeError:   # if it is a TypeError, do the following
        print('The values passed are not the right type')
        return None
    except ZeroDivisionError:   # if there is a ZeroDivisionError, do the following
        print('Second parameter cannot be zero')
        return None
    except:     # for any other errors, do the following
        print('Something went wrong')
        return None

print(my_division_2(10, 5))     # prints: 2.0
print(my_division_2('1', 2))        # prints: The values passed are not the right type  None
print(my_division_2(1, 'two'))      # prints: The values passed are not the right type  None
print(my_division_2(7, 0))          # prints: Second parameter cannot be zero   None



# It is also possible to trigger an exception by raising it
def complainer():
    raise Exception("ERROR") # does not do anything but throw an error
    # in JavaScript: throw new Error("ERROR")

# complainer()    # prints Exception: ERROR

# Program will stop running once it hits an error
# Wrapping an error in a try/except block will ignore it and move on
try:
    complainer()
except:
    print('i am ignoring complainer()')



def calculate_total(item, unit_price, qty):
    total = unit_price * qty
    return 'The total price for ' + item + ' is ' + total

print(calculate_total('chips', 3.99, 17))       # prints: TypeError: can only concatenate str (not "float") to str
print(calculate_total('cookies', 7.99, 10))


# To get around error, convert total into a string by passing total into str()
def calculate_total_2(item, unit_price, qty):
    total = unit_price * qty
    return 'The total price for ' + item + ' is ' + str(total)

print(calculate_total_2('chips', 3.99, 17))     # prints: The total for chips is 67.83
print(calculate_total_2('cookies', 7.99, 10))   # prints: The total for cookies is 79.9



# Recursion
# - a function that calls on itself until it stops running
# - needs a base case and a recursive case

def countdown(n):
    for i in range(n, 0, -1):
        print(i)

print(countdown(10))   # prints: 10 9 8 7 6 5 4 3 2 1



def factorial(n):
    result = 1
    for i in range(n, 0, -1):
        result *= i     # same as result = result * i

    return result
print(factorial(1))     # prints: 1
print(factorial(5))     # prints: 120



def factorial_2(n):
    result = 1
    i = n

    while i >= 1:
        result *= i
        i -= 1
        return result

print(factorial_2(1))
print(factorial_2(5))


def recursive_factorial(num):
    # base case:
    if (num == 1) or (num == 0):
        return 1

    # recursive case:
    else:
        return num * factorial(num - 1)

print(recursive_factorial(1))     # prints: 1
print(recursive_factorial(5))     # prints: 120