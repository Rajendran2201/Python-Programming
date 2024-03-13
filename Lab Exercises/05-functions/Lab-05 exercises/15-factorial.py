'''
Write a Python function to calculate the factorial of a non-negative
 integer using recursion.

'''

def calculate_factorial(n)->int:
    '''This function takes a positive integer as an input and returns the factorial of the number'''
    if n < 2:
        return 1
    return n * calculate_factorial(n-1)

n = int(input("Enter a number : "))
print("The factorial of {} is {}".format(n, calculate_factorial(n)))


'''
OUTPUT : 

Enter a number : 10
The factorial of 10 is 3628800

'''