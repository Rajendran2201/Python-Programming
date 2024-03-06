'''
Write a python code to check if a given element is present in a set ot not

'''

element = int(input("Enter an element : "))
set_1 = (1,2,3,4,5)

if element in set_1 : 
    print(f"{element} is present in {set_1}")
else : 
    print(f"{element} is not present in {set_1}")


'''
OUTPUT -1 : 

Enter an element : 34
34 is not present in (1, 2, 3, 4, 5)

OUTPUT -2 : 

Enter an element : 4
4 is present in (1, 2, 3, 4, 5)


'''