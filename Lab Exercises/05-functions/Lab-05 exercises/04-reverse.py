'''
 Write a Python function called reverse_list that takes a list as input
 and returns a new list with the elements in reverse order

'''

def reverse_list(nums)->list:
    '''This function takes a list as an input and returns a new list with the elements in reverse order'''
    reversed = []
    for i in range(len(nums)-1, -1, -1):
        reversed.append(nums[i])
    return reversed

my_list = [1,2,3,4,5]
print("The list before reversing : ",my_list)
print("The list after reversed : ",reverse_list(my_list))


'''
OUTPUT : 

The list before reversing :  [1, 2, 3, 4, 5]  
The list after reversed :  [5, 4, 3, 2, 1]    

'''