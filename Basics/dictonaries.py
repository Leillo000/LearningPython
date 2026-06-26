"""
A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.

    - Creating a Dictionary 
    - Dictionary Length
    - Accessing Dictionary Items (and checking if a value exists) : ["key1"][1], .get("keyname")
    - Adding Items to a Dictionary
    - Modifying Items in a Dictionary
    - Checking Keys in a Dictionary
    - Removing Key and Value Pairs from a Dictionary
    - Changing Dictionary to a List of Items
    - Clearing a Dictionary
    - Deleting a Dictionary
    - Copy a Dictionary
    - Getting Dictionary Keys as a List
    - Getting Dictionary Values as a List

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





# ============= DICTONARY LENGTH =============
print(len(person))




# ============= ACCESING DICTONARY ITEMS =============
print(person["skills"][1]) # We access through keys. The index after the key is the index of a list in a dictonary
print(person["address"]["street"]) # It works the same as the before case

# Check if a value exist with a key, in the case that we don't want to check manually
print(person.get("city")) # None
print(person.get("skills"))






# ============= ADDING ITEMS TO A DICTONARY =============
# We declare a "variable" or a key using dictonary_name["new_key"] = "new_value"
person["job_tittle"] = "Instructor"
# Practically person["skills"] it's a list, so we can use .append()
person["skills"].append("CSS") # Because it's a list in a dictonary
# It's a dictonary in a dictonary, so it's the same logic
person["address"]["avenue"] = "Florida" # Because it's a dictonary in a dictonary
print(person)

