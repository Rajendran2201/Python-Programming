'''
Implement a python program to determine whether the given number is an armstrong number or not 

'''

number = int(input("Enter a number : "))
duplicate = number 

# counting the number of digits 
snumber = str(number)
count = len(snumber)


# finding the computation
sum = 0
while duplicate>0:
    rem = duplicate%10
    sum += rem**count
    duplicate = int(duplicate/10)

# Evaluating the condition 
    
if sum == number:
    print(f"{number} is an Armstrong number")
else:
    print(f"{number} is not an Armstrong number")

'''
OUTPUT : 

Enter a number : 1634
1634 is an Armstrong number

'''
