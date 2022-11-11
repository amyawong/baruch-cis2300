# General rule of thumb: avoid using global variables as much as possible
# Global variables are variables that exist outside of functions of a program

# print() is for displaying and not actually using it
# print() can be used to check value of variable(s) at different points
# return is for values you want to use for something else and not just displaying it



def factorial_visualizer(n):
    print(f'function factorial_visualizer was called with parameter {n}')   # added print statement to visualize changes of n
    if n == 1:
        return n
    else:
        return n * factorial_visualizer(n - 1)

print(factorial_visiualizer(5))
# prints:
# function factorial_visualizer was called with parameter 5
# function factorial_visualizer was called with parameter 4
# function factorial_visualizer was called with parameter 3
# function factorial_visualizer was called with parameter 2
# function factorial_visualizer was called with parameter 1
# 120



def mad_function(p):
  if p < 10:
    return 1
  else:
    return mad_function(p - 1)

print(mad_function(99))     # prints: 1
print(mad_function(1005))   # prints: 1
# this will always print out 1 because the (p - 1) in the recursive case decrements the value of p until it hits the if condition where p is less than 10 (unless maximum call stack is exceded)



def f(msg):
    output = "this is the message:" + msg
    print(output)

def g(msg):
    output = "this ist he message:" + msg
    print(output)

# the msg parameter and output variable in both functions are unrelated to each other since they are in different functions and in local scopes
# anything that happens in a function stays within a function unless it is returned



def h(a):
    print(a)
    a = 100
    return "hello"

result = h('flower')    # prints: flower BUT returns hello
print(result)           # prints: hello



def h(a):
  print(a)
  a = 100
  return "hello"

x = 19.2
result = h(x)   # prints: 19.2
print(x)        # prints: 19.2
print(result)   # prints: hello



def display_facts(country, capital, leader):    # parameters are positional and the order they are passed in matters, can't pass it in as (country, leader, capital) otherwise order of print statement will be messed up
    print(f'The capital of {country} is {capital} and the leader is {leader}')

# function is invoked using positional arguments
display_facts('USA', 'Washington DC', 'Joe Biden')                          # prints: The capital of USA is Washington DC and teh leader is Joe Biden
display_facts('Canada', 'Ottowa', 'Justin Trudeau')                         # prints: The capital of Canada is Ottowa and the leader is Justin Trudeau
display_facts('Mexico', 'Mexico City', 'Andrés Manuel López Obrador')       # prints: The capital of Mexico is Mexico City and the leader is Andrés Manuel López Obrador

# functino is invoked using named arguments, order of parameters does not matter if set up like this
display_facts(country = 'China', leader = 'Xi Jinping', capital = 'Beijing')    # prints: The capital of China is Beijing and the leader is Xi Jinping



#  can set up functions with default values
def state_capital(state = 'NY', capital = 'Albany'):
    print(f'The capital of {state} is {capital}')


state_capital() # since state and capital are already defined, prints: The capital of NY is Albany

# sticks with default value unless explicitly changed
state_capital(state = 'CT')     # prints: The capital of CT is Albany
state_capital(capital = 'Manhattan')    # prints: The capital of NY is Manhattan
state_capital('California', 'Sacramento')   # prints: The capital of California is Sacramento
    # can also do state_capital(state = 'California', capital = 'Sacramento') or state_capital(capital = 'Sacramento', state = 'Calfiornia')



# it is also possible to pass in variables as default values
NY_SALES_TAX_RATE = 8.875

def calculate_price(qty, price, tax = NY_SALES_TAX_RATE / 100):
    return qty * (price * (1 + tax))

print(calculate_price(50, 10, NY_SALES_TAX_RATE / 100))     # prints: 544.375

# tax parameter goes with default value
print(calculate_price(50, 10))                              # prints: 544.375