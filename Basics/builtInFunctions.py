
"""
len()
"""
# Count the lenght of a variable
word_1 = "Hello!"

print(len(word_1))

"""
input()
"""

my_age = input("Type your age: ")
print("Your age is:", my_age)

"""
int()
float()
str()
list()
tuple()
"""

# If we specify the data type, it just """ visual """, we can declarate gravity again as a bool, int, string, etc.
gravity : float = 9.81

print(int(gravity)) # Output : 9
print(type(str(gravity)))
# print(list(gravity)) a float can't be iterate
# Yes, you can print entire lists without iterate them position by position
print(list(word_1))
# Converting to a tupla. A tupla is inmutable.
print(tuple(word_1))

"""
round()
"""

# Round a number to his closer integer

print(round(gravity)) # Output : 10

