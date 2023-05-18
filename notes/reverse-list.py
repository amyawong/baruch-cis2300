# Method 1
list = [1, 2, 3, 'a', 'b', 'c']
list.reverse()
print(list)



# Method 2
list = [1, 2, 3, 'a', 'b', 'c']
def reverse_list_2(list):
    output = []
    for i in range(len(list) - 1, -1, -1):
        output.append(list[i])
    return output

print(reverse_list_2(list))



# Method 3
def reverse_list_3(list):
    for i in range(0, len(list)):
        # swap list[i] with list[len(list) - 1 - i]
        temp = list[i]
        # print(list[len(list) - 1 - i])
        list[i] = list[len(list) - 1 - i]
        list[len(list) - 1 - i] = temp
    return list

# print(reverse_list_3(list))




# Method 4
def reverse_list_4(list):
    out = []
    while len(list):
        out.append(list.pop())
    return out

# print(reverse_list_4(list))