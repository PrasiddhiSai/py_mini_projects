balance = 5000;
user = 0
while user != 4:
  user = int(input(" 1. Check balance \n 2. Deposit \n 3. Withdraw \n 4. Exit\n What do you wanna do?\t"))
  if user == 1:
    print(f"Your current balance is ${balance} . You rich mf!")
    continue
    
  elif user == 2:
     amount = int(input("Enter the amount you wanna deposit: "))
     if amount <= 0:
          print("Invalid amount ")
     else:
          balance = amount + balance
          print(f"Your current balance is ${balance}")
          continue
          
  elif user == 3:
     amt = int(input("How much you wanna withdraw?: "))
     if balance > amt:
         balance = balance - amt
         print(f"You have ${balance} left now.")
     elif balance < amt:
          print("You broke mf you don't have sufficient amount to withdraw") 
     elif balance == amt:
          print("You have withdrawn all the money. Now your account has no money. Start earning some cash mf")
          continue

  elif user == 4:
     print('Thank You!')
     

  else:
    print("you illiterate mf select 1,2,3 or 4.")
     

        
   
     
     

    

