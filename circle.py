import math


def circumference(radius):
	return 2 * math.pi * radius
def area(radius):
	return math.pi * radius ** 2

radius = float(input("Enter the radius: "))
print(f"Circumference: {circumference(radius)}")
print(f"Area: {area(radius)}")	
