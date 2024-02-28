'''
Check if all the elements of the tuple is unique or not 

'''

def check_if_unique(my_list)->bool:
    for i in range(len(my_list)):
        for j in range(i+1,len(my_list)):
            if my_list[i] == my_list[j]:
                 return False
    return True
    

list1 = [1,2,3,4,5,3,4]
list2 = [1,4,6,8,9]

is_unique = check_if_unique(list2)
if is_unique == True :
    print("There are no duplicate Elements, The list is unique")
else : 
    print("There are  duplicate Elements, The list is not unique")


'''
 
 OUTPUT (list1) : 

 There are  duplicate Elements, The list is not unique

 OUTPUT (list2) : 

 There are no duplicate Elements, The list is unique

 '''   