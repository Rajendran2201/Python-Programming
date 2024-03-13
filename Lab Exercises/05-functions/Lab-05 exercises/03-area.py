'''
 Write a Python function called calculate_area that takes the radius
 of a circle as input and returns its area. Use the formula: area = π*
 radius^2

'''
import math

def caculate_area(radius)->float:
    '''This function takes radius as input and returns the area of the circle'''
    area = math.pi * (radius**radius)
    return area

radius = float(input("Enter the radius : "))
area = caculate_area(radius)
print("The area of the circle of radius {} is {}".format(radius, area))



'''
OUTPUT :

Enter the radius : 3
The area of the circle of radius 3.0 is 84.82300164692441

'''