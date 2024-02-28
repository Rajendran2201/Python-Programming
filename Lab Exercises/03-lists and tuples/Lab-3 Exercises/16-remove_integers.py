'''
Given a tuple of various data types, remove the values of data type of int and print the resultant tuple 

'''

my_tuple = (1,2,3,4,5,"raj",7,"5",53,3.43,True)

my_list = list(my_tuple)

i = 0
while i < len(my_list):
    if type(my_list[i]) == int:
        my_list.remove(my_list[i])
        continue
    i+=1

print("Resultant tuple : ",tuple(my_list))


'''

OUTPUT : 

Resultant tuple :  ('raj', '5', 3.43, True)


'''