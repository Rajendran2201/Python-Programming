'''

Write a Python program to accept a coordinate point in a XY coordinate
 system and determine in which quadrant the coordinate point lies. 

'''


x_coordinate = int(input("Enter the X_Co-ordinate : "))
y_coordinate = int(input("Enter the Y_Co-ordinate : "))


if x_coordinate==0 and y_coordinate==0:
    print("The point lies in the origin")
elif x_coordinate==0 or y_coordinate==0: 
    print("The point lies on the axis")
elif x_coordinate>0 and y_coordinate>0 : 
    print("First Quadrant")
elif x_coordinate<0 and y_coordinate>0: 
    print("Second Quadrant")
elif x_coordinate<0 and y_coordinate<0: 
    print("Third Quadrant")
else : 
    print("Fourth Quadrant")

    

'''

OUTPUT : 

Enter the X_Co-ordinate : 4
Enter the Y_Co-ordinate : -6
Fourth Quadrant

'''
