'''

Implement the formula for the nth Fibonacci number using the closed-form expression involving the golden ratio.
 
'''

import math

# fibonacci series : 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377

n = int(input("Enter the nth number : "))
res = (1 / math.sqrt(5)) * (((1 + math.sqrt(5)) / 2) ** n - ((1 - math.sqrt(5)) / 2) ** n)

print(int(res))

'''
OUTPUT : 

Enter the nth number : 12
144

'''
