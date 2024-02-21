'''

Write a python function which can take a number as an input and print its multiplication table  

'''
def multiply(n)->None:
    for i in range(11):
        print(f"{n} * {i} = {n*i}")

n = int(input("Enter the number : "))
multiply(n)

'''

OUTPUT : 

Enter the number : 6
6 * 0 = 0
6 * 1 = 6
6 * 2 = 12
6 * 3 = 18
6 * 4 = 24
6 * 5 = 30
6 * 6 = 36
6 * 7 = 42
6 * 8 = 48
6 * 9 = 54
6 * 10 = 60

'''