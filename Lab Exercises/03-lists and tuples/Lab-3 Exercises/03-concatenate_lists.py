'''

Concatenate two lists of string data type 

'''

list1 = ["Hello ", "take "]
list2 = ["Dear ", "care "]
concatenated_list = []

for i in range(len(list1)) :
    for j in range(len(list2)) :
        concatenated_list.append(list1[i] + list2[j])

print("Concatenated list : ",concatenated_list)



'''
OUTPUT : 

Concatenated list :  ['Hello Dear ', 'Hello care ', 'take Dear ', 'take care ']   

'''