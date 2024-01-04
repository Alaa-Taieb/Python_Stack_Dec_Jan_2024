# The print method us used to display 'things' to console.
# print("Hello World!")

"""
    This is a multiline comment.
    Line 2
    Line 3
"""

# Variables
# Declaring a variable => variable_name = variable_value
# String
name = "John"

# Integers 
age = 51

# Float
height = 1.81

# Boolean
is_married = False

# List
my_list = [15,23,45,88]
# print(my_list[1])
my_list[0] = -23
# print(my_list[1])
my_list.append(99)
# print(my_list)

# Dictionary
human2 = {
    "name": "Mike",
    "age": 12,
    "height": 1.71,
    "is_married": False,
}

human = {
    "name": "John",
    "age": 51,
    "height": 1.81,
    "is_married": False,
    "brother": human2
}


human["hobbies"] = ["Reading" , "Coding" , "Gaming"]

print(human["hobbies"][0])

# Tuple
my_tuple = (15 , 35 , 18)

# Casting
number_string = "50"
number_integer = int(number_string)
print(type(number_string))

# Tuple => List
new_list = list(my_tuple)
new_list.append(150)
new_list.append(155)
my_tuple = tuple(new_list)

print(my_tuple)


"""
javascript
if condition {
    instruction 1  
    instruction 2  
    instruction 3
    ...  
}

"""

# Conditionals
# We have a bar that only lets in people 18 years old or older 
if human["age"] >= 18 :
    print(f"Welcome {human['name']} to our prestigious bar.")
else:
    print("Sorry we can't let you in.")


# Loops
# A loop is a way to execute the same code block multiple times.
# A loop is also used to iterate over a list or tuple

# print("Hello ") # x5
# for i in range(100):
#     print("Hello ")
#     print("World!")

my_list = [15,23,45,88 , 454 , 55 , 99 , 999]

for value in my_list:
    value = value + 1

print(my_list)

# Create a loop that adds 1 to each value in this list
for i in range(0 , len(my_list), 2):
    print(i)

print(my_list)
