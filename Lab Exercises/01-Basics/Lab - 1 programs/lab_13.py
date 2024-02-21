
'''
 Write a Python program to check whether a triangle can be formed by the
 given value for the angles.
 Test Data :
 40 55 65
 Expected Output :
 Thetriangle is not valid

'''


angle_1 = int(input("Enter the angle-1 : "))
angle_2 = int(input("Enter the angle-2 : "))
angle_3 = int(input("Enter the angle-3 : "))

total_angle = angle_1+angle_2+angle_3 

if total_angle==180: 
    print("The triangle is valid")
else: 
     print("The triangle is not valid")





'''
OUTPUT : 


Enter the angle-1 : 60
Enter the angle-2 : 40
Enter the angle-3 : 100
The triangle is not valid


'''