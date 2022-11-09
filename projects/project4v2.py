num_to_word = {
  0: ['zero', 'zero', 'ling'],
  1: ['one', 'un', 'yi'],
  2: ['two', 'deux', 'er'],
  3: ['three', 'trois', 'san'],
  4: ['four', 'quatre', 'si'],
  5: ['five', 'cinq', 'wu'],
  6: ['six', 'six', 'liu'],
  7: ['seven', 'sept', 'qi'],
  8: ['eight', 'huit', 'ba'],
  9: ['nine', 'neuf', 'jiu'],
  10: ['ten', 'dix', 'shi']
}


def num_to_french(num):
  french = []
  for x, y in num_to_word.items():
    french.append(y[1])
  return french[num]
  
# Test Cases
print(num_to_french(0))
print(num_to_french(1))
print(num_to_french(2))
print(num_to_french(3))
print(num_to_french(4))
print(num_to_french(5))
print(num_to_french(6))
print(num_to_french(7))
print(num_to_french(8))
print(num_to_french(9))
print(num_to_french(10))



def num_to_pinyin(num):
  pinyin = []
  for x, y in num_to_word.items():
    pinyin.append(y[2])
  return pinyin[num]
  
# Test Cases
print(num_to_pinyin(0))
print(num_to_pinyin(1))
print(num_to_pinyin(2))
print(num_to_pinyin(3))
print(num_to_pinyin(4))
print(num_to_pinyin(5))
print(num_to_pinyin(6))
print(num_to_pinyin(7))
print(num_to_pinyin(8))
print(num_to_pinyin(9))
print(num_to_pinyin(10))



def num_to_english(num):
  english = []
  for x, y in num_to_word.items():
    english.append(y[0])
  return english[num]
  
# Test Cases
print(num_to_english(0))
print(num_to_english(1))
print(num_to_english(2))
print(num_to_english(3))
print(num_to_english(4))
print(num_to_english(5))
print(num_to_english(6))
print(num_to_english(7))
print(num_to_english(8))
print(num_to_english(9))
print(num_to_english(10))



def english_to_num(word):
  for key, values in num_to_word.items():
    for translation in values:
      if word == translation:
        return key

# Test Cases
print(english_to_num('zero'))
print(english_to_num('one'))
print(english_to_num('two'))
print(english_to_num('three'))
print(english_to_num('four'))
print(english_to_num('five'))
print(english_to_num('six'))
print(english_to_num('seven'))
print(english_to_num('eight'))
print(english_to_num('nine'))
print(english_to_num('ten'))



def pinyin_to_num(word):
  for key, values in num_to_word.items():
    for translation in values:
      if word == translation:
        return key

# Test Cases
print(pinyin_to_num('ling'))
print(pinyin_to_num('yi'))
print(pinyin_to_num('er'))
print(pinyin_to_num('san'))
print(pinyin_to_num('si'))
print(pinyin_to_num('wu'))
print(pinyin_to_num('liu'))
print(pinyin_to_num('qi'))
print(pinyin_to_num('ba'))
print(pinyin_to_num('jiu'))
print(pinyin_to_num('shi'))



def french_to_num(word):
  for key, values in num_to_word.items():
    for translation in values:
      if word == translation:
        return key

# Test Cases
print(french_to_num('zero'))
print(french_to_num('un'))
print(french_to_num('deux'))
print(french_to_num('trois'))
print(french_to_num('quatre'))
print(french_to_num('cinq'))
print(french_to_num('six'))
print(french_to_num('sept'))
print(french_to_num('huit'))
print(french_to_num('neuf'))
print(french_to_num('dix'))



# extra
def french_to_pinyin(word):
  for key, values in num_to_word.items():
    for translation in values:
      if word == translation:
        return values[2]

# Test Cases
print(french_to_pinyin('zero'))
print(french_to_pinyin('un'))
print(french_to_pinyin('deux'))
print(french_to_pinyin('trois'))
print(french_to_pinyin('quatre'))
print(french_to_pinyin('cinq'))
print(french_to_pinyin('six'))
print(french_to_pinyin('sept'))
print(french_to_pinyin('huit'))
print(french_to_pinyin('neuf'))
print(french_to_pinyin('dix'))