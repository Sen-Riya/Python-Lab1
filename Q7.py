# (7) Write a program to find the area of a triangle. Then find the area of two arbitrary triangles by entering the three sides both using the input function (input()). 
# Print the total area enclosed by both triangles and each triangle’s contribution (%) towards it.
# Hint: area of a triangle:
# A = squareroot{s(s − a)(s − b)(s − c)}          s = (a + b + c)/ 2

import math

def calculate_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def triangle_sides():
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    c = float(input("Enter the length of side c: "))
    return a, b, c


print("Enter the sides of the first triangle:")
a1, b1, c1 = triangle_sides()

print("Enter the sides of the second triangle:")
a2, b2, c2 = triangle_sides()

area1 = calculate_area(a1, b1, c1)
area2 = calculate_area(a2, b2, c2)

total_area = area1 + area2

percentage_of_1 = (area1 / total_area) * 100
percentage_of_2 = (area2 / total_area) * 100

print(f"Area of the first triangle: {area1:.2f}")
print(f"Area of the second triangle: {area2:.2f}")
print(f"Total area enclosed by both triangles: {total_area:.2f}")
print(f"First triangle's contribution to the total area: {percentage_of_1:.2f}%")
print(f"Second triangle's contribution to the total area: {percentage_of_2:.2f}%")
