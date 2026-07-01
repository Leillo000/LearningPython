"""
In today's lesson we will see :

    - While Loop
    - Break and Continue - Part 1
    - For Loop
    - The Range Function
    - Nested For Loop
    - For Else
    - Pass

"""

# ==================== WHILE LOOPS ====================
# While loop syntaxis:

count = 0
while count <= 5:
    print(count)
    count += 1
    
# This execute just once

else :
    print(count)

# I already know what loops are, so i skip the description






# ==================== BREAK AND CONTINUE - PART 1====================
# Break : we use break when we like to get out of or stop the loop

count = 0
while count <= 5:
    print(count)
    count += 1
    if count == 3:
        break # We use break to get out of the loop

# Continue : Skips the current iteration, and continue with the next

count = 0
while count <=5:
    if count == 3:
        count += 1
        continue
    print(count)
    count += 1

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')








# ==================== FOR LOOPS ====================
# We can use for loops over sequences as lists, a tuple, a dictionary or a string
# Iterates item by item

# Example 
lst = [1, 2, 3, 4, 5]
# We don't need to name item "item", we can called it like book, person, etc.
for item in lst:
    print(item, "Belongs to lst")
    
fruits = ["banana", "apple", "pineapple"]
for fruit in fruits:
    print(fruit, "Belongs to fruits")

dct_person = {"first_name" : "Leilo00",
        "last_name" : "Fernández",
        "major" : "programming" 
        }

for keys, values in dct_person.items():
    print(keys) # Keys
    print(values) # Values

print(dct_person.items())

tpl_grocery = ("bottle of water", "pill", "medicine")

for item in tpl_grocery:
    print(item)

word = "Hello Python!"

for letter in word:
    print(letter)






# ==================== RANGE FUNCTION ====================
# The range function can take 3 parameters: range(start, end, step)

lst_ = list(range(11)) # By default it starts from 0 and the increment is 1 by step
print(lst_)

tpl_ = tuple(range(1, 11))
print(tpl_)

st_ = set(range(1, 10, 2))
print(st_)

lst_2 = list(range(11, 0, -1)) 
#  Produces a range reversed, if Start > Index, we have to specify
#  The step in negative number
print(lst_2)

lst_3 = list(range(5, 0, -2)) # It starts with five and decrease 2 by step, until reaching 0
print(lst_3)

for number in range(11):
    print(number) # It starts with 0, and ends with 10
    





# ==================== NESTED FOR LOOPS ====================

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)
    




# ==================== PASS ====================
# If we still don't know what to put in our for we can use pass to avoid any error

for number in range(11):
    pass

"""
for number in range(11):

Expected intended block

"""