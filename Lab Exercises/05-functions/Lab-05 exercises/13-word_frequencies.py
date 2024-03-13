'''
Implement a Python function named calculate_word_frequencies that
 takes a string of text as input and returns a dictionary where the keys
 are the words in the text and the values are the frequencies of those
 words

'''


def calculate_word_frequencies(sentence) -> int: 
    '''This function takes a string as an input and finds the number of times the string appeared'''
    count = 0
    for i in list1: 
        if i == word: 
            count += 1
    return count


sentence = input("Enter a sentence : ")
list1 = sentence.split(' ')
set1 = set(list1)
counts = []
for word in set1:
    count = calculate_word_frequencies(word)
    counts.append(count)

print(dict(zip(set1,counts)))


'''
OUTPUT : 

Enter a sentence : My name is the name of the king's name which is rajendran
{'which': 1, 'the': 2, "king's": 1, 'is': 2, 'My': 1, 'of': 1, 'rajendran': 1, 'name': 3}

'''