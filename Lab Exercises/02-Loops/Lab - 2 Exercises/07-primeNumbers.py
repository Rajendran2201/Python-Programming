'''
Implement a python program to genrate all the prime number less than a given number 

'''

import math 

def isPrimeNumber(number)->int:
    for i in range(2,int(math.sqrt(number))+1):
        if number%i==0:
            return 0
    return 1    


n = int(input("Enter a number : "))

for i in range(2,n):
    if isPrimeNumber(i) == 1:
        print(i)


'''
OUTPUT : 

Enter a number : 20
2
3
5
7
11
13
17
19

'''