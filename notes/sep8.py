# <-- a comment (code that gets ignored)

print("Hello World")
# equivalent to console.log("Hello World") in Javascript



# PROMPT: Summing up the numbers from 1-50
# in JavaScript:
# const addAllNums = num => {
#   let sum = 0;
#   for (let i = 1; i <= num; i++) {
#     sum += i
#   }
#   return sum
# }
# console.log(addAllNums(50)) // 1275

# in Python:
def addNumbers(number):
    sum = 0
    for x in number:
        sum += x
    print(sum)



# PROMPT: Counting numbers from 1-50 that are divisible by 10
# in JavaScript:
# const numsDivisibleBy10 = num => {
#   let total = 0;
#   for (let i = 1; i <= num; i++) {
#     if (i % 10 === 0) {
#       total++
#     }
#   }
#   return total
# }
# console.log(numsDivisibleBy10(50)) // 5

# in Python:
def numbersDivisibleBy10(number):
  sum = 0
  for x in range(number):
    if x % 10 == 0:
      sum += 1
  print(sum)
numbersDivisibleBy10(50)