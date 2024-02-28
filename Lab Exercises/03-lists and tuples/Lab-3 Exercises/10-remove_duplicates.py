'''

Remove duplicates from a tuple and print the result 

'''

my_tuple = (1,2,3,2,4,2,1,5,3,6,7,6,4)

my_list = list(my_tuple)
unique_list = []

for i in my_list:
    if i not in unique_list:
        unique_list.append(i)

unique_tuple = tuple(unique_list)

print("Tuple after removing duplicate elements : ",unique_tuple)


'''
OUTPUT : 

Tuple after removing duplicate elements :  (1, 2, 3, 4, 5, 6, 7)

'''

