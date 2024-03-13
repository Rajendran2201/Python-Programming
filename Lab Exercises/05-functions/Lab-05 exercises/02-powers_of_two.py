'''

 Write a Python function named print_power_of_two that takes an
 integer n as input and prints the first n powers of 2 without
 returning anything.

'''


def print_power_of_two(n)->None:
    '''This function takes an integer 'n' as an input and print the powers of 2 till n '''
    num = 2
    for i in range(1,n+1):
        print("{} ^ {} = {}".format(num, i, num**i))

n = int(input("Enter a number : "))
print_power_of_two(n)



'''
OUTPUT :

Enter a number : 10
2 ^ 1 = 2
2 ^ 2 = 4
2 ^ 3 = 8
2 ^ 4 = 16
2 ^ 5 = 32
2 ^ 6 = 64
2 ^ 7 = 128
2 ^ 8 = 256
2 ^ 9 = 512
2 ^ 10 = 1024

'''