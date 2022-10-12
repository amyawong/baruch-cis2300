# break
# given a particular condition, you can exit out of a loop
# also works on while loops
for i in range(1, 101):
    print(f'iteration #{i}')
    if i == 19:
        break  # --> prints iteration #1 to iteration #19
    print('here is something else')
print('the for loop is done') # this is outside of the for loop, so it only prints out once; you can tell based off the indentation



# continue
# skips a certain condition in a condition
# also works on while loops
for i in range(1, 101):
    print(f'iteration #{i}')
    if i >= 19:
        continue  # --> prints iteration #1 to iteration #100 but skips iteration #19
    print('here is something else')
print('the for loop is done')



# nested loops
# bad time complexity, each additional loop raises by a factor of n
# avoid unless absolutely necessary
for a in range(1, 11):
    print(f'{a}')
    for b in range(5, 0, -1):
        print(f'-- {b}')


for a in range(1, 12 + 1):
    for b in range(1, 12 + 1):
        print(f'{a} * {b} = {a * b}'). # --> prints out multiplication


# Three letter password cracker
# assume all letters are lowercase
# brute force solution
# as password gets longer, it takes more time to figure guesses
# Method 1
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for letter_1 in alphabet:
    for letter_2 in alphabet:
        for letter_3 in alphabet:
            print(f'{letter_1}{letter_2}{letter_3}')  # --> prints out every combination


# Method 2
# if you pass in ascii code into the chr function, it returns the letter or symbol
print(chr(65))  # --> prints A

password = "zen"
found_password = False  # flagging variable, keeps track of a certain state

for l1 in range(65, 123):
    if found_password:
        break
    for l2 in range(65, 123):
        if found_password:
            break
        for l3 in range(65, 123):
            guess = chr(l1) + chr(l2) + chr(l3)
            print(guess)
            if guess == password:
                found_password = True
                print(f'password is {guess}')
                break
# English: found_password is initially set as false, with every loop, it checks if it matches password
# guess is a variable set as a combination of three letters, if it matches the password string, it changes the value of found_password to true, prints out password, and breaks out of the last loop
# In the real world, passwords are encrypted



# Generate a random number
# In Javascript: Math.random() * __
# In Python:
import random
letter1 = random.randint(97, 122)  # first argument is starting number, second argument is ending number and is inclusive
letter2 = random.randint(97, 122)
print(letter1, letter2)


# Password cracker using random strings and count how many tries it takes
password = "qi"
password_found == False
num_of_tries = 0

while password_found == False:
    letter1 = char(random.randint(97, 122))
    letter2 = char(random.randint(97, 122))
    guess = letter1 + letter2
    num_of_tries += 1
    print(f'trying password: {guess}')
    if guess == password:
        password_found = True
        break
print(f'it took {num_of_tries} tries')

