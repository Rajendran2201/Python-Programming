''''

 Write a Python function that takes alist of integers and returns the
 maximum element.


'''
def maximum_element(my_list)->int:
    '''This function takes a list as an input and returns the maximum element in the list'''
    return max(my_list)

my_list = [4,5,3,5,25,43,98]
print("The maximum element in {} is {}".format(my_list, maximum_element(my_list)))

'''
OUTPUT :

The maximum element in [4, 5, 3, 5, 25, 43, 98] is 98

'''