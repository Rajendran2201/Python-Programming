'''

Given two tuples, perform element-wise addition and print the result


'''

# function to add the remaining elements 
def add_remaining_list1(min_length) -> list: 
    sum_list = list2[min_length:]
    return sum_list
def add_remaining_list2(min_length) -> list: 
    sum_list = list1[min_length:]
    return sum_list


tuple1 = (1,54,3,2)
tuple2 = (3,5,4,2,5,23,4)

#converting the tuples into list 

list1 = list(tuple1)
list2 = list(tuple2)

sum_list = []

min_length = min(len(list1),len(list2))

# add the elements upto the length of both valid indices 
for i in range(min_length):
    sum_list.append(list1[i]+list2[i])

# adding the leftovers     
if min_length == len(list1):
    sum_list += add_remaining_list1(min_length)
else :
    sum_list += add_remaining_list2(min_length)

print("Sum of two tuples (element-wise) : ", tuple(sum_list))


'''

OUTPUT : 


Sum of two tuples (element-wise) :  (4, 59, 7, 4, 5, 23, 4)

'''
