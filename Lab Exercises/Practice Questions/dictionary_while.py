'''
Write a python code to print the elements of a dictionary 

'''

my_dict = {
    'name' : "Raj",
    'age' : 19,
    'gender' : 'M',
    'place' : "Coimbatore"
}

keys = list(my_dict.keys())
values = list(my_dict.values())
i = 0
while i<len(keys) : 
    print(keys[i], " : ", values[i])
    i += 1

'''
OUTPUT : 

name  :  Raj
age  :  19
gender  :  M
place  :  Coimbatore

'''