"""
Class: https://github.com/Asabeneh/30-Days-Of-Python/blob/master/03_Day_Operators/03_operators.md

"""

age : int = 22
height : float = 1.65
complex_number : complex = 1j

base : float = float(input("Enter the base of a triangle: "))
height : float = float(input("Enter t1he height of a triangle: "))
print("The area of the triangle is:", (base * height) / 2)

side_a : float = float(input("Enter the lenght of the first side of the triangle: "))
side_b : float = float(input("Enter the lenght of the second side of the triangle: "))
side_c : float = float(input("Enter the lenght of the third side of the triangle: "))

print(side_a + side_b + side_c)

rectangle_length : float = float(input("Enter the lenght of a rectangle: "))
rectangle_width : float = float(input("Enter the width of a rectangle: "))

print("The perimeter of the rectangle is:", 2 * (rectangle_width + rectangle_length))
print("The area of the rectangle is:", rectangle_length * rectangle_width)

radius_circle : float = float(input("Enter the radius of a circle: "))
area_circle = radius_circle ** 2 * 3.14
perimeter_circle = radius_circle * 2 * 3.14

# Calculate the slop of 2x - 2, X-intercept and y-intercept

slope : int = 2
y_intercept : int = 2
x_intercept : int = 2

# Calculate the slope in points (2,2) and (6,10)

x_1 : int = 2
x_2 : int = 6
y_1 : int = 2
y_2 : int = 10

slope_points = (y_2 - y_1) / (x_1 - x_2)
print(slope_points)

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x : float = float(input("Enter the X value for squared function:"))
result = x ** 2 + 6 * x + 9
print(result)

python_length : int = len("python")
dragon_length : int = len("dragon")
print(python_length == dragon_length)
print("on" in "python" and "on" in "dragon")
print("jargon" in "I hope this course is not full of jargon")

number_test = 2
# Check if a number is even using Python
is_number_even : bool = number_test % (python_length / 3) == 0

print(7 // 3 == int(2.7)) # Output: True, 7 // 3 = 2, and int(2.7) is 2
print(type('10') == type(10)) # Output: False
print(int(9.8) == 10) # Output: False

hours : int = int(input("Enter the hours that you work weekly: "))
rate_per_hour : int = int(input("Enter your rate per hour: "))
print("Your weekly earning is:", hours * rate_per_hour)