'''
Write a python program to print a diamond pattern

'''

count = int(input("Enter the number of rows : "))
n = int(count/2)

for i in range(n):
    print(" "*(n-i+1), "*"*(i*2+1))

for i in range(n, -1, -1):
    print(" "*(n-i+1), "*"*(i*2+1))


'''

OUTPUT - 1 : 

Enter the number of rows : 3

   *
  ***
   *

OUTPUT - 2  :

Enter the number of rows : 5

    *
   ***
  *****
   ***
    *
'''
