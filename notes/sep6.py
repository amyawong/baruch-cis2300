# PROMPT: print the bigger number out of two numbers
# in Javascript
# const biggerNum = (a, b) => {
#   if (a === b) {
#    return "both numbers are equal to each other"
#   } else if (a > b) {
#    return a
#   } else if (a < b) {
#    return b
#   }
# }
# console.log(biggerNum(5, 8))
# console.log(biggerNum(15, 15))

# in Python (method 1)
def bigger_number_v1(num1, num2): 
 if num1 == num2:
  print("both numbers are equal to each other")
 elif num1 > num2:
  print (num1)
 elif num1 < num2:
  print (num2)
bigger_number_v1(3, 5)
bigger_number_v1(593, 593)

# in Python (method 2 (easier and faster))
def bigger_number_v2(num1, num2):
  print(max(num1, num2))
bigger_number_v2(3, 17)
bigger_number_v2(92, 92)


# PROMPT: print the bigger number out of three numbers
# in Javascript
# function getMax(num1, num2, num3) {
#   if (num1 > num2) {
#     if (num1 > num3) {
#       return num1;
#     }
#     return num3;
#   } else if (num2 > num3) {
#     return num2;
#   } else {
#     return num3;
#   }
# }

# in Python (method 1)
def get_max_v1(num1, num2, num3):
 if num1 > num2 & num1 > num3:
  print (num1)
 elif num1 == num2 & num1 > num3:
  print (num1)
 elif num1 == num3 & num1 > num2:
  print (num1)
 elif num1 < num2 & num2 > num3:
  print (num2)
 elif num1 == num2 & num2 > num3:
  print (num2)
 elif num1 == num3 & num1 < num2:
  print (num2)
 elif num1 > num2 & num1 < num3:
  print (num3)
 elif num1 < num2 & num2 < num3:
   print(num3)
 elif num1 == num2 & num2 < num3:
  print (num3)
 elif num1 == num2 & num2 == num3:
  print ("all three numbers are equal to each other")
get_max_v1(4, 5, 2)
get_max_v1(84, 52, 84)
get_max_v1(67, 67, 67)

# in Python (method 2 (easier and faster))
def get_max_v2(num1, num2, num3):
 print (max(num, num2, num3))
get_max_v2(3, 5, 1)
get_max_v2(98, 98, 48)



# Application Programs (Executables)
# High Level Program 
#   - Java, C, Python, etc. --> Machine Language
#   - is done by some kind of a translation process

# Translation process comes in two "flavors":
# 1. Compiler 
#    - gives a one time translation form of code which computer CPU will execute
#    - give compiler executable code, once code is given, can get rid of compiler
#    - only need it once
#    - executables are efficient and don't take up a lot of memory
#    - allows for very fast execution
#    - optimization happens during compilation time
# 2. Interpreter 
#    - works with person; if person wants to change mind, interpreter will make appropriate translation
#    - runs in background and must always be run with program, without it, program will not run
#    - language examples: Python, Javascript
#    - will always need the interpreter
#    - can be resource intensive (takes up a lot of memory and use up a lot of CPU)
#    - allows for certain run-time optimization
#    - longer you run this type of code, the better the program gets



# homework: look at Anaconda or Spyder IDE and install one of them
# within Anaconda, launch Spyder