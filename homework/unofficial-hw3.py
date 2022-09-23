# original for loop set up as:
for x in range(99, 0, -1):
    print(f'{x} bottles of beer on the wall, {x} bottles of beer,')
    print(f'Take one down and pass it around, {x - 1} bottles of beer on the wall\n')
    # --> prints the lyrics of the 99 bottles of beer on the wall but with grammatical errors towards the end of the song and doesn't include last line of song


# HOMEWORK: fix loop above to match lyrics in 99 bottles of beer on the wall
for x in range(99, 0, -1):
  if x < 100 and x > 2:
  # can also do: 
  # if x < 100 and x >= 3:
  # if x <= 99 and x > 2:  
  # if x <= 99 and x >= 3:
    print(f'{x} bottles of beer on the wall, {x} bottles of beer,')
    print(f'Take one down and pass it around, {x - 1} bottles of beer on the wall\n')
  elif x == 2:
    print(f'{x} bottles of beer on the wall, {x} bottles of beer,')
    print(f'Take one down and pass it around, {x - 1} bottle of beer on the wall\n')
  elif x == 1:
    print(f'{x} bottle of beer on the wall, {x} bottle of beer,')
    print('Take one down and pass it around, no more bottles of beer on the wall\n')

print('No more bottles of beer on the wall, no more bottles of beer')
print('Go to the store and buy some more, 99 bottles of beer on the wall')