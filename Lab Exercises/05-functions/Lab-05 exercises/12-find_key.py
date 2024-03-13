'''

 Implement a Python function called find_key_by_value that takes a
 dictionary and a value as input and returns the corresponding key
 if the value is found in the dictionary, and None otherwise.

'''

def find_key_by_value(my_dict,num):
    '''This function takes a dictionary and a num as an input and returns the key of the value in the dictionary'''
    for key,value in my_dict.items():
        if num == value :
            return key
    return None

my_dict = {'raj' : 22, 'aswin' : 23, 'karthik' : 51}
value = int(input("Enter a value : "))
print("The key of {} is {}".format(value, find_key_by_value(my_dict, value)))


'''
Enter a value : 23
The key of 23 is aswin

Enter a value : 25
The key of 25 is None

'''