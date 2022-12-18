def count_cs(list):
    count = 0
    for item in list:
        if item == 'c':
            count += 1
    return count

my_list = ['a', 'b', 'c', 'c', 10]
# print(count_cs(my_list))    # prints: 2
# can pass in my_list as list because it is being defined
# can also do:
# print(my_list.count('c'))   # prints: 2



def sum_up_items(list_of_nums):
    result = 0
    for num in list_of_nums:
        result += num
    return result

# print(sum_up_items([1, 2, 3, 4, 5, 6, 7, 8]))   # prints: 36
# print(sum_up_items(['a', 2, 3]))    # can NOT pass in string(s) because it it isn't possible to add a string with an integer



def print_elements(collection):
    for item in collection:
        print('item is:', item)

# print(print_elements([1, 2, 3, 4, 5, 6, 7, 8]))   # prints:
# item is: 1
# item is: 2
# item is: 3
# item is: 4
# item is: 5
# item is: 6
# item is: 7
# item is: 8



# In Python, it is possible to reassign values of variables by swapping them unlike other programming languages
a, b = 10, 20
# print(f'a = {a}, b = {b}')      # prints: a = 10, b = 20

# Swap variable values by doing so:
a, b = b, a
# print(f'a = {a}, b = {b}')      # prints: a = 20, b = 10