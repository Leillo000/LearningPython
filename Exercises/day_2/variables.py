# Day 2: 30 Days of python programming
# Class : https://github.com/Asabeneh/30-Days-Of-Python/blob/master/02_Day_Variables_builtin_functions/02_variables_builtin_functions.md

first_name : str = "González"
last_name : str = "Leo"
full_name : str = first_name + " " + last_name
country : str = "Mexico"
city : str = "Monterrey"
age : int = 21
year : int = 2026
is_married : bool = False
is_true : bool = True
is_light_on : bool = True 
# Never do this
first_variable, second_variable, third_variable = "Today ", 2026, True

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(first_variable))
print(type(second_variable))
print(type(third_variable))

num_one : int = 5
num_two : int = 4 
radius : int = 30
num_three : int = num_one + num_two
num_division = num_one / num_two
num_diff = num_one - num_two
num_product = num_one * num_two
num_modulus = num_two % num_one
num_power = num_one ** num_two
floor_division = num_one // num_two
area_of_circle = 3.1416 * (radius ** 2)
circum_of_circle = 3.1416 * (radius * 2)

radius : int = int(input("Enter the radius of a circle: "))
area_of_circle = 3.1416 * (radius ** 2)
print(area_of_circle)
