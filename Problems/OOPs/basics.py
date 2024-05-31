'''
OOP - Object Oriented Programming

1. Class
2. Object


----------------------- Restaurant Ordering System ---------------------------------


1. Boss Login
    - add food item
    - remove food item
    - check revenue

2. Customer Login
    - view menu
    - order
    - generate bill

'''

menu = {'squid chilly':300, 'vanjaram':250, 'prawn biryani':400, 'butter chicken':140}
items = []
grand_total = 0

class Customer:
  def __init__(self, customer_name):
    self.customer_name = customer_name


  def view_menu(self):
    for i in menu:
      print(i)
  
  def take_order(self):

    while(True):
      print("Enter your choice, Enter 0 to break")
      item = input("What do you want?")
      if item == "0":
        break
      if item not in menu:
        print("Sorry, the item is not available")
      else:
        items.append(item)
        print("The item is successfully added!")
        return menu[item]
  
  def generate_bill(self):
    total = 0
    for i in items:
      total += menu[i]
    print(f"Your bill is {total}")
    return total
      
        
class Boss:
  def add_item(self):
    item = input("Enter the item to be added: ")
    price = int(input("Enter the price: "))
    menu[item] = price

  def remove_item(self):
    item = input("Enter the item to be removed: ")
    menu.pop(item)


  def generate_revenue(self):
    print(f"Revenue: {grand_total}")

print("Welcome to SP Restaurant!!")
while(True):
  print("Enter an option")
  print("0 - Quit")
  print("1 - Customer Login")
  print("2 - Boss Login")

  option = int(input("Enter your option: "))

  if option == 0:
    break
  elif option == 1:
    name = input("Enter your name: ")
    c = Customer(name)
    while(True):
      print("0 - break")
      print("1 - view menu")
      print("2 - order")
      print("3 - generate bill")
      choice = int(input("Enter your choice: "))

      if choice == 0:
        break
      elif choice == 1:
        c.view_menu()
      elif choice == 2:
        total = c.take_order()
        grand_total += total
      elif choice == 3:
        c.generate_bill()
        
      else:
        print("Invalid input")
  elif option == 2:
    b = Boss()
    while(True):
      print("0 - break")
      print("1 - add item")
      print("2 - remove")
      print("3 - generate revenue")
      choice = int(input("Enter your choice: "))

      if choice == 0:
        break
      elif choice == 1:
        b.add_item()
      elif choice == 2:
        b.remove_item()
      elif choice == 3:
        b.generate_revenue()
      else:
        print("Invalid input")
  else:
    print("Invalid Input")





