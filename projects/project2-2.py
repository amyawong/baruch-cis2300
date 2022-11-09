from math import sqrt

K = 16

# Method 1
left = int((( 1 + sqrt(5) )/2) ** K)
right = int((( 1 - sqrt(5) )/2) ** K)
test = (left - right) / sqrt(5)

print(round(test))



# Method 2: one line solution
print(round(((int((( 1 + sqrt(5) )/2) ** K)) - (int((( 1 - sqrt(5) )/2) ** K))) / sqrt(5)))