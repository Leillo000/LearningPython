"""

Source: https://github.com/Asabeneh/30-Days-Of-Python/blob/master/09_Day_Conditionals/09_conditionals.md

"""

#1 
age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to learn to drive")
else:
    print("You need", 18 - age, "more years to learn to drive")

#2
my_age = int(input("Enter your age: "))
your_age = 25

if my_age == your_age + 1:
    print("You are 1 year older than me")
elif my_age == your_age - 1:
    print("You are 1 year younger than me")
elif my_age > your_age:
    print("You are", my_age - your_age, "years older than me")
elif my_age < your_age:
    print("You are", your_age - my_age, "years younger than me")
else:
    print("We are the same age")
    
#3
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print(a, "is greater than", b)
elif a < b:
    print(a, "is smaller than", b)
else:
    print(a, "is equal to", b)


