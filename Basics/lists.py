"""
Lists
There are four collection data types in Python :

    - List: is a collection which is ordered and changeable
    (modifiable). Allows duplicate members.
    
    - Tuple: is a collection which is ordered and unchangeable or 
    unmodifiable(immutable). Allows duplicate members.

    - Set: is a collection which is unordered, un-indexed and 
    unmodifiable in a no-restricted way (we can add and remove items), but 
    we can add new items to the set. Duplicate members are not allowed.

    - Dictionary: is a collection which is unordered, changeable
    (modifiable) and indexed. No duplicate members.

In this class you learn:

    - Declare list
    - Declaring a single list with different data types.
    - Accessing to list through index (negative and positive numbers)
    - Unpacking Lists
    - Slicing items from a list
    - Reverse items
    - Modifiying
    - Adding items
    - Checking for items
    - Inserting items with index
    - Removing items
    - Poping items (the same as removing, but giving the index)
    - Deleting items and deleting lists with keyword del (not a built-in function)
    - Clearing a list
    - Copying list
    - Joining lists (.extend() built-in function)
    - Find index in a list
    - Sorting lists with reverse = True
    
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
fruits_reversed_2 = fruits.reverse()
print(fruits_reversed)


fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] # it returns all the fruits
orange_and_mango = fruits[-3:-1] # it does not include the last index,['orange', 'mango']
orange_mango_lemon = fruits[-3:] # this will give starting from -3 to the end,['orange', 'mango', 'lemon']





# ==================== MODIFYING LIST ====================

fruits[0] = "avocado" # Now our first element will be avocado
print(fruits) # ['avocado', 'orange', 'mango', 'lemon'] avocado instead of banana




# ==================== CHEKING ITEMS IN A LIST ====================
# We can check the existence of an element in a list, as we do in strings.

does_exist = "banana" in fruits # Returns True or False
print(does_exist) # False, i modified the list, dissapearing banana





# ==================== ADDING ITEMS TO A LIST ====================
# REMEMBER we can do all this because lists are mutable

fruits.append("banana") # We add banana again





# ==================== INSERTING ITEMS INTO A LIST ====================
# We insert an item into a list like this:
# list.insert(index, item_to_insert)

# Index is the position that you wanna be that stay the item you want.

fruits.insert(0, "apple") # Insert an item into a list
print(fruits)





# ==================== REMOVING ITEMS ====================
# We specify the item
fruits.remove("banana") # We removed the item "banana" from the list.
# Removes the first ocurrence of banana





# ==================== POPING ITEMS ====================
# It works the same as remove, but in this we specify the index
# If we don't specify, it removes the last item
fruits.pop()

fruits.pop(0) # We remove apple

print(fruits) # ["avocado", "mango", "lemon"]





# ==================== DELETING LISTs ====================
# The del keyword removes the specified index and it can also be used to delete items within index range. 
# It can also delete the list completely

"""

SYNTAX

lst = ['item1', 'item2']
del lst[index] # only a single item
del lst        # to delete the list completely

"""

fruits.append(["banana", "apple", "pineapple"]) # ["avocado", "mango", "lemon", "banana", "apple", "pineapple"]

# We deleted ["avocado", "mango", "lemon"]
del fruits[0:3]
print(fruits)

# We delete fruits completly
del fruits
# print(fruits) # "fruits" are not defined





# ==================== CLEARING A LIST ====================
# It's the same as initializing a variable

fruits = ["avocado", "mango", "lemon", "banana", "apple", "pineapple"]
fruits.clear()
print(fruits) # []





# ==================== COPYING A LIST ====================
# This way is more efficient than reassing it a list this way:
# fruits_2 = fruits
# Why? It's only a theory, but i think that this (.copy()) copy exactly the memory adrees of our original list
# In the other hand, we create another space for the variable, so this way is more efficient.
# We use less RAM.

fruits = ["pineapple"]
fruits_2 = fruits.copy()





# ==================== JOINING LISTS ====================

# USING + operator
vegetables = ["leafy greens", "roots"]
extra_green_food = ["plant"]

# IT BEHAVES AS A STRING, IN INDEX TOO
green_food = fruits + extra_green_food + vegetables 
print(green_food) # ['pineapple', 'plant', 'leafy greens', 'roots']


# USING .extend() built-in function
# It's the same as + operator
green_food.clear()
green_food.extend(fruits)
green_food.extend(extra_green_food)
green_food.extend(vegetables)
print(green_food)





# ==================== COUNTING ITEMS IN A LIST ====================
# Returns the number of ocurrences of an item

"""

SYNTAX

list = ['item1', 'item2']
list.count('item1')

"""

list_numbers = [1, 1, 1, 2, 3, 4, 4, 5, 6, 6, 6, 6]
print(list_numbers.count(1)) # 3





# ==================== FINDING INDEX OF AN ITEM ====================

"""
SYNTAX

list = ['item1', 'item2']
list.index(item)

"""

number_1 = list_numbers.index(1) # Returns the first ocurrence, the position
print(number_1) # Returns 0





# ==================== SORTING LISTS ====================
fruits = ["avocado", "mango", "lemon", "banana", "apple", "pineapple"]
fruits.sort()
print(fruits) # This sort in alphabetical way
list_numbers.sort()
print(list_numbers)
list_numbers.sort(reverse = True)
# We have to reverse the lists before using them, but rather they return None (a NoneType)
print(list_numbers) # When we use reverse = True in .sort(), we literally reverse the sort list