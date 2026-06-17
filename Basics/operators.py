"""

These are all the operators we can use in Python.
I'll only type the operators i hadn't seen before.
The class i've taken today:
https://github.com/Asabeneh/30-Days-Of-Python/blob/master/03_Day_Operators/03_operators.md


"""

# I won't type "is" and "is not" conditions because they throw an advertation.
# Better use "==" or "!="

print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B not in Asabeneh', 'B' in 'Asabeneh') # False - there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

# We can do comparisions in prints

print(3 > 2) # True
print( 3 == 2 ) # False
print( 10 >= 20 ) # False
print( 10 != 20) #True

# We use and instead of &&, and or instead of ||

print(3 > 2 and 4 > 3) # True
print(3 > 2 or 4 > 3) # True
print(not(3 > 2)) # False, reverses true to false and vice versa

print("aaaa" >= "aaaa")
print("aaaa" > "abaa") # It's comparing an alphabetic sorter
print("aaaa" == "abaa") # The value of a string is less if the letters are first on the alphabet
print("aaaa" != "aaca") 
print("b" > "a") # True
print("c" > "d") # False
print("A" == "a") # False
print("a" == "a") # True, this is the only wich compares the string directly
# Z = Greater value = 27 for example
# A = Lowest value = 1 for example
