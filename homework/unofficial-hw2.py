# Problem #1: A small town has a population of 27,000 people. A mild flu virus is spreading across the population and the infection rate is such that appromiately 2 times more people get infected each day. If the infection started with 1 person on day 1 (she returned back from a vacation abroad), on what day will this virus have spread across the entire population? We assume that once infected, the virus stays in the body indefinitely and the person becomes contagious.
# Day 1 -- 1 person infected
# Day 2 -- 2 persons infected
# Day 3 -- 4 persons infected
# Day ?? -- 27,000 or more persons infected
# Your goal is to find ??

# Psuedocode
# Need to establish a relationship between day number and number of people infected
# Number of people infected is exponential
# Need to solve 2^(x-1) where x is the day number and the result is the number of people infected
# Determine paramters - initially infected and population size
# Solution is 15 for this scenario since 2^15 is 32768 but 2^14 is 16384

# Edge Cases
# - Can a person be reinfected and if so, are they counted once or twice?
# - What if solution asks for decimal as answer (i.e. Day 7.3)?
# - What if number of people infected doesn't start at 1?

# In Javascript:
# const daysTilInfected = (infected, populationSize) => {
#   let dayNum = 1;
#   while (2 ** (dayNum - 1) < populationSize) {
#     infected = 2 ** (dayNum - 1)
#     dayNum++
#   }
#   return dayNum - 1
# }
# console.log(daysTilInfected(1, 27000)) // 15
# console.log(daysTilInfected(1, 1024)) // 10

# In Python:
def days_Til_Infected(infected, populationSize):
  dayNum = 1
  while 2 ** (dayNum - 1) < populationSize: 
    infected == 2 ** (dayNum - 1)
    dayNum += 1
  print(dayNum - 1)
days_Til_Infected(1, 27000)
days_Til_Infected(1, 1024)



# Problem #2: In arithmetic you have 4 basic operations: addition, subtraction, multiplication, and division. In mathematics, there is another operation called modulo. It is usually referred to as mod and '%' is used to denote this operation.
# In simplest terms, given two integers (whole numbers), x and y:
# x mod y (or x % y)  equals the remainder that is left over when we try to divide x with y.
# Thus, 5 % 2 equals 1. Why? because if you try to divide 5 by 2, using methods of long division you learned in school, 2 x 2 = 4 is the closest number you can get to 5, and 1 remains.
# Similarly, 31 % 14 equals 3. why? 14 x 2 = 28 is the closest you can get to 31 and then 3 remains.
# As a consequence of this, if you pick any number N and mod it with 2, if the result is 0, it means that the number is divisible by 2. Thus 2 % 2 equals 0, 4 % 2 equals 0, 6 % 2 equals 0, and so on...If N % 2 equals 0, then N is even.
# Similarly if N % 10 equals 0, then N must be divisible by 10.
# If you want to know more about mod, check: https://www.youtube.com/watch?v=pNXwzIohx8c
# Actual Problem Statement: Given all this background, design an algorithm that counts how many numbers between 1 and 25 are divisible by 3 and displays that count.

# Pseudocode
# Numbers between 1 and 25 divisible by 3: 3, 6, 9, 12, 15, 18, 21, 24
# Total numbers: 8
# Function should output 8 if given 1 and 25 as input range

# Edge Cases
# - What if range includes negative numbers?
# - Are numbers inclusive or exclusive to the range? (i.e. if range is between 1 and 24, do we include or exclude 24?)
# - What if number range doesn't start at 1?
# - Does 0 count? (since 0 % 3 === 0)

# In Javascript:
# const divisibleBy3 = (start, end) => {
#   let count = 0;
#   for (let i = start; i <= end; i++) {
#     if (i % 3 === 0) {
#       count++
#     }
#   }
#   return count
# }
# console.log(divisibleBy3(1, 25)) // 8
# console.log(divisibleBy3(6, 30)) // 9

def divisible_by_3(start, end):
  count = 0
  for i in range(start, end + 1):
    if i % 3 == 0:
      count += 1
  print(count)
divisible_by_3(1, 25)
divisible_by_3(6, 30)
