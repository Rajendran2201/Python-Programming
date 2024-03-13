'''

 Create a Python function called calculate_average_grade that takes a
 dictionary where the keys are student names and the values are lists
 of grades, and returns a new dictionary where the keys are student
 namesandthevalues are their average grades.


'''

def calculate_average_grade(my_dict):
    '''This function takes a dictionary of student names as keys and list of marks as values as an input and 
    returns another dictionary with student names as key and their average grades as the values'''
    keys = list(my_dict.keys())
    average_grades = []
    for key, grades in my_dict.items():
        sum = 0
        for i in grades:
            sum += i 
        avg = sum / len(grades)
        average_grades.append(avg)

    return dict(zip(keys, average_grades))


my_dict = {'raj' : [100,90,80,70,60], 'rishi' : [100,100,100]}

print(calculate_average_grade(my_dict))

'''
OUTPUT : 

{'raj': 80.0, 'rishi': 100.0}

'''