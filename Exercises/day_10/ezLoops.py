#1
for number in range(0,11):
    print(number)
    
number = 0

while number <=10 :
    print(number)
    number += 1
#2
for number in range(10, -1, -1):
    print(number)
    
number = 10

while number >= 0:
    print(number)
    number -= 1
#3
count = 0
str_hash = ""

for hashtag in range(0,7):
    str_hash += "#"
    for hash_ in range(count):
        str_hash += "#"
    count += 1
    print(str_hash)
    str_hash = ""
#4
str_hash = ""

for rows in range(0,8):
    for columns in range(0,8):
        str_hash += "# "
    if rows != 7:
        str_hash += "\n"
print(str_hash)
#5
for row in range(0 , 11):
    print(row, "X", row, "=", row ** 2)
#6
python_list = ["Python", "Numpy", "Pandas", "Django", "Flask"]
for item in python_list:
    print(item)
#7 and 8
for number in range(1, 101):
    if number % 2 == 0: 
        print(number, "is even number")
    else:
        print(number, "is odd number")