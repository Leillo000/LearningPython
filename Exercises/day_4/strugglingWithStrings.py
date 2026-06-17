"""

This is day 4 with Python

"""

concatenation_1 : str = "Thirty " + "Days " + "Of " + "Python"
company : str = "Coding " + "For " + "All"

print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.swapcase())
print(company.title())

print(company[7:])
print(company.index("Coding"))
print(company.replace("Coding", "Python"))
print("Python For Everyone".replace("Everyone", "All"))
print(company.split(" "))
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(" "))
print(company[0]) # C

# The last index of Coding for All

print(len(company) - 1)

# Character at position 10

print(company[10]) # The character at 10 position

# Create an acronym or an abbreviation for Python For Everyone

acroym : str = "Python For Everyone".split(" ")
new_acronym  : str = ""

for i in range(0, len(acroym)):
    word = acroym[i]
    new_acronym += word[0] # Just append the first letter of each word

print(new_acronym)

# For Coding For All, i skipped some topics ok

acroym = "Coding For All".split(" ")
new_acronym = ""

for i in range(0, len(acroym)):
    word = acroym[i]
    new_acronym += word[0].upper() # Just append the first letter of each word, upper if it's not

print(new_acronym)

phrase : str = "Coding For All"

print(phrase.index("C"))
print(phrase.index("F"))
print(phrase.rfind("L"))
print("You cannot end a sentence with \"because\" because is a conjunction".index("because"))
print("You cannot end a sentence with \"because\" because is a conjunction".rindex("because"))
phrase_2 = "You cannot end a sentence with because because because is a conjunction"
print(phrase_2.replace("because ", ""))


print(phrase.startswith("Coding")) # True
print(phrase.startswith("coding")) # False
print("   Coding For All      ".strip(" ")) # Without spaces, deletes given characters and the end and at the start of a string

# Check for right names of variables

print("30DaysOfPython".isidentifier()) # False 
print("thirty_days_of_python".isidentifier()) # True

libraries : str = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']

libraries = " #".join(libraries)
print(libraries)

print("I am enjoying this challenge. \nI just wonder what is next.")

print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki".expandtabs(10))

# Use the string formatting methosto display the following

radius : float = 10.0
area : float = 3.14 * radius ** 2

# I prefer this method because i restrict the type of each variable
print("The area of a circle with radius %.1f is %.2f meters square"%(radius, area))

a : int = 8
b : int = 6

print("%d + %d = %d"%(a, b, a + b))
print("%d - %d = %d"%(a, b, a - b))
print("%d * %d = %d"%(a, b, a * b))
print("%d / %d = %.2f"%(a, b, a / b))
print(f"{a} % {b} = {a % b}")
print("%d // %d = %d"%(a, b, a // b))
print("%d ** %d = %d"%(a, b, a ** b))
