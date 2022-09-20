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
        score += int(key)
  print(score)

# test cases
get_score('cat') # expected: 5, printed: 5
get_score('bad') # expected: 6, printed: 6
get_score('mmmmm') # expected: 15, printed: 15
get_score('hello') # expected: 8, printed: 8
get_score('world') # expected: 9, printed: 9
get_score('hello world') # expected: 17, printed: 17
# get_score('')