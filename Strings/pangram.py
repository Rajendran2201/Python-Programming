'''Write a python program to check is a string is pangram or not'''

def check_pangram(word1) -> bool:
    '''This function takes a string as an input and returns the uoupt as a boolean value. It evaluates whether the given string is a pangram or not. Pangram is a string in which all the alphabets are present'''
    
    word1 = word1.lower()
    alphabets = 'abcdefghijklmnopqrstvwxyz'
    for character in alphabets : 
        if character not in word1: 
            return False
    return True


word1 = input("Enter a string : ")
isPangram = check_pangram(word1)
print("It is a pangram") if isPangram == True else print("It is not a pangram")

'''

OUTPUT - 1 : 

Enter a string : The quick brown fox jumps over the lazy dog
It is a pangram

OUTPUT - 2 : 

Enter a string : rajendran
It is not a pangram

'''
