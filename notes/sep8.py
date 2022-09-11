# <-- a comment (code that gets ignored)

print("Hello World")
# equivalent to console.log("Hello World") in Javascript



# PROMPT: Summing up the numbers from 1-50
# in JavaScript:
# const addAllNumbers = num => {
#   let sum = 0;
#   for (let i = 1; i <= num; i++) {
#     sum += i
#   }
#   return sum
# }
# console.log(addAllNumbers(50)) // 1275

# in Python:
def add_all_numbers(number):
    sum = 0
    for x in range(number + 1):
        sum += x
    print(sum)
add_all_numbers(50)


# PROMPT: Counting numbers from 1-50 that are divisible by 10
# in JavaScript:
# const numbersDivisibleBy10 = num => {
#   let total = 0;
#   for (let i = 1; i <= num; i++) {
#     if (i % 10 === 0) {
#       total++
#     }
#   }
#   return total
# }
# console.log(numbersDivisibleBy10(50)) // 5

# in Python:
def numbers_divisible_by_10(number):
  total = 0
  for x in range(number):
    if x % 10 == 0:
      total += 1
  print(total)
numbers_divisible_by_10(50)