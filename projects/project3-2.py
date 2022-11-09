unique_num = 12340
K = unique_num * 19

count = 0

# count all the numbers between 1 and 10,000 (inclusive) that are even (divisible by 2)
for n in range(1, 10_000+1):
  if (n % 1 == 0) or (n % 3 == 0) or (n % 6 == 0) or (n % 4 == 0) or (n % 8 == 0):
    count += 1

print(count)