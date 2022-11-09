# Method 1
a, e, i, o, u, n, r, t, l, s = 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
d, g = 2, 2
b, c, m, p = 3, 3, 3, 3
f, h, v, w, y = 4, 4, 4, 4, 4
k = 5
j, x = 8, 8
q, z = 10, 10

# can also do:
# a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = 1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10

value = c + a + t
print(value)    # expected: 5, printed: 5



# Method 2
scores_and_letters = {
  0: [' '],
  1: ['a', 'e', 'i', 'o', 'u', 'n', 'r', 't', 'l', 's'],
  2: ['d', 'g'],
  3: ['b', 'c', 'm', 'p'],
  4: ['f', 'h', 'v', 'w', 'y'],
  5: ['k'],
  8: ['j', 'x'],
  10: ['q', 'z'],
}

def get_score(word):
  score = 0
  for i in word:
    for key in scores_and_letters:
      if i in scores_and_letters[key]:
        score += key
  return score

print(get_score('cat')) # expected: 5, printed: 5