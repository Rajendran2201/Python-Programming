''' 
-------------------------------------------- SUPERMARKET MANAGEMENT SOFTWARE --------------------------------------------

 1. ---- Functionalities:

 - Billing
 - Inventory Management
 - HR Functionalities 

 2. ---- Main Objects:

 Create a software system which allows the user to handle the following operations

 -- Customer viewpoint:

 - Add a product
 - Remove a product 
 - Generate bill 
 - Deduce discount based on the total bill
 - Include Taxes such as GST

 -- Employee viewpoint:

 - Add an employee 
 - Remove an employee
 - Salary of each employee
 - Generate payroll

 3. ---- Attributes:

 Classes: 

 1. Product: product_name, price, quantity
 2. Customer: customer_name, customer_phno
 3. Employee: employee_name, employee_id, employee_phno, employee_join_date, employee_salary, employee_role
 4. HR: HR_name, HR_id, HR_salary

 4. ---- Methods:

 PRODUCT: add_product(), remove_product(), calculate_bill(),  add_taxes(), deduce_discount(), generate_bill()
 EMPLOYEE: add_employee(), remove_employee(), print_employee_details() 
 HR: generate_payroll()




'''
# Global declarations
total_employees, products = [], []
total_products = {"Apple":120, "Banana" : 5, "Cherry" : 60, "Bread" : 35, "Cheese" : 50, "Rice" : 45, "Pasta" : 25}
total_quantity =  {}


class Product:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
        total_quantity[product_name] = quantity

        

        self.add_product()

    def add_product(self):
        products.append(self.product_name)
       
    
    def remove_product(product_name):
        products.remove(product_name)



    def generate_bill():
        def calculate_GST(total):
            if total < 500:
                GST = total * 0.05
            elif 500< total < 1000:
                GST = total * 0.1
            else:
                GST = total * 0.12
            return GST
    
        def calculate_discount(total):
            if total < 500:
                discount = total * 0.02
            elif 500< total < 1000:
                discount = total * 0.04
            else:
                discount = total * 0.06
            return discount

        total = 0
        for i in products:
            sub_total = total_quantity[i]*total_products[i]
            print(f"{i}          {total_quantity[i]} x {total_products[i]} = {sub_total}")
            total += sub_total
        print("Total amount: ₹", total)
        GST = calculate_GST(total)
        discount = calculate_discount(total)
        total += GST
        total -= discount
        print("GST: ₹", GST)
        print("Discount: ₹", discount)
        print("Final total amount: ₹", total)
          
class Employee:
    def __init__(self, employee_id, employee_name, employee_phone, employee_jdate, employee_role, employee_salary):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.employee_phone = employee_phone
        self.employee_jdate = employee_jdate
        self.employee_role = employee_role
        self.employee_salary = employee_salary

        self.add_employee()

    def add_employee(self):
        total_employees.append([self.employee_id, self.employee_name, self.employee_phone,  self.employee_jdate, self.employee_role, self.employee_salary])
    
    def remove_employee():
        removable_employee_id = int(input("Enter the id of the employee to be removed: "))
        for employee in total_employees:
            if employee[0] == removable_employee_id:
                total_employees.remove(employee)
    
    def display_employees():
        i = 0
        print("Total Employees in the SuperMarket: ")
        for employee in total_employees:
            print(f"{i}. {employee}")
            i += 1
    def generate_payroll():
        total = 0
        for employee in total_employees:
            total += employee[5]
        return total
        
while(True):
     # Main menu
    print("------------------------------------------------------------------------")
    print("Enter the appropriate option:")
    print("0 - quit")
    print("1 - Customer menu")
    print("2 - HR menu")

    try: 
        main_option = int(input("Enter your choice: "))

        if main_option == 0:
            break
        elif main_option == 1:
            while(True):
                # Main Menu for the customer
                print("------------------------------------------------------------------------")
                print("Enter the appropriate option to perform the following operations: ")
                print("0 - Quit")
                print("1 - Add a product to the cart")
                print("2 - Remove a product from the cart")
                print("3 - View the products in the cart")
                print("4 - Generate bill")
                print("5 - View all the products available in the supermarket")


                try: 
                    option = int(input("Enter your option: "))

                    # 0 - Quit
                    if option == 0:
                        print("Thank you for shopping! Visit us again!")
                        break

                    # 1 - Adding items to the cart
                    if option == 1:
                        product_name = input("Enter the product name: ")
                        try: 
                            price = total_products[product_name]
                            quantity = int(input("Enter the quantity: "))
                            product = Product(product_name, price, quantity)
                        except:
                            print("The product is not available!")
                    
                    # 2 - Removing items from the cart
                    elif option == 2:
                        product_name = input("Enter the product name: ")
                        Product.remove_product(product_name)

                    # 3 - View products in the cart
                    elif option == 3:
                        print("Products in the cart:")
                        i = 1
                        for product in products:
                            print(f"{i}. {product}")
                            i += 1

                    # 4 - Generate the bill 
                    elif option == 4:
                        Product.generate_bill()

                    # 5 - View the products in the super market
                    elif option == 5:
                        print("Products in the super market:")
                        i = 1
                        for product in total_products:
                            print(f"{i}. {product}")
                            i += 1

                # To handle the invalid inputs
                    else:
                        print("Invalid Input")
                except:
                    print("Oops! That was an invalid input, Please try again!")
        elif main_option == 2:
             while(True):
                # Main Menu for the HR
                print("------------------------------------------------------------------------")
                print("Enter the appropriate option to perform the following operations: ")
                print("0 - Quit")
                print("1 - Add an employee")
                print("2 - Remove an employee")
                print("3 - View the employees in the supermarket")
                print("4 - Generate payroll")

                try: 
                    option = int(input("Enter your option: "))

                    if option == 0:
                        break
                    elif option == 1:
                        employee_id = int(input("Enter the Employee ID: "))
                        employee_name = input("Enter the Employee name: ") 
                        employee_phone = input("Enter the Employee contact no: ")
                        employee_jdate = input("Enter the joining date: ")
                        employee_role = input("Enter the role of the Employee: ")
                        employee_salary = int(input("Enter the salary of the Employee: "))
                        employee = Employee(employee_id, employee_name, employee_phone, employee_jdate, employee_role, employee_salary)
                    elif option == 2:
                        Employee.remove_employee()
                    elif option == 3:
                        Employee.display_employees()
                    elif option == 4:
                        payroll = Employee.generate_payroll()
                        print("Payroll : ", payroll)
                    else:
                        print("Can you please enter a valid input?")

                except Exception as e:
                    print(e)
                    print("Sorry, You entered an invalid choice!")
        else:
            print("Invalid input, please enter a valid choice!")
    except:
        print("Sorry, That wasn't a valid choice!")

   

print("Thank you for shopping! Visit us again!")