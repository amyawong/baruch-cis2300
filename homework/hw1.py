def get_value(word):
  letters = ' abcdefghijklmnopqrstuvwxyz'
  arr = list(letters)
  word_value = 0
  for i in word:
    word_value += arr.index(i)
  print(word_value)

# test cases
get_value('cat') # expected: 24, printed: 24
get_value('abc') # expected: 6, printed: 6
get_value('mmmmm') # expected: 65, printed: 65
get_value('hello') # expected: 52, printed: 52
get_value('world') # expected: 72, printed: 72
get_value('hello world') # expected: 124, printed: 124
# get_value('')