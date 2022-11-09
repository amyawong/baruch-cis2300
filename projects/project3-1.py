M = 12345

count = 0

for n in range(1, M + 1):
    if (n % 2 == 0) and (n % 3 == 0) and (n % 5 == 0) and (n % 7 != 0):
    # can also do:
    # if (n % 30 == 0) and (n % 7 != 0):
        count += 1

print(count)    # expected: 353, printed: 353