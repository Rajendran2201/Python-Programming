'''


Write a Python program to find the longest string in a given list of strings.
Input:
['cat', 'car', 'fear', 'center']

'''

    
words = []
lengths = []


print("Enter stop to quit \nEnter the words to find the longest of them : ")

# getting the input values 
while(1):
    word = input()
    if(word == 'stop'):
        break
    words.append(word)

# finding the length of each word
for i in words:
    count = len(i)
    lengths.append(count)
    
# finding the word with maximum length
index = 0
maximum = 0

for i in range(len(lengths)):
    if lengths[i] > maximum :
        maximum = lengths[i]
        index = i
        
print("The longest word is ",words[index])


'''

OUTPUT : 


Enter stop to quit 
Enter the words to find the longest of them : 
varun
vsurn
stop
The longest word is  varun


'''
    


    

    

    