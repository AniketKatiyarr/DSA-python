print("Welcome to the Money Bank of India")
restart = ('y')
chances = 3
balance = 100
while chances >=0:
    
   Pin = int(input("Enter your 4 digit pin:"))
   if Pin == 1234:
     print("you enter your code corrrectly")
     while restart not in ('n','N', 'No'):
       print("Do you want to Withdraw ?")
       print("Do you want to enquire your balance ?")
       print("Want fast cash ?")
       option = int(input("what would you like to chossse ?"))
       if option == 1:
           print("you can withdraw the balance INR:\n",balance)
           restart = int(input("would you like to restart"))
           if restart in ('N','n','No'):
               print("Thank you")
               break
           elif option == 2:
              restart = ('y')
              withdrawal = (float(input("How much you want to withdraw the amount:")))
              if withdrawal in [10,20,30,40,50,60,70,80,90,100]:
                  balance = balance - withdrawal
                  print("your current balance is:" ,balance)
                  restart = input("would you like to go back?")
                  if restart in ('n','No','no','N'):
                    print("THANK YOU")
                    break
              elif withdrawal != [10,20,30,40,50,60,70,80,90,100]:
                  print("Invalid Amount , Please Re-try/n")                 
                  restart = ('y')
              elif withdrawal == 1:
                  withdrawal = float(input('Please Enter Desired amount:'))
           elif option == 3:
             pay_in = float(input('How much would you like to pay in?'))
             balance = balance + pay_in
             print('/Your balance is now: ',balance) 
             restart  = input("Would you like to Go back?")
             if restart in('n','N','No'):
               print("Thank you")
               break
           elif option == 4:
              print('please wait while your card is returned...../n')
              restart('y')
   elif Pin != ('1234'):
      print('Incorrect Password')
      chances = chances - 1
      if chances ==0:
        print("/No more attempt")
        break                
                   
            
               
            
           