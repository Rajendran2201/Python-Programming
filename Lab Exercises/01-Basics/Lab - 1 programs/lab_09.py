'''
. Tell whether the transaction is pro table or not
 Buying Price : 500 Selling Price: 700

'''


buying_price = int(input("Enter your buying price : "))
selling_price = int(input("Enter your selling price : "))

profit_loss = selling_price-buying_price

if profit_loss>0: 
    print(f"Your profit is {profit_loss}")
elif profit_loss<0: 
     profit_loss*=-1
     print(f"Your loss is {profit_loss}")
else: 
      print("Your buying price is as same as your selling price")

'''

OUTPUT : 

Enter your buying price : 500
Enter your selling price : 700
Your profit is 200


'''