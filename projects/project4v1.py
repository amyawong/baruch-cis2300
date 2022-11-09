def num_to_french(num):
  if num == 0:
    return 'zero'
  elif num == 1:
    return 'un'
  elif num == 2:
    return 'deux'
  elif num == 3:
    return 'trois'
  elif num == 4:
    return 'quatre'
  elif num == 5:
    return 'cinq'
  elif num == 6:
    return 'six'
  elif num == 7:
    return 'sept'
  elif num == 8:
    return 'huit'
  elif num == 9:
    return 'neuf'
  elif num == 10:
    return 'dix'

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
  if num == 0:
    return 'ling'
  elif num == 1:
    return 'yi'
  elif num == 2:
    return 'er'
  elif num == 3:
    return 'san'
  elif num == 4:
    return 'si'
  elif num == 5:
    return 'wu'
  elif num == 6:
    return 'liu'
  elif num == 7:
    return 'qi'
  elif num == 8:
    return 'ba'
  elif num == 9:
    return 'jiu'
  elif num == 10:
    return 'shi'

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
  if num == 0:
    return 'zero'
  elif num == 1:
    return 'one'
  elif num == 2:
    return 'two'
  elif num == 3:
    return 'three'
  elif num == 4:
    return 'four'
  elif num == 5:
    return 'five'
  elif num == 6:
    return 'six'
  elif num == 7:
    return 'seven'
  elif num == 8:
    return 'eight'
  elif num == 9:
    return 'nine'
  elif num == 10:
    return 'ten'

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
  if word == 'zero':
    return 0
  elif word == 'one':
    return 1
  elif word == 'two':
    return 2
  elif word == 'three':
    return 3
  elif word == 'four':
    return 4
  elif word == 'five':
    return 5
  elif word == 'six':
    return 6
  elif word == 'seven':
    return 7
  elif word == 'eight':
    return 8
  elif word == 'nine':
    return 9
  elif word == 'ten':
    return 10

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



def french_to_num(word):
  if word == 'zero':
    return 0
  elif word == 'un':
    return 1
  elif word == 'deux':
    return 2
  elif word == 'trois':
    return 3
  elif word == 'quatre':
    return 4
  elif word == 'cinq':
    return 5
  elif word == 'six':
    return 6
  elif word == 'sept':
    return 7
  elif word == 'huit':
    return 8
  elif word == 'neuf':
    return 9
  elif word == 'dix':
    return 10

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



def pinyin_to_num(word):
  if word == 'ling':
    return 0
  elif word == 'yi':
    return 1
  elif word == 'er':
    return 2
  elif word == 'san':
    return 3
  elif word == 'si':
    return 4
  elif word == 'wu':
    return 5
  elif word == 'liu':
    return 6
  elif word == 'qi':
    return 7
  elif word == 'ba':
    return 8
  elif word == 'jiu':
    return 9
  elif word == 'shi':
    return 10

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



# extra
def french_to_pinyin(word):
  if word == 'zero':
    return 'ling'
  elif word == 'un':
    return 'yi'
  elif word == 'deux':
    return 'er'
  elif word == 'trois':
    return 'san'
  elif word == 'quatre':
    return 'si'
  elif word == 'cinq':
    return 'wu'
  elif word == 'six':
    return 'liu'
  elif word == 'sept':
    return 'qi'
  elif word == 'huit':
    return 'ba'
  elif word == 'neuf':
    return 'jiu'
  elif word == 'dix':
    return 'shi'

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