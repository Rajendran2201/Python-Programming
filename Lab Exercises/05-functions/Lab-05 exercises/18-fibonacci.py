'''
 Implement a Python function to find the nth Fibonacci number
 using recursion

'''

def fibo(n)->int:
    '''This function takes an integer (n) as an input and find the nth  number in the fibonacci series'''
    if n == 1 :
        return 0
    if n == 2:
        return 1
    return fibo(n-1) + fibo(n-2)

n = int(input("Enter the value of n : "))
print("The {}th number in the fibonacci series is {}".format(n, fibo(n)))


'''
OUTPUT: 

Enter the value of n : 5
The 5th number in the fibonacci series is 3

'''