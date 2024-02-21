
'''

 Write a Python program to read temperature in centigrade and display a
 suitable message according to temperature state below :
 Temp<0thenFreezingweather
 Temp0-10thenVeryColdweather
 Temp10-20thenColdweather
 Temp20-30thenNormalinTemp
 Temp30-40thenIts Hot
 Temp>=40thenIts Very Hot
 Test Data :
 42
 Expected Output :
 It's very hot.


'''



temp = int(input("Enter the temperature : "))

if temp<0: 
    print("Freezing Weather")
elif temp>=0 and temp<10: 
    print("Very Cold weather")
elif temp>=10 and temp<20: 
    print(" Cold weather")
elif temp>=20 and temp<30: 
    print("Normal weather")
elif temp>=30 and temp<40: 
    print("Hot")
else: 
    print("Very Hot")

        

'''

OUTPUT : 

Enter the temperature : 65
Very Hot

'''