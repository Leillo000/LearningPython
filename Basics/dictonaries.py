"""
A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.

    - Creating a Dictionary : {}
    - Dictionary Length : len()
    - Accessing Dictionary Items (and checking if a value exists) : ["key1"][1], .get("keyname")
    - Adding Items to a Dictionary : dic[new_key] = new_value
    - Modifying Items in a Dictionary : dic[key] = new_value
    - Checking Keys in a Dictionary : in
    - Removing Key and Value Pairs from a Dictionary : .pop(key), .popitem(), del
    - Changing Dictionary to a List of Items : .items() -> key pairs with values
    - Clearing a Dictionary : .clear()
    - Deleting a Dictionary : del
    - Copy a Dictionary : .copy()
    - Getting Dictionary Keys as a List : .keys() -> only keys
    - Getting Dictionary Values as a List : .values() -> only values
    - Create a dictionary with association or a copy : dict.fromkeys()

Source: https://github.com/Asabeneh/30-Days-Of-Python/blob/master/08_Day_Dictionaries/08_dictionaries.md

"""

# ============= CREATING EMPTY DICTONARIES =============
empty_dictonary = {}
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }





# ============= DICTIONARY LENGTH =============
print(len(person))




# ============= ACCESING DICTIONARY ITEMS =============
print(person["skills"][1]) # We access through keys. The index after the key is the index of a list in a dictionary
print(person["address"]["street"]) # It works the same as the before case

# Check if a value exist with a key, in the case that we don't want to check manually
print(person.get("city")) # None
print(person.get("skills")) # Verify if the value exists






# ============= ADDING ITEMS TO A DICTIONARY =============
# We declare a "variable" or a key using dictonary_name["new_key"] = "new_value"
person["job_tittle"] = "Instructor"
# Practically person["skills"] it's a list, so we can use .append()
person["skills"].append("CSS") # Because it's a list in a dictionary
# It's a dictionary in a dictionary, so it's the same logic
person["address"]["avenue"] = "Florida" # Because it's a dictionary in a dictionary
print(person)






# ============= MODIFYIING ITEMS IN A DICTIONARY =============
# We can modify our dictionary:
person["first_name"] = "Leillo0000"
print(person["first_name"])






# ============= CHECKING KEYS IN DICTiONARY =============
# As we do in strings, lists, tuples and sets, we can check if a value exists with "in"
# In this case, we check if a key exists inside the dictionary
print("Does skill key exists in person?","skill" in person) # True, key "skill" exists in person
print("Does second_name key exists in person?","second_name" in person) # False, it doesn't exist second_name key in person






# ============= REMOVING KEY AND VALUE PAIRS FROM A DICTIONARY =============
# As we do in lists, we can use .pop() method
print(person.pop("job_tittle"), "this is the item that will be eliminated")
print(person)
# Delete a key completly
del person["address"]["avenue"] # removes adress { avenue }
print("I removed the address { avenue } in the dictionary")


# Delete the last item of the dictionary
print(person.popitem(), "this is the last item in person dictionary")
print(person)





# ============= CHANGIND DICTONARY TO A LIST OF TUPLES =============
new_list = person.items()
print(type(new_list))
print(new_list) # It prints a list of tuples
# If we really want that our list or items or tuples it really be a list, we have to use the constructor list()






# ============= CLEARING A DICTIONARY =============
print(person.clear())






# ============= DELETING A DICTIONARY =============
del person






# ============= COPYING A DICTIONARY =============
new_dct = {"key1" : "item1","key2" : "item2","key3" : "item3"}
new_dct_2 = new_dct.copy() # We can copy a dictionary like this






# ============= GETTING DICTIONARY KEYS AS A LIST ==============
list_keys = list(new_dct.keys())
print(type(new_dct.keys()))
print(type(list_keys))
print(list_keys)





# ============= GETTING DICTIONARY VALUES AS A LIST =============
list_values = list(new_dct.values())
print(type(new_dct.values()))
print(type(list_values))
print(list_values)




# ============= CREATING A NEW DICTIONARY OR A COPY =============
# This is made with purpose for visualize what .fromkeys() really do.
my_new_dict = dict.fromkeys(["name", "age"], ["Leillo", 45])
print(my_new_dict)
my_new_dict_1 = dict.fromkeys("age", 1)
print(my_new_dict_1)
my_new_dict_2 = dict.fromkeys(["age"], 1)
print(my_new_dict_2)
my_new_dict_3 = dict.fromkeys(new_dct)
print(my_new_dict_3) 