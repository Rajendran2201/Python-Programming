'''
Implement a python program to determine whether the given number is an armstrong number or not 

'''

number = int(input("Enter a number : "))
dup1 = number
dup2 = number 

# counting the number of digits 
snumber = str(number)
count = len(snumber)


# finding the computation
sum = 0
while dup2>0:
    rem = dup2%10
    sum += rem**count
    dup2 = int(dup2/10)

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