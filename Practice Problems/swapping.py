'''Implement a python program to swap the values of two variables'''


a = int(input("Enter number-1 : "))
b = int(input("Enter number-2 : "))

print("Before Swapping : ")
print("Value of a : ", a)
print("Value of b : ", b)

b, a = a, b

print("After Swapping : ")
print("Value of a : ", a)
print("Value of b : ", b)


'''
OUTPUT : 

Enter number-1 : 3
Enter number-2 : 6
Before Swapping : 
Value of a :  3
Value of b :  6
After Swapping : 
Value of a :  6
Value of b :  3

'''
