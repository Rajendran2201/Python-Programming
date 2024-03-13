'''
 Write a Python function called create_phonebook that takes two lists,
 one containing names and the other containing phone numbers, and
 returns a dictionary where the names are keys and the phone numbers
 are values.

'''

def create_phonebook(list1, list2)->dict:
    '''This function takes two lists as input and returns a dictionary by mapping the values of two lists'''
    my_dict = dict(zip(list1,list2))
    return my_dict

list1 = ['raj','siri','theju']
list2 = [9500342342, 2342342343, 4234235544]
print("Dictionary : ", create_phonebook(list1, list2))


'''
OUTPUT : 

Dictionary :  {'raj': 9500342342, 'siri': 2342342343, 'theju': 4234235544}

'''