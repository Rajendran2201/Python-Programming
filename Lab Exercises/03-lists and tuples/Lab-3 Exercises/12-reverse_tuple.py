'''
Reverse the order of elements in a tuple without using the reverse function 

'''

my_tuple = (1,2,3,4,5)
list1 = list(my_tuple)
list2 = list1[::-1]
print("Reversed tuple : ",tuple(list2))


'''


OUTPUT : 

Reversed tuple :  (5, 4, 3, 2, 1)



'''