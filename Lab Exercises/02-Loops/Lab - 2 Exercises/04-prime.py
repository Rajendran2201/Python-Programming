'''
Develop a python program that prompts the user to give a number and tells whether the number is prime or not 

'''
import math

number = int(input("Enter a number : "))

isPrime = 1
for i in range(2,int(math.sqrt(number))+1):
    if number%i==0:
        isPrime = 0

if isPrime==0:
    print(f"{number} is not a prime number")
else:
    print(f"{number} is  a prime number")


'''

OUTPUT : 

Enter a number : 13
13 is  a prime number

'''