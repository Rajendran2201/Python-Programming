'''
 Write a Python program to check whether agiven numberispositive or negative.

'''


num = int(input("Enter a number : "))

if num>0:
    print(f"{num} is a positive number")
elif num<0: 
     print(f"{num} is a negative number")
else: 
     print("The input was zero")


'''

OUTPUT : 

Enter a number : -87
-87 is a negative number

'''