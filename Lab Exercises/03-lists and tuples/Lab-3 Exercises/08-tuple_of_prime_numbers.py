'''

Create a tuple containing first five prime numbers 

'''


def isPrime(n)->bool: 
    for i in range(2,int(n**0.5)+1):
        if n % i == 0 : 
            return False 
    return True 


my_list = []

i , count = 2 , 0 
while count < 6:
    if isPrime(i) == True : 
        my_list.append(i)
        count+=1
    i+=1

print("Tuple containing first five prime numbers : ",tuple(my_list))


'''
OUTPUT : 

Tuple containing first five prime numbers :  (2, 3, 5, 7, 11, 13)

'''