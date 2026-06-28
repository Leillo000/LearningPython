
# EXERCISES LEVEL 2

#1

grade = int(input("Enter your grade: "))

if grade >= 0 and grade <= 59:
    print("You got a F")
elif grade >= 60 and grade <= 69:
    print("You got a D")
elif grade >= 70 and grade <= 79:
    print("You got a C")
elif grade >= 80 and grade <= 89:
    print("You got a B")
elif grade >= 90 and grade <= 100:
    print("You got a A")

#2

months_seasons = {
    "september" : "Autum",
    "october" : "Autum",
    "november" : "Autum",
    "december" : "Winter",
    "january" : "Winter",
    "february" : "Winter",
    "march" : "Spring",
    "april" : "Spring",
    "may" : "Spring",
    "june" : "Summer",
    "july" : "Summer",
    "august" : "Summer"
}

month_selected = input("Enter the month that you want know its season: ").lower()
if month_selected in months_seasons:
    print("The season in", month_selected.capitalize() , "it's", months_seasons[month_selected])
else: 
    print("Select a valid month")

#3
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit_ = input("Enter a fruit to add: ").lower()

if fruit_ in fruits:
    print("That fruit already exists")
else:
    fruits.append(fruit_)
    print("The list changed: ", fruits)

    