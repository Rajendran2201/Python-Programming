'''
 Implement a Pythonfunction to reverse a string

'''

def reverse_string(word)->str:
    '''This function takes a string as an input and returns the reverse of the string'''
    return word[::-1]

word = input("Enter a word : ")
print("The reverse of {} is {}".format(word, reverse_string(word)))


'''

OUTPUT : 

Enter a word : rajendran
The reverse of rajendran is nardnejar


'''