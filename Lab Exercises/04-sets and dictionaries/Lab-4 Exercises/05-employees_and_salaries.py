'''
Write a python program te get employee names and their salaries as input and store them in a dictionary

'''

dict_1 = {}

keys , values = [] , [] 
print("Enter -1 for value to stop giving the inputs")

while(1) :
    key = input("Enter the employee name : ")
    value = int(input("Enter the employee salary : "))
    keys.append(key)
    if value == -1 : 
        break
    values.append(value)
    
dict_1 = dict(zip(keys,values))

print(dict_1)

'''
OUTPUT : 

Enter -1 for value to stop giving the inputs

Enter the employee name : sino
Enter the employee salary : 12345
Enter the employee name : raj
Enter the employee salary : 543231
Enter the employee name : malai
Enter the employee salary : 123
Enter the employee name : theju 
Enter the employee salary : 1234
Enter the employee name : krishi
Enter the employee salary : -1

{'sino': 12345, 'raj': 543231, 'malai': 123, 'theju ': 1234}


'''
