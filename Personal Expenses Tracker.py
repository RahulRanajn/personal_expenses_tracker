import json
import os
menu = ["Add Income", "Add Expenses", "View All Transaction", "Total Income", "Total Expenses"," Remaining Balance","Monthly Summary","Delet An Expenses", "Exit"]

transacations = []
total_expenses = 0
total_income = 0

if os.path.exists("transactions.json"):
  with open("transactions.json", "r") as file:
    transacations = json.load(file)   

else:
  with open("transactions.json", "w") as file:
    json.dump(transacations,file)

for item in transacations:
  if item["type"] == "income":
    total_income += item["amount"]
  elif item["type"] == "expenses":
    total_expenses += item["amount"]
    
def saved_transactions():
  with open("transactions.json", "w") as file:
    json.dump(transacations,file, indent=4)
   
def transactions_data(name, amount, category, type):
  
  transacations.append({
    "name" : name,
    "amount" : amount,
    "category" : category,
    "type" : type
  })

def income_inputs():
  income_type = "income"
  income_name = input("Enter income name: ")
  income_amount = float(input("Enter your income: "))
  income_category = input("Enter the category: ")
  return income_type, income_name, income_amount, income_category
  
   
def expenses_inputs():
   transaction_type = "expenses"
   name = input("Enter a expenses name: ")
   amount = float(input("Enter amount: "))
   category = input("enter category: ")
   return name, amount, category, transaction_type
    


while True:
  print("=== Expenses Tracker ===")
  
  for idx, items in enumerate(menu):
    print(idx+1, items)
  choice = int(input("Enter your choice (1-9): "))
  
  if (choice > 9) or (choice <= 0):
    print("Please select a valid number between 1-7")
  elif choice == 9:
    print("Exiting...")
    break
    
  if choice == 1:
    print("=== Add Your Income ===")
    income_info = income_inputs()
    in_type, in_name, in_amount, in_category = income_info
    transactions_data(in_name, in_amount, in_category,in_type)
    total_income += in_amount
    saved_transactions()
    print("income added successfully...")
    
  elif choice == 2:
    print("=== Add Your Expenses ===")
    expenses_info = expenses_inputs()
    ex_name, ex_amount, ex_category, ex_type = expenses_info
    transactions_data(ex_name,ex_amount,ex_category,ex_type)
    total_expenses += ex_amount
    saved_transactions()
    print("expenses added successfully")
    
  elif choice == 3:
    if not transacations:
      print("No Transaction Found!")
    else:
      for index, item in enumerate(transacations):
       print(f"====== Transaction {index+1} ======")
       for key, value in item.items():
         print(f"{key} : {value}")
         
  elif choice == 4:
    print("=== Printing Total Income ===")
    print(f"Total Income: {total_income}")
    
  elif choice == 5:
    print("=== Printing Total Expenses ===")
    print(f"Total Expenses: {total_expenses}")

  elif choice == 6:
    remaining_balance = total_income - total_expenses
    print(f"Remaining Balance: ₹{remaining_balance}")
