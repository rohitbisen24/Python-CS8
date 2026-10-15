# # # Project - Atm  

# # # 1. lanaguge -> hindi or english > urdu ✅
# # # 2. options
# # # 3. deposit 
# # # 4. credit 
# # # 5. check balance 
# # # 6. reset pin 
# # # 7. genrate pin

# balance = 1000
# pin = 1234

# print("1. Hindi \n2. English \n3. Urdu")
# lanaguge_option = int(input("Select Languge number : "))


# if  lanaguge_option == 2 :

#     user_pin = int(input("enter your pin : "))

#     if user_pin == pin :
#         print("welcome to your Acount")
#         print("1. Check Balaance")
#         print("2. Credit")
#         print("3. Deposit")
#         print("4. pin chnage")
#         print("5. exit")
        
#         choise = int(input("Please Select any option : "))

#         if choise == 1:
#            print(f"Your Ac Balance : {balance}")

#         elif choise == 2:
#             credit_amount =  int(input("Please enter credit amount : ")) #900

#             if credit_amount <= balance :
#                balance = balance - credit_amount
#                print(f"Amount Credited : {credit_amount}")
#                print(f"Clear Ac balance : {balance}")
#             else:
#                print("Ac Balance is low")

#         elif choise == 3:
#             deposit_amount = int(input("Plese enter deposit amount : "))  #5000 
 
#             balance = balance + deposit_amount
#             print(f"Amount Deposited : {deposit_amount}")
#             print(f"Clear Ac balance : {balance}")


#         elif choise == 4:
#             new_pin = int(input("Plese enter new pin : "))
#             pin = new_pin
#             print("pin  Changed")

#         elif choise == 5:
#             print("thanks for visiting")   
            

#         else:
#             print("please enter again") 

#     else : 
#         print("wrong pin Try again")        

# else :
#     print("please enter again")

    

# ATM

# option
# check  balance 
# deposit
# credit


# user - option select krega 
# 1 2 3 

# task perfrom hoga 
# check  balance  
# deposit
# credit


# balance = 1000

# print("welcome to your Acount")
# print("1. Check Balaance")
# print("2. Credit")
# print("3. Deposit")
# print("4. Exit")


# while True : 
#     option = int(input("Select any option 1,2, 3, 4: ")) 


# #balance check hoga
#     if option == 1:
#         print(f"AC Balance : {balance}")

# #AC me paise nikleneg 
#     elif option == 2:
#          credit_amount = int(input("enter creditable amount : "))
         
#          if credit_amount <= balance :
#             balance = balance - credit_amount
#             print(f"amount Credited : {credit_amount}")
#             print(f"Amount balance  : {balance}")
#          else:
#             print("Ac balance is Low")    

   
# #AC me  paise jama honge
#     elif option == 3:
#         deposit_amount = int(input("Enter deposit amount : "))

#         balance = balance + deposit_amount
#         print(f"Amount balance : {balance}")

# #AC se exit hoga 
#     elif option == 4:
#         print("Thanks for visiting")    
#         break

#     else:
#         print("wrong input")  








