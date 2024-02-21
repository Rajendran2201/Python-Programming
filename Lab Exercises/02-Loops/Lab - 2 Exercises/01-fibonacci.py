'''


 Write a python program to print the fibonacci series upto a specified number of terms using a loop 

 
'''

n = int(input("Enter the number of terms: "))

first, second = 0, 1

if n >= 1:
    print(first)
if n >= 2:
    print(second)

for i in range(2, n):
    next = first + second
    print(next)
    first, second = second, next



'''
OUTPUT : 

Enter the number of terms : 10
0
1
1
2
3
5
8
13
21
34
55

'''