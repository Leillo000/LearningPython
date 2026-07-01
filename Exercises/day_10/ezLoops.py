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


