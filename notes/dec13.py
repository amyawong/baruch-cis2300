# will NOT be on final exam:
 
# Steps to open a file and read the contents
# 1. Open the file object in a particular mode
# open command opens name of file based off name and location of file
# open command only opens local files (files stored on your computer)
file_object = open("/Users/amy/Desktop/entire/path/to/whatever/file/you/want/to/access.py", "r")
    # this serves as an entry point to file being passed into open command
    # second arg is the mode of opening file - "w" for writing, "r" for reading, "a" for appending
    # file_object now serves as variable that points to file

# 2. Read content using .read() or .readline()
all_content = file_object.read()  # adding a .read() method lets you read file
print(all_content)

# readline() lets you read one line at a time
line_1 = file_object.readline()
line_2 = file_object.readline()
line_3 = file_object.readline()

print(line_1.strip())  # .strip() removes extra new line at the end of the lines
print(line_1.strip())
print(line_1.strip())

# 3. Once done with the file, MUST close file after opening
file_object.close()



# Another way of opening file using a with loop
FILENAME = "/Users/amy/Desktop/path/to/whatever/file/you/want/to/access.py"

# with command automatically closes file once we are out of the with scope and doesn't require close command
with open(FILENAME, "r") as file_object:
    line1 = file_object.readline().strip()
    print(line1)



# Read all lines of a file using a for loop
with open(FILENAME, "r") as file_object:
    for line in file_object:
        print('line', line.strip())



# Read something from a file and put into a list
file_items_list = list()
with open(FILENAME, "r") as file_object:
    for line in file_object:
        file_items_list.append(line.strip())

print(file_items_list)



# This reads the Excel .csv file contents and populates a list
EXCEL_FILE = "User/amy/Desktop/path/to/a/.csv"
excel_file_list = list()
with open(EXCEL_FILE, "r") as excel_file_object:
    for line in excel_file_object:
        excel_file_list.append(line.strip())

print(excel_file_list)



# How to write to a file
FILENAME = "/Users/amy/path/to/file/to/whatever/file/you/want/to/access/can/be/.py/or/.txt/or/whatever"
with open(FILENAME, "w") as file_object:    # change "r" to "w" puts it in writing mode
    file_object.write("This is a test")

with open(FILENAME, "w") as file_object:
    for i in range(0, 100 + 1):
        file_object.write("line:" + str(i))



# Object Oriented Programming
# - Polymorphism
# - Inheritance
# - Encapsulation
# - Abstraction



# Classes
# - custom data type
# - first letter of class is capitalized
# - within classes are methods
# - first method has to be named __init__ (constructor function in Javascript) and first argument is self (this in Javascript)

class Student:
    def __init__(self, first_name, last_name, major):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major

    def register(self, some_class):
        print(f'{self.last_name}, {self.first_name} is a {self.major} major and was just registered for {some_class}')

# Classes can be used to create new instances of students
student1 = Student('Michael', 'Scott', 'Business')
student2 = Student('Jane', 'Doe', 'Physics')

print(student1.major)                   # prints: music
print(student2.last_name)               # prints: Doe
print(type(student1))                   # prints: <class '__main__.Student'>
print(student1.register('CIS 2300'))    # prints: Scott, Michael is a Business major and was just registered for CIS 2300