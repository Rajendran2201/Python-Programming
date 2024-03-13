'''
 Implement a Python function named count_vowels that takes a
 string as input and returns the number ofvowels(a,e, i, o, u) in the
 string.

'''

def count_vowels(sentence)->int:
    '''This function takes a string as an input and returns the number of vowels in the string'''
    vowels = ['a','A','e','E','i','I','o','U','u']
    letters = list(sentence)
    count = 0
    for i in letters :
        if i in vowels:
            count += 1
    return count

word = input("Enter a sentence: ")
print("The number of vowels in {} is {}".format(word, count_vowels(word)))


'''
OUTPUT : 

Enter a sentence: rajendran
The number of vowels in rajendran is 3   


Enter a sentence: AbcdEfghijklmnopqrstUvwxyz
The number of vowels in AbcdEfghijklmnopqrstUvwxyz is 5


'''