'''
 Write a Python program to find the largest integer divisor of a number n that is less than n.
 
Input: 18
Output:
9

Input: 6500
Output:
3250
'''

number = int(input("Enter a number : "))
for i in range(number-1,0,-1):
    if number % i == 0:
        print(i)
        break
    
'''


OUTPUT  :

Enter a number : 6500
3250

'''
