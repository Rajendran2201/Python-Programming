'''


 Create a Python function called calculate_average that takes a list
 of numbers as input and prints the average of those numbers
 without returning anything.

 
 '''

def calculate_average(nums)->None :
    '''This function takes a list as an input and print the average of the values of the list'''
    sum = 0
    for i in nums : 
        sum += i
    avg =  sum / len(nums)
    print("Average :",avg)

list1 = [1,2,3,4,5]
calculate_average(list1)


'''
OUTPUT : Average : 3.0

'''