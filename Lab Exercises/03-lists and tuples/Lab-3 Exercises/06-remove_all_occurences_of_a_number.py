'''

Given a python list, write a program to remove all the occurences of item 20 

'''

my_list = [23,54,65,20,68,20,67,20]

for i in my_list: 
    if i == 20 : 
        my_list.remove(i)

print("List after removing 20 : ",my_list)


'''
OUTPUT : 

List after removing 20 :  [23, 54, 65, 68, 67]

'''