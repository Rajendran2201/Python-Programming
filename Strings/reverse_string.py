'''Create a function to reverse a string'''

def reverse(word1) -> str:
    '''This function takes a string as an input and returns the reverse of the string'''
    return word1[::-1]


word1 = input("Enter string-1 : ")
print(reverse(word1))


'''

OUTPUT : 

Enter string-1 : Rajendran
nardnejaR

'''
