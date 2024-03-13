'''
 Write a Python function that takes a list of numbers as input and
 returns the sum of all the numbers using recursion.

'''

def sum_of_numbers(list1) -> int:
    '''This function takes a list as an input and returns the sum of the numbers in the list recursively'''
    if not list1:
        return 0
    return list1[0] + sum_of_numbers(list1[1:])


list1 = [1,2,3,4,5]
print("The sum of elements in {} is {}".format(list1, sum_of_numbers(list1)))

'''
OUTPUT : 

The sum of elements in [1, 2, 3, 4, 5] is 15  

'''