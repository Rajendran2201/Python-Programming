'''
Take a tuple of two elements representing the co-ordinates and calculate the distance between them 

'''

my_tuple = ((1,2),(3,4))

distance = ((my_tuple[1][0] - my_tuple[0][0])**2 + (my_tuple[1][1] - my_tuple[0][1])**2)**0.5

print("Distance : ",distance)

'''
OUTPUT : 

Distance :  2.8284271247461903

'''