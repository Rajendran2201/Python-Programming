'''
 Write a Python function to calculate the power of a number using
 recursion.

'''

def find_power(base, power)->int:
    '''This function takes two numbers (base, power) as input and find the the power of the base to the power'''
    if power < 1 :
        return 1
    return base * find_power(base,power-1)

base = int(input("Enter the value of base : "))
exponent = int(input("Enter the value of exponent : "))
print("The power of {} to {} is {}".format(base, exponent, find_power(base, exponent)))


'''
OUTPUT : 

Enter the value of base : 2
Enter the value of exponent : 5
The power of 2 to 5 is 32

'''