'''Write a python code to find the longest word in a sentence'''

sentence = input("Enter a sentence : ")
words = list(sentence.split())

max_word = 0
for i in range(len(words)) : 
    if len(words[i]) > len(words[max_word]):
        max_word  = i

print("The longest word in the sentence is {}".format(words[max_word]))


'''

OUTPUT : 

Enter a sentence : my name is rajendran
The longest word in the sentence is rajendran

'''
