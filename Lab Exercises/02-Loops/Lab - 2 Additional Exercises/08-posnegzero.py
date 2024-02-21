'''

Write a python program to get an input from the user and determine whether it is positive, neagtive or zero until the user gives a specific value 

'''


while(1):
    print("Enter -1 to quit")
    n = int(input("Enter a number : "))
    if(n==-1):
        print("The program ends!")
        break
    elif n>0:
        print("Positive number")
    elif n<0:
        print("Negative number")
    else:
        print("Zero")

'''
OUTPUT : 


Enter -1 to quit
Enter a number : 4
Positive number
Enter -1 to quit
Enter a number : -8
Negative number
Enter -1 to quit
Enter a number : 0
Zero
Enter -1 to quit
Enter a number : 45
Positive number
Enter -1 to quit
Enter a number : -1
The program ends!


'''