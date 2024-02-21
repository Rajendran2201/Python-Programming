'''
Create a python function that takes a number as an input and returbs the sum of its digits 

'''
def sumOfDigits(number):
    sum = 0
    while number>0:
        rem = number%10
        sum += int(rem)
        number /= 10
    return sum


number = int(input("Enter a number : "))
sum = sumOfDigits(number)
print(f"The sum of the digits of {number} is {sum}")

'''
OUTPUT : 

Enter a number : 234
The sum of the digits of 234 is 9

'''