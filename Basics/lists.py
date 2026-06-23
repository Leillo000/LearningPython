"""
Lists
There are four collection data types in Python :

    - List: is a collection which is ordered and changeable
    (modifiable). Allows duplicate members.
    
    - Tuple: is a collection which is ordered and unchangeable or 
    unmodifiable(immutable). Allows duplicate members.

    - Set: is a collection which is unordered, un-indexed and 
    unmodifiable, but we can add new items to the set. Duplicate
    members are not allowed.

    - Dictionary: is a collection which is unordered, changeable
    (modifiable) and indexed. No duplicate members.

In this class you learn:

    - Declare list
    - Declaring a single list with different data types.
    - Accessing to list through index (negative and positive numbers)
    - Unpacking Lists
    - Slicing items from a list
    - Reverse items
    
An array != list, you can do a lot of things with a list comparing to
an array, talking about Python.

    All this info. don't belongs me, it belongs to:
    https://github.com/Asabeneh/30-Days-Of-Python/blob/master/05_Day_Lists/05_lists.md


"""

# There are two ways to declare a list

# list() is a built-in function of Python

empty_list = list()
print(len(empty_list)) # Output : 0

# Using square brackets

empty_list_2 = [] 
print(len(empty_list_2)) # Output : 0

# Length of a list

fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits

# Print the lists and its length
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))

# THIS IS IMPORTANT, this is an example of why a list is so different to a conventional array.
                       # String  # Int # Boolean   # Dictonary
list_dif_data_types = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}] # list containing different data types

print(list_dif_data_types) # It literally prints the above

dictonary_list = list_dif_data_types[3] # Equals to a dictonary

print(dictonary_list)

# We access to its element number 4 counting from right to left
# It's kinda similar to index a string.
string_list = list_dif_data_types[-4] 
print(string_list) # Output = Asabeneh





# ==================== UNPACKING LISTS ====================

# First Example

string_example = "Hello Everyone, how are you today?"
list_example = string_example.split(" ")
print(list_example)

# The * after declaring a variable means that will take the value / values of the element/s
# that weren't/ wasn't taken by other variable.

first_word, second_word, third_word, *rest = list_example

print(first_word) # Hello
print(second_word) # Everyone,
print(third_word) # how
print(rest) # ['are', 'you', 'today?']


# Second Example
                                                         
first_number, second_number, third_number, *rest_numbers, forth_number = [1, 2, 3, 4]

print(first_number) # 1
print(second_number) # 2
print(third_number) # 3
print(rest_numbers) # [], all values were taken
print(forth_number) # 0





# ==================== SLICING LISTS ====================
# It works the same like slicing a string.

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # it returns all the fruits

# this will also give the same result as the one above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3] # it does not include the first and last index
orange_mango_lemon = fruits[1:] # It doesn't include the first item

# We take an element each 2 items
orange_and_lemon = fruits[::2]





# ==================== REVERSING STRINGS ====================
# We can reverse items the same as strings
fruits_reversed = fruits[::-1]

print(fruits_reversed)


fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] # it returns all the fruits
orange_and_mango = fruits[-3:-1] # it does not include the last index,['orange', 'mango']
orange_mango_lemon = fruits[-3:] # this will give starting from -3 to the end,['orange', 'mango', 'lemon']
reverse_fruits = fruits[::-1] # a negative step will take the list in reverse order,['lemon', 'mango', 'orange', 'banana']