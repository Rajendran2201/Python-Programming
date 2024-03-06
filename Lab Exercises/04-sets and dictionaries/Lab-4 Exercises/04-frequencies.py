'''
Counting the frequencies in  a list using dictionary 

INPUT : [1,1,1,2,2,3,4,4,4,4,5,5]

OUTPUT : 

1 : 3
2 : 2
3 : 1
4 : 4
5 : 2

'''
def get_count(element) -> int: 
    '''
    purpose : to find the frequency / number of occurences of an element in a list 
    param : element (int)
    rtype : int
    '''
    count = 0
    for i in list_1: 
        if i == element: 
            count += 1
    return count


list_1 = [1,1,1,2,2,3,4,4,4,4,5,5]
set_1 = set(list_1)
counts = []
dict_1 = {}

for i in set_1:
    count = get_count(i)
    counts.append(count)

dict_1 = dict(zip(set_1,counts))
print("Frequencies : ",dict_1)


'''
OUTPUT : 

Frequencies :  {1: 3, 2: 2, 3: 1, 4: 4, 5: 2} 

'''
