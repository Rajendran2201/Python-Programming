'''Create a python program that takes a sentence and counts the number of words in it'''

sentence = input("Enter a sentence : ")
my_list = list(sentence.split())
print("The number of words in the sentence is ",len(my_list))

'''

OUTPUT : 

Enter a sentence : This is a sample text written to count the number of words in a sentence
The number of words in the sentence is  15

'''
