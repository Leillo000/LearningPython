"""

Set is a collection of items. Let me take you back to your elementary or high school
Mathematics lesson. The Mathematics definition of a set can be applied also in Python.
Set is a collection of unordered and un-indexed distinct elements. In Python set is 
used to store unique items, and it is possible to find the union, intersection, difference,
symmetric difference, subset, super set and disjoint set among sets.

Note: We say that 2 sets are disjoint, if they don't share any element.

We don´t use sets to find a value, but we use it to find intersections and differences.

It's unmutable, not-indexed and unordered. But we can add and remove items.
Duplicated members aren't allowed.

We will see in this class: 
 
    - Creating a Set: set() never just {}. If we put in initial values we can use just {} so
    - Getting Set's Length : len()
    - Accessing Items in a Set : with loops
    - Checking an Item: in
    - Adding Items to a Set .add(item), .update(list or set or tupla)
    - Removing Items from a Set: .remove(item)
    - Clearing Items in a Set:  .pop(no-argument because it's un-indexed), .clear()
    - Deleting a Set: del
    - Converting List to Set
    - Joining Sets : .union()
    - Finding Intersection Items : intersection()
    - Checking Subset and Super Set: issuperset() and issubset()
    - Checking the Difference Between Two Sets : .difference()
    - Finding Symmetric Difference Between Two Sets : .symmetric_difference()
    - Joining Sets : .isdisjoint()


Source: https://github.com/Asabeneh/30-Days-Of-Python/blob/master/07_Day_Sets/07_sets.md

"""

# ============= CREATING EMPTY SETS =============
# my_set = {} We can't declare sets like this because it will be detected as a dictonary
my_set = set()
my_set_1 = {1, 2, 3, 4, "hola"}






# ============= GETTING LENGTH=============
print(len(my_set), "Length of my_set") # 0






# ============= CHECKING FOR AN ITEM =============
print("Does hola is in my_set?", "hola" in my_set_1)





# ============= ADDING ITEMS TO A SET =============
my_set.add(1) # If we left the set declaration as my_set = {}, this would've crashed because it would detected as a dictonary
my_set.add(2)
my_set.add(3)
print(my_set) 

# We can add elements in list format with .update()
my_set.update([2, 3, 4]) # We put as parameter a list
print(my_set, "We updated the set") # It doesn't allow duplicated memvers, so automatically takes out the duplicated members
# 1, 2, 3, 4 and not 1, 2, 3, 2, 3, 4




# ============= ACCESSING ITEMS IN A SET =============
# We will see it in loop section





# ============= CHECKING FOR ITEMS =============
print("Does 1 is in my_set?", 1 in my_set) # True





# ============= REMOVING ITEMS FROM A SET =============
my_set.remove(1)
print(my_set, "We removed 1 number")
# We can use .pop() which removes a random item of our set
my_set.pop() # We can't specify the index because a set is un-indexed
# If we intersted in the removed item
# removed_item = my_set.pop()
print(my_set, "I removed a random item with pop")








# ============= CLEARING SETS =============
# To clear a set
my_set.clear()
print(my_set)







# ============= DELETING A SET =============
del my_set








# ============= LIST TO SET =============
my_set = {1, 2, 3, 4}
my_list = list(my_set)
print(my_list, "Set to List")

my_list.append(1) # If we add a duplicate value, it automatically takes out.
my_set_example = set(my_list)
print(my_set_example, "List to Set")
# This can be dangerous because the set order is random, and if we try to access
# to an index, the returned value it will changed every execution
# Example:

print(my_list[0]) # It can change every execution







# ============= JOINING SETS =============
# As in math, we join sets making them in a union

# EXAMPLE
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2) #st3 = st1 | st2

print(st3)

# We can use update too
# st3 = st1.update(st2)







# ============= FINDING INTERSECTIONS =============
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}
# It shows the coincidences between the sets.
python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.intersection(dragon)     # {'o', 'n'}
# python & dragon






# ============= CHECKING FOR SUBSETS AND SUPERSETS =============
# Check for subsets and supersets definition in "howASetWorks", Example:

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers) # False, because it is a super set
whole_numbers.issuperset(even_numbers) # True

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(dragon.issubset(python))     # False






# ============= CHECKING THE DIFFERENCE BETWEEN TWO SETS =============
# See how sets works
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.difference(st1)) # set() : st2 - st1, because all the elements are in st1
print(st1.difference(st2)) # {'item1', 'item4'} => st1\st2  : st2 - st1






# ============= FINDING SYMMETRIC DIFFERENCE =============
st1 = {"item1","item2","item3","item4"}
st2 = {"item1","item2"}
st1.symmetric_difference(st2) # {"item3", "item4"}, is the opposite of intersection






# ============= JOINING SETS (disjoint) =============
even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # True, because no common item

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)  # False, there are common items {'o', 'n'}