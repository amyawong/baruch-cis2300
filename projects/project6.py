def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


# A = 12345
A = 12
B = 9 * A

count = 0

for i in range(A, B + 1):
    if is_prime(i):     # same as: if is_prime(i) == True:
        count += 1

print(count)


# this outputs only prime numbers between A and B
# for n in range(A, B + 1):
    # if is_prime(n) == True:
        # print(n)
    # else:
        # count += 1