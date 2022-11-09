# Method 1
a = 1 
b = 2
c = 3
d = 4
e = 5
f = 6
g = 7
h = 8
i = 9
j = 10
k = 11
l = 12
m = 13
n = 14
o = 15
p = 16
q = 17
r = 18
s = 19
t = 20
u = 21
v = 22
w = 23
x = 24
y = 25
z = 26

word = c + a + t
print(word)   # expected: 24, printed: 24



# Method 2
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def print_value(word):
    value = 0
    for score in range(len(word)):
      value += letters.index(word[score]) + 1
    return value

print(print_value('cat'))   # expected: 24, printed: 24