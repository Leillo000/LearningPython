"""

A tuple is a collection of different data types which is ordered and unchangeable 
(immutable). Tuples are written with round brackets, (). Once a tuple is created, 
we cannot change its values. We cannot use add, insert, remove methods in a tuple 
because it is not modifiable (mutable). Unlike list, tuple has few methods. 
Methods related to tuples:

    - tuple(): to create an empty tuple
    - count(): to count the number of a specified item in a tuple
    - index(): to find the index of a specified item in a tuple
    - + operator: to join two or more tuples and to create a new tuple

In this class you will see the methods before mentioned and :
    - Length
    - Accessing to a tuple
    - Slicing tuples
    - Converting tuples to lists
    - Checking for items in a tuple
    - Joining tuples
    - Deleting tuples

Source:
https://github.com/Asabeneh/30-Days-Of-Python/blob/master/06_Day_Tuples/06_tuples.md
    
"""

"""

SYNTAXIS

empty_tuple = ()

# or using the tuple constructor

empty_tuple = tuple()

"""

empty_tuple = () # This is a tuple

fruits = ("Banana","Apple","Pineapple") # We add initial values like we do in a list


# ============= LENGTH =============

print(len(fruits))





# ============= ACCESING WITH INDEX =============
# # Accesing to a tuple with index

print(fruits[0]) # Banana
print(fruits[-1]) # Pineapple





# ============= SLICING TUPLES =============

print(fruits[1:len(fruits) - 1])
print(fruits[1:])




# ============= CHANGING TUPLES TO LISTS =============
# We use the constructor list()
tuple_example = ("Mexico City", "Aguascalientes", "Monterrey")
list_changing = list(tuple_example)
list_changing[0] = "Puebla"
print(list_changing) # Now we can modify the list
 




# ============= CHECKING AN ITEM IN A TUPLE =============
does_exist = "Mexico City" in tuple_example # True
print(does_exist)





# ============= JOINING TUPLES =============
# In tuple's case, we can't use .extend() method, just through + operator

tuple_example_2 = ("Puebla", "Cuernavaca", "Zacatecas")
fusion_tuples = tuple_example + tuple_example_2
print(fusion_tuples)





# ============= DELETING TUPLES =============
del fusion_tuples
# print(fusion_tuples) # This throw an error

# We can say that a tuple is a list of constants