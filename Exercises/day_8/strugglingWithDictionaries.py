#1
dog = {}
#2
dog["name"] = "Pepe"
dog["color"] = "white"
dog["breed"] = "Maltez"
dog["legs"] = 20.1
dog["age"] = 40
#3
student = {}
student["first_name"] = "Leillo"
student["last_name"] = "Fernández"
student["gender"] = "male"
student["age"] = 32
student["marital_status"] = "married"
student["skills"] = ["JavaScript", "C#", "CSS", "HTML", "Python" , "SQL", "NoSQL"]
student["country"] = "Mexico"
student["city"] = "Mexico City"
student["address"] = {
    "street" : "Carmona",
    "avenue" : "Av. Prolongación de Independencia",
    "zipcode" : "3003"
}

print(student)
#4
print(len(student))
#5
print(type(student["skills"]))
#6
student["skills"].append("Firebase")
student["skills"].append("Mongo Atlas")
#7
student_keys = student.keys()
print(student_keys)
#8
student_values = student.values()
print(student_values)
#9
student_list_form = student.items()
print(student_list_form)
#10
del student["marital_status"]
print(student)
#11
del dog 
