import math

#how to call a function and use embedded variables into a function
def area_of_a_circle(radius):
    area = radius**2*math.pi
    return area
 
radius = float(input("enter the radius of a circle:"))
area = area_of_a_circle(radius)
print('The area of the circle of radius', radius, 'is', area)