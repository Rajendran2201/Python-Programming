'''

Write a python code to remove the intersection of the second set from the first set 

'''

set_1 = {1,2,3,4,5,6,5,7,8}
set_2 = {1,2,3}

set_3 = set_1 - set_1.intersection(set_2)

print("RESULT : ",set_3)

'''
OUTPUT : 

RESULT :  {4, 5, 6, 7, 8}


'''