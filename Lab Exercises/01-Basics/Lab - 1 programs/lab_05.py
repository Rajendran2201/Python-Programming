'''
 Write a Python program to find the largest of three numbers.

'''


num1 = int(input("Enter the number-1 : "))
num2 = int(input("Enter the number-2 : "))
num3 = int(input("Enter the number-3 : "))

if num1>num2 and num1>num3 : 
    print(f"{num1} is the greatest of {num1},{num2} and {num3}")
elif num2>num1 and num2>num3:
    print(f"{num2} is the greatest of {num1},{num2} and {num3}")
else: 
    print(f"{num3} is the greatest of {num1},{num2} and {num3}")



'''

OUTPUT : 

Enter the number-1 : 4
Enter the number-2 : 6
Enter the number-3 : 7
7 is the greatest of 4,6 and 7


'''