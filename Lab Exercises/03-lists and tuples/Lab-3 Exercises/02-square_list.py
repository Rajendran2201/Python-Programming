'''

Given a list of numbers. Write a program to turn every item of a list into its square

'''

my_list = [1,2,3,4,5,6,7,8,9]

for i in range(len(my_list)):
    my_list[i] *= my_list[i]

print("Squared list : ",my_list)


'''
OUTPUT : 

Squared list :  [1, 4, 9, 16, 25, 36, 49, 64, 81]

'''
