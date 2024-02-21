'''
Write a python program to find the factorial of a number using loops 

'''

number = int(input("Enter a number : "))

fact = 1
for i in range(1,number+1):
    fact *=i

print(f"The factorial of {number} is {fact}")


'''
OUTPUT : 

Enter a number : 5
The factorial of 5 is 120


'''