#   Base                      Number of symbols
# - Decimal (10)              10 (0, 1, 2, 3, 4, 5, 6, 7, 8, 9) => used to represent fractions, integers, decimals
# - Binary (2)                2 (0, 1) 
# - Octal (8)                 8 (0, 1 , 2, 3, 4, 5, 6, 7)
# - Hexadecimal (16)          16 (0 - 9, A (10), B (11), C (12), D (13), E (14), F(15))

# 157 in base 10 => 1*(10^2) + 5*(10^1) + 7*(10^0)
# 101 in base 2 => 1*(2^2) + 0*(2^1) + 1*(2^0) => 4 + 0 + 1 => 5 in base 10
# 157 in base 8 => 1*(8^2) + 5*(8^1) + 7*(8^0) => 64 + 40 + 7 => 111 in base 10
# 157 in base 16 => 1*(16^2) + 5*(16^1) + 7*(16^0) => 256 + 80 + 7 => 343 in base 10
# A0 in base 16 => 10*(16^1) + 0*(16^0) => 160 + 0 => 160 in base 10

# hex => binary
# 0 => 0000
# 1 => 0001
# 2 => 0010
# 3 => 0011
# 4 => 0100
# 5 => 0101
# 6 => 0110
# 7 => 0111
# A => 1010
# B => 1011
# C => 1100
# D => 1101
# E => 1110
# F => 1111
# A057B => 1010 0000 0101 0111 1011
#            A    0    5    7    B

# hex => base 10
# 1010 => 1*(16^3) + 0*(16^2) + 1*(16^1) + 0*(16^0) => 4096 + 0 + 16 + 0 = 4112

# A singular "digit" in binary is called a bit (i.e. 0)
# A collection of 4 bits is called a nibble (i.e. 0010)
# A collection of 8 bits is called a byte (i.e. 0010 1010)

# Advantage of hexadecimal is that it is good for converting to binary to base 10

# How computers read letters:
# letter => ascii => binary
# A => 65 => 01000001
# B => 66 => 01000010
# C => 67 => 01000011
# a => 97 => 01100001
# b => 98 => 01100010


# Computers have two types of memories
#  - RAM: stores information temporarily, only active when power is on, much faster
#  - Hard drive: stores information permanently


# Truth Table
# R = "it is raining" 
#   => negated would be not R or !R
#   !R = "it is not raining"
# S = "it is sunny" 
#   => negated would be not S or !S
#   !S = "it is not sunny"

#   conditionA    | conditionB    | conditionA && conditionB   | conditionA || conditionB
# --------------------------------------------------------------------------------------------
#   true          | true          | true                        | true
#   true          | false         | false                       | true
#   false         | true          | false                       | false
#   false         | false         | false                       | false

# 'and' is represented as &&
# 'or' is represented as ||
# putting a ! in front of a variable negates it


# Ways to represent solutions
# - Worded Solution
#   verbally expressed or written

# - Flow Charts
#   a diagram/a way to visually represent a solution
#   elliptical represents start/stop
#   parallelogram represents an input (from a keyboard/mouse) or an output (on computer screen, paper, etc)
#   rectangle represents a step/process (i.e. adding two numbers and putting result somewhere)
#   diamond represents a condition (yes or no)

# - Pseudocode
#   not actual code but can be used to represent a solution, code that isn't read

# - Program/Source Code
#   what actually gets read by computer