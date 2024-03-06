'''

Write a python program to check is a set is a superset of itself and a superset of an another given set 

'''

set_1 = {1,2,2,3,4,5,6,6,7}
set_2 = {1,2,4,5,6,7,8}

if set_1.issuperset(set_1):
    print("The set is a superset of itself")
else : 
    print("The set is not a superset of itself")
    
if set_1.issuperset(set_2): 
    print("The set is a superset of another given set")
else : 
    print("The set is not a superset of another given set")


'''
OUTPUT : 

The set is a superset of itself
The set is not a superset of another given set

'''

