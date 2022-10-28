def max_3(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= c and b >= a:
        return b
    elif c >= a and c >= b:
        return c

print(max_3(4, 9, 2))


# Easier method because life is already hard enough:
def max_of_3(a, b, c):
    max_num = max(a, b, c)
    return max_num

print(max_of_3(4, 9, 2))  # --> prints 9

# In Javascript:
# const maxOf3 = (a, b, c) => Math.max(a, b, c)
# console.log(maxOf3(4, 9, 2))



def ten():
    return 10
# this function is called ten and no matter what, it returns 10

ten()
# calling the function like invokes it, but nothing is printed

print(ten())  # --> prints 10
# passing it through the print function prints out the result

xyz = ten()
# assigning the value of ten function to a variable called xyz

xyz += 5  # xyz now has a value of 15 because ten() has a value of 10 and 10 + 5 = 15
xyz *= 3  # xyz is now 45 because 15 * 3 = 45
print(xyz)  # --> prints out 45


# In Javascript:
# const ten = () => 10
# console.log(ten())
# xyz = ten()
# xyz = 5
# xyz *= 3
# console.log(xyz)



def mysterious():
    a = 10
    b = a  # this means that b also as a value of a, makes a shallow copy of a
    pass
    c = 10
print(mysterious())
# None in Python means that something does not have a value assigned
# calling a function that doesn't return anything or does not have a return statement
# functions that return nothing are called void functions and do not contain any return statements



# Local variables mean that they are contained within a function (defined within local scope)
# Global variables are variables that are outside of functions that any function can have access to (defined in the global scope)

global_var = 8.875
def global_vs_local():
    local_var = 1
    print(global_var)
print(global_vs_local())  # --> prints 8.875 and None
print(local_var)  # --> prints an error because local_var is a local variable that isn't accessible outside of the function

# another example
# using global keyword overrides the value of the global variable
some_var = 23
def global_vs_local_v2():
    global some_var # global keyword reassigns the value of a global variable in a function
    some_var = 59
    return some_var
print(global_vs_local_v2())  # --> prints 59
print(some_var)  # --> prints 59