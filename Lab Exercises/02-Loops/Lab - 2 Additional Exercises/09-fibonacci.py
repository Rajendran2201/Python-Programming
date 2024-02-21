'''


 Write a python program to print the fibonacci series upto a specified number of terms using a loop 

 
'''

first = 0
second = 1

n = int(input("Enter the number of terms : "))

if n==0:
    pass
elif n == 1:
    print(first)
else:
    print(first)
    print(second)

i = 2

while i<n: 
    next = first+second
    print(next)
    first = second
    second = next
    i+=1



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