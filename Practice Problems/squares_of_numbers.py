'''
Write a python code to find the square of the values of a list  

'''

list_1 = [1,2,3,4,5]
list_2 = []

i = 0
while i<len(list_1):
    list_2.append(list_1[i]**2)
    i += 1
    
print(list_2)

'''

OUTPUT : 

[1, 4, 9, 16, 25]


'''
