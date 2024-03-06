'''

For the following dictionary, find the subject with the least marks 

dict_1 = {

    'physics' : 82,
    'maths' : 65,
    'history' : 75 

}

'''

dict_1 = {

    'physics' : 82,
    'maths' : 65,
    'history' : 75 

}

list_1 = list(dict_1.values())
least_mark = min(list_1)

for key,value in dict_1.items() : 
    if value == least_mark:
        print("The subject with the least mark is ",key)


'''
OUTPUT : 

The subject with the least mark is  maths     

'''