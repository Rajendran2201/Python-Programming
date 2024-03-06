'''
Convert two lists into a dictionary using zip function and list() constructor 

'''

list_1 = ['a','b','c','d','e']
list_2 = [5,6,7,8,9]
resultant_list = dict(zip(list_1,list_2))
print("The dictionary after merging the two lists is ",resultant_list)



'''
OUTPUT: 

The dictionary after merging the two lists is  {'a': 5, 'b': 6, 'c': 7, 'd': 8, 'e': 9}

'''