"""

Class:
https://github.com/Asabeneh/30-Days-Of-Python/blob/master/06_Day_Tuples/06_tuples.md

"""

# 1

my_tuple = ()

# 2 
my_brothers = ("Alejandro", "Maria", "Fernando")
my_sisters = ("Maria", "Fernanda", "Daniela")

# 3
my_siblings = my_brothers + my_sisters

# 4

print("I have", len(my_siblings), "siblings")

# 5

family_members = list(my_siblings)
family_members.append("Eligio")
family_members.append("Juana")

# LEVEL 2 

# 1

family_members_tuple = tuple(family_members)

bro1, bro2, bro3, sis1, sis2, sis3, father, mother = family_members_tuple
print(father)

# 2

fruits = ("Apple", "Pineapple", "Blackberry")
vegetables = ("Lettuce", "Carrot", "Roots")
animal_products = ("Milk", "Butter", "Yogurt")

food_stuff_tp = fruits + vegetables + animal_products
# 3
food_stuff_lst = list(food_stuff_tp)

# 4
# Middle item
print(food_stuff_tp[round(len(food_stuff_tp) / 2)])

# 5
print(food_stuff_lst[:3])
print(food_stuff_lst[-3:])

# 6

del food_stuff_tp

# 7

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print("Estonia" in nordic_countries) # False
print("Iceland" in nordic_countries) # True 