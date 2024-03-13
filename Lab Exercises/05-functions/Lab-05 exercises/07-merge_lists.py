'''
 Create a Python function called merge_lists that takes two lists as
 input and returns a new list containing all the elements from both
 lists

'''


def merge_lists(list1, list2) -> list:
    '''This function takes two lists as an input and returns a new list by merging the two lists'''
    
    new_list = []

    # adding the elements of first list into the new list 
    for i in list1:
        new_list.append(i)

    # adding the elements of second list into the new list 
    for i in list2:
        new_list.append(i)
    return new_list

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
print("The list after merging the two lists is ", merge_lists(list1, list2))


'''
OUTPUT : 

The list after merging the two lists is  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''