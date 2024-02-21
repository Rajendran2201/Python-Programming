'''
Write a
 Python program to ndtheeligibility of admission for a professional course
 based onthefollowing criteria:
 Eligibility Criteria : Marks in Maths >=65 and Marks in Phy >=55 and Marks in
 Chem>=50 and Total in all three subject >=190 or Total in Maths and Physics
 >=140------------------------------------- Input the marks obtained in Physics
 :65 Input the marks obtained in Chemistry :51 Input the marks obtained in
 Mathematics :72 Total marks of Maths, Physics and Chemistry : 188 Total
 marks of MathsandPhysics : 137 Thecandidate is not eligible.
 Expected Output :
 Thecandidate is not eligible for admission

'''



math_mark = int(input("Enter your maths marks : "))
physics_mark = int(input("Enter your physics marks : "))
chemistry_mark = int(input("Enter your chemistry marks : "))

total_mark = physics_mark+math_mark+chemistry_mark
partial_total = math_mark+physics_mark

if math_mark>=65 and physics_mark>=55 and chemistry_mark>=50: 
    if total_mark>=190 or partial_total>=140:
        print("The candidate is eligible for admission")
    else: 
        print("The candidate is not eligible for admission")
else: 
    print("The candidate is not eligible for admission")

    

'''
OUTPUT : 


Enter your maths marks : 72
Enter your physics marks : 65
Enter your chemistry marks : 51
The candidate is not eligible for admission

'''
