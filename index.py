# Get average of three numbers
x = int(input('Enter X: '))
y = int(input('Enter Y: '))
z = int(input('Enter Z: '))
a = (x + y + z)/3
print('the average of the three numbers is', a)


# Get the bigger number of two numbers
x = int(input('Enter X: '))
y = int(input('Enter Y: '))
if x > y:
  print(x)
else:
  print(y)


# Convert a temperature in Fahrenheit to Celsius
def convert_F_to_C(temp):
  print((temp - 32) * (5 / 9))
convert_F_to_C(100)


# Find the greatest number out of three numbers
def get_greatest_of_three(num1, num2, num3):
  print(max(num1, num2, num3))
get_greatest_of_three(5, 9, 3)