'''
Create a python program to print the followiing pattern: 

*
**
***
****

'''

n = int(input("Enter the number of rows : "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print("\n",end="")


'''
OUTPUT : 

Enter the number of rows : 5
*
**
***
****
*****

'''