'''


 Implement a Python function called calculate_tax that takes the
 income of a person as input and returns the amount of tax they need
 to pay based onthefollowing tax brackets:
 0%tax for income uptoRs10,000
 10% tax for income between Rs.10,001 and Rs.50,000
 20% tax for income between Rs.50,001 and Rs.100,000
 30% tax for income above Rs.100,000

 '''


def calculate_tax(income) -> float:
    '''This function takes the income of a person and returns the tax amount for the given income'''
    if income <= 10000:
        return 0 
    elif income <= 50000:
        return income * 0.1
    elif income <= 100000:
        return income * 0.2
    return income * 0.3

income = float(input("Enter your income : "))
print("The tax amount for ${} is ${}".format(income, calculate_tax(income)))



'''
OUTPUT : 

Enter your income : 70000
The tax amount for $70000.0 is $14000.0    

'''