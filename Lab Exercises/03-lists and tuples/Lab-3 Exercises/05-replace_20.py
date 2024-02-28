'''

 You have given a python list.
 Write a program to find the value 20 in the list,
 and if it is present , replace it with 200. 
 Only update the first occurence of an item 

'''

my_list = [23,54,65,20,68,20,67,20]

is_changed = False
for i in range(len(my_list)):
    if my_list[i]==20 and is_changed == False :
        my_list[i] = 200
        is_changed = True

print("List after replacement : ",my_list)


'''

OUTPUT : 

List after replacement :  [23, 54, 65, 200, 68, 20, 67, 20]

'''