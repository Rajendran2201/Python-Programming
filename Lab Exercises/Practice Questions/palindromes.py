'''

Write a Python program to check whether the given strings are palindromes or not. Return True otherwise False.
Input:
['palindrome', 'madamimadam', '', 'foo', 'eyes']

'''
# function to check if the word is a palindrome or not 
def checkPalindrome(word)->bool:
    rev_word = word[::-1]
    for i in range(len(word)):
        if word[i] != rev_word[i]:
            return False
    return True
    

words = []
palindromes = []

print("Enter stop to quit \nEnter the words to check if they are palindrome or not : ")

# getting the input values 
while(1):
    word = input()
    if(word == 'stop'):
        break
    words.append(word)


# checking if each word is a palindrome or not 
for i in words : 
    isPalindrome = checkPalindrome(i)
    if isPalindrome: 
        palindromes.append(True)
    else:
        palindromes.append(False)
print(words)
print(palindromes)
        

'''

OUTPUT : 

Enter stop to quit 
Enter the words to check if they are palindrome or not : 
viks
lenin
pip
key
passap
stop
['viks', 'lenin', 'pip', 'key', 'passap']
[False, False, True, False, True]


'''
