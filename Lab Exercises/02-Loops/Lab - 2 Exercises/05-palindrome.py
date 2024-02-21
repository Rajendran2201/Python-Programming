'''
Write a python program to check if the gievn word is a palindrome or not

'''
def checkPalindrome(word1):
    word2 = word1[::-1] 
    for i in range(0,len(word1)):
        if word1[i] != word2[i]:
            return 0
    return 1


word1 = input("Enter a string : ")
isPalindrome = checkPalindrome(word1)


if isPalindrome == 0:
    print(f"{word1} is not a palindrome")
else:
     print(f"{word1} is  a palindrome")


'''
OUTPUT - 1 : 

Enter a string : raj
raj is not a palindrome

OUTPUT - 2 :

Enter a string : malayalam
malayalam is  a palindrome

'''
