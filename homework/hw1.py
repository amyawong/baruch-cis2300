# Flowchart 1: System asks temperature in Fahrenheit and displays the temperature in Celsius
# Worded Solution: Subtract given temperature by 32, then multiply result by 5/9
# In JavaScript:
  # const fahrenheitToCelsius = temperature => {
  #   return (temperature - 32) * (5 / 9)
  # }
  # console.log(fahrenheitToCelsius(100)) // 37.77...
  # console.log(fahrenheitToCelsius(120)) // 48.88...
# In Python:
def convert_F_to_C(temp):
  print((temp - 32) * (5 / 9))
convert_F_to_C(100)



# Flowchart 2: System asks for 3 inputs and displays the largest of the 3
# Worded Solution: Sort three numbers from least to greatest, then return the third number
# # In JavaScript:
  # const getMaxOfThree = (a, b, c) => {
  #   return Math.max(a, b, c)
  # }
  # console.log(getMaxOfThree(5, 8, 3)) // 8
  # console.log(getMaxOfThree(843, 1932, 4905)) // 4905
# In Python:
def get_greatest_of_three(num1, num2, num3):
  print(max(num1, num2, num3))
get_greatest_of_three(5, 9, 3)