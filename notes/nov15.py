# Recursion
# think the movie Inception but with an ending
# breaking down a problem into a smaller set of problems

# iterative approach uses a loop
def factorial_iterative(n):
    result = 1
    for i in range(n, 0, -1):
        result *= i     # same as result = result * i

    return result
print(factorial_iterative(1))     # prints: 1
print(factorial_iterative(5))     # prints: 120



# recursive approach uses recursion
def recursive_factorial(num):
    # base case:
    if (num == 1) or (num == 0):
        return 1

    # recursive case:
    else:
        return num * factorial(num - 1)

print(recursive_factorial(1))     # prints: 1
print(recursive_factorial(5))     # prints: 120


# function calls on itself using smaller and smaller values
# makes the assumption that fact(n) = n * fact(n - 1)
# advantages: easier to write (because of compactness) and to analyze
# disadvantaes: can lead to RecursiveError which could exhaust memory and crash program



# Towers of Hanoi game
def move_discs(num, from_peg, to_peg, temp_peg):
    # num: the number of discs to move
    # from_peg: the peg to move from
    # to_peg: peg to move
    # temp_peg: the temporary peg
    if num > 0:
        move_discs(num - 1, from_peg, temp_peg, to_peg)
        print('Move a disc from peg', from_peg, 'to peg', to_peg)
        move_discs(num - 1, temp_peg, to_peg, from_peg)

move_discs(3, 1, 3, 2)
# prints:
# Move a disc from peg 1 to peg 3
# Move a disc from peg 1 to peg 2
# Move a disc from peg 3 to peg 2
# Move a disc from peg 1 to peg 3
# Move a disc from peg 2 to peg 1
# Move a disc from peg 2 to peg 3
# Move a disc from peg 1 to peg 3



# Fibonacci Series
# first two numbers of the series are ALWAYS 1 and 1
# next numbers are ALWAYS the sum of the previous two
# 1, 1, 2, 3, 5, 8, 13, 21...

# recursive approach
def fib(n):
    # base case
    if n == 1 or n == 2:
        return 1
    
    # recursive case
    else:
        return fib(n- 1) + fib(n - 2)

print(fib(2))   # prints: 1
print(fib(3))   # prints: 2
print(fib(5))   # prints: 5

# for visualization
for i in range(1, 15):
    print(fib(i))   # prints: 1 1 2 3 5 8 13 21 34 55 89 1 233 377