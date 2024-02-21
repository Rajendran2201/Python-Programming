'''
 Write a Python program to determine whether a given year is leap year or not
 
'''


year = int(input("Enter a year : "))

if year%400 == 0 or (year%100!=0 and year%4==0):
    print(f"{year} is a leap year")
else:
     print(f"{year} is not a leap year")


'''

OUTPUT : 

Enter a year : 2006
2006 is not a leap year

'''