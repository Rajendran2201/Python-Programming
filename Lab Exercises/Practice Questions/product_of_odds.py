'''

Write a Python program to compute the product of the odd digits in a given number, or 0 if there aren't any.


Input: 123456789
Output:
945
Input: 2468
Output:
0
Input: 13579
Output:
945

'''

def find_product(number)->int:
    product = 1
    isOne = False
    while(number>0) :
        rem = int(number%10)
        if rem%2 != 0:
            if rem == 1:
                isOne = True
            product *= rem
        number /= 10
    if isOne == True or product > 1:
        return product
    return 0
    

number = int(input("Enter a number : "))
product = find_product(number)
print(product)



'''

OUTPUT - 1 : 

Enter a number : 123456789
945


OUTPUT - 2 : 

Enter a number : 2468
0


'''
