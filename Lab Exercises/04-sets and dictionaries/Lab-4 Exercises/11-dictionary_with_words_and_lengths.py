'''
Get a string as an input from the user and create a dictionary which stores each word as its key and the length of the word as its value

'''
def get_count(element) -> int: 
    '''
    purpose : to find the frequency / number of occurences of an element in a list 
    param : element (int)
    rtype : int
    '''
    count = 0
    for i in lengths_2: 
        if i == element: 
            count += 1
    return count

string = input("Enter a sentence : ")

words = list(string.split(" "))

set_1 = set(words)

lengths_1 = [len(word) for word in set_1]  
dict_1 = dict(zip(set_1, lengths_1))
print(dict_1)

lengths_2 = [len(word) for word in words]  
set_2 = set(lengths_2)

counts = [get_count(i) for i in set_2]  
dict_2 = dict(zip(set_2, counts))
print(dict_2)


'''
OUTPUT : 

Enter a sentence : A fat cat is on the mat
{'is': 2, 'the': 3, 'mat': 3, 'A': 1, 'cat': 3, 'fat': 3, 'on': 2}
{1: 1, 2: 2, 3: 4}

'''