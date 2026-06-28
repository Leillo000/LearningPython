
# LEVEL 3

#1
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Mexico',
    'is_married': False,
    'skills': ['JavaScript', 'React'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if "skills" in person:
    print(person["skills"][len(person["skills"]) // 2])
    if "Python" in person["skills"]:
        print("This person has Python in their skills")
else:
    print("This person has no skills")

set_skills = set(person["skills"])

if "Node" in person["skills"] and "Python" in person["skills"] and "MongoDB" in person["skills"]:
    print("He's a backend developer")
    if "Node" in person["skills"] and "React" in person["skills"] and "MongoDB" in person["skills"]:
        print("He's a fullstack developer")
elif set_skills == {"JavaScript", "React"}:
     print("He's a frontend developer")
else:
    print("Unknown tittle")
    
if person["is_married"] and person["country"] == "Finland":
    print(person["first_name"], "lives in", person["country"],". He's married")
elif person["country"] != "Findland" and person["is_married"] == False:
    print(person["first_name"], "lives in", person["country"],". He isn't married")
else:
    print(person["first_name"], "lives in", person["country"],". He is married")
    