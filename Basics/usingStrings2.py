"""

In this file you will find:
    
    - Ends and Starts with
    - Reversing Strings easily
    - Capitalizing and tittling strings easily 
    - Find Substrings
    - Expand tabs
    - Skipping characters while slicing
    - Checking if it's alphanumeric, alphabetic and decimal
    - Check if all alphabet characters are uppercase or lowercase
    - Replacing()
    - Split() -> 
    - Join() -> Concatenation
    - Transform lowercase -> uppercase and vice versa (Swapcase)
    - Strip() -> Removes all given characters
    - Unpacking strings

Source:
https://github.com/Asabeneh/30-Days-Of-Python/blob/master/04_Day_Strings/04_strings.md

"""

expanded_tabs = "Day\tSalary\tHours"
challenge = 'thirty days of python'

# .count(substring, start, end)
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1

# To find a substring

print(challenge.find("y")) # Find the first 'y' in the string
print(challenge.rfind("y")) # Find the last 'y' in the string

print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False
print(challenge.startswith('th')) # True
print(challenge.startswith('Th')) # False

print(expanded_tabs.expandtabs())
print(expanded_tabs.expandtabs(10)) # Default tab size is 8

# Reversing strings

# This is a way
reversed_word : str = "Hello"[::-1]

# This is another way
reversed_word_2 : str = reversed_word[::-1] 

print(reversed_word) # Output : olleH
print(reversed_word_2)# Output : Hello

# Capitalize and tittling strings

lower_case : str = "i'm bored"
upper_case : str = lower_case.capitalize() # I'm bored
print(upper_case)
print(lower_case.capitalize())
print(lower_case.title()) # I'm Bored

# Skipping characters while slicing
# n is defined as: "skip a character each n number of position"
# string_to_indexing[start (included) : end (excluded) : n]

# substring -> position 
# =======================================
# P     |   -> 0 |  It's included       |
# y     |   -> 1 |                      |
# t     |   -> 2 |  It's included       | 
# h     |   -> 3 |                      |
# o     |   -> 4 |  It's included       | 
# n     |   -> 5 |                      |
# None  |   -> 6 |  (not included)      |
# # =====================================

language = "Python"
print(language[0:6:2]) # Output : Pto


# Check if it's alphanumeric

challenge = '30DaysPython'
print(challenge.isalnum()) # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False, space is not an alphanumeric character


# Check if it's alphabetic

print("123".isalpha()) # False, it contains numbers

# Check if it's decimal

print("123".isdecimal()) # True, they are numbers

# Check if it's a digit

print("19.2".isdigit()) # False, points aren't allowed

# Check for lowercase and uppercase

print("HELLO".islower()) # False
print("HELLO".isupper()) # True
print("hello".islower()) # True
print("hello".isupper()) # False

# Uppercase -> Lowercase and vice versa
# string.swapcase()

print("Hello".swapcase()) # hELLO
print("HELLO".swapcase()) # hello
print("hELLO".swapcase()) # Hello
print("hello".upper()) # HELLO
print("HELLO".lower()) # hello

# string.join()
# if it isn't an array, python automatically transform it into an array


web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # HTML CSS JavaScript React, it doesn't apply to the first element as you can see, there's no space before 'HTML'
print(web_tech) # ['HTML', 'CSS', 'JavaScript', 'React']



# string.replace(substring_to_replace , replacing_substring)
# challenge = thirty days of python

print(challenge.replace('python', 'coding')) # 'thirty days of coding'

# string.split(",") 
# Splits the string, using given string or space as a separator

print(challenge.split()) # ['thirty', 'days', 'of', 'python'] Separates using space as default

challenge = "thirty, days, of, python"
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python'] Separates using coma with space ", "

# We can unpacking characters, but the number of variables have to equal to the number of characters in a string

language : str = "Python"

a, b, c, d, e, f = language

# I can't define a, b = language, because Python have 6 characters
# So that, a = P, b = y, c = t ...

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# How index works

challenge = "Hola da da da"
substring_challenge : str = "da"
print(challenge.index(substring_challenge))
print(challenge.rindex(substring_challenge))