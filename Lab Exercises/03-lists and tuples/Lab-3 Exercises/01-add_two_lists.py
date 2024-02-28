'''

Write a program to add two lists index-wise. 
Create a new list that contains the 0th index item from both the list,
then the 1st index item, and so on till the last item. 
Any leftover will get added at the end of the new list.

'''
list1, list2 = [1,2,3,4] , [4,5,6] 
sum_list = []

max_length = max(len(list1),len(list2))

# add the elements upto the length of both valid indices 
for i in range(max_length):
   if i < len(list1):
      sum_list.append(list1[i])
   if i < len(list2):
      sum_list.append(list2[i])


print("Resultant list : " , sum_list)


'''
OUTPUT : 

Resultant list :  [1, 9, 2, 8, 3, 7, 4, 6, 5, 4, 3, 2]


'''