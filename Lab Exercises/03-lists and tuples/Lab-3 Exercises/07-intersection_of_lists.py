'''

Create a function to find the intersection of two lists 

'''

def intersection(list1,list2)->list:
    intersetion_list = [] 
    for i in list1:
        if i in list2: 
            intersetion_list.append(i)
    return intersetion_list


list1 = [1,2,3,4,5,6]
list2 = [4,5,6,7,8,9]

intersetion_list = intersection(list1,list2)

print("The Intersection of two lists : ", intersetion_list)


'''
OUTPUT : 

The Intersection of two lists :  [4, 5, 6]

'''