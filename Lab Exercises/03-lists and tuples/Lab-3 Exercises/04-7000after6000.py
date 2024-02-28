'''

Write a python program to add 7000 after 6000 in a list

'''

list1 = [1000,2000,4000,6000,8000,10000]
ans_list = []

for i in list1: 
    ans_list.append(i)
    if i == 6000 : 
        ans_list.append(7000)
    

print("List after appending : ", ans_list)


'''

OUTPUT : 

List after appending :  [1000, 2000, 4000, 6000, 7000, 8000, 10000]


'''