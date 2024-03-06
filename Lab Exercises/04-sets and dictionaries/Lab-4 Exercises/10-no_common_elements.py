'''

Write a python code to check if two sets have no common elements 

'''

set_1 = {1,2,3,4,5}
set_2 = {6,7,8,9}
is_common_present = set_1.isdisjoint(set_2)

if is_common_present == True : 
    print("There are no common elements in the sets")
else : 
    print("There are  common elements in the sets")


'''
OUTPUT : 

There are no common elements in the sets

'''