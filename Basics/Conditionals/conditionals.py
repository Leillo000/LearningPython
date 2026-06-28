"""
In this class we will see:

    - If Condition
    - If Else
    - If Elif Else : elif
    - Short Hand : if / else in one line
    - Nested Conditions
    - If Condition and Logical Operators
    - If and Or Logical Operators

Source : https://github.com/Asabeneh/30-Days-Of-Python/blob/master/09_Day_Conditionals/09_conditionals.md

"""

# ============= IF =============
condition = True
if condition:
    print("Hello World!")

value_ = 3

# if variable != null
if value_:
    print("The value is ", value_)




# ============= IF ELSE =============
if condition == False:
    print("Condition is False")
else :
    print("Condition is True")




# ============= ELIF =============
multiply = 10 * 2

if multiply == 21:
    print("The result is 21")
elif multiply == 19:
    print("The result is 19")
else :
    print("The result is", multiply)




# ============= IF ELSE IN ONE LINE =============
a = 1
print("A is zero") if a == 0 else print("A is equal to", a)




# ============= NESTED CONDITIONS =============
a = 0
if a > 0:
    print("A is equal to", a)
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print("Hello")
    print('A is zero')
else:
    print('A is a negative number')




# ============= LOGICAL OPERATORS =============
# AND CASE
a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')
    
# OR CASE
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')

# We don't use || or && for conditionals, we use "or" and "and"
