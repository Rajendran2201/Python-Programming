'''

Write a python program to find the sum of natural numbers upto n 

'''

n = int(input("Enter a number : "))
sum = 0
for i in range(1,n+1):
    sum += i

print(f"The sum of natural numbers from 1 to {n} is {sum}")

'''
OUTPUT : 

Enter a number : 10
The sum of natural numbers from 1 to 10 is 55

'''