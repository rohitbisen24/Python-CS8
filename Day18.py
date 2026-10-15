#Error Handling - error handing code k kisi ek part me aaye error 
# ko handle krke pura code sahi se chalata h

# try - error wala yaha likhte hai
# except - agr error aa gya to fir except run hota h
# else -  age error aaya hi nhi tb yr code chlage
# finally - ye hamesha chlega 


try:
    num = int(input("enter any number : "))  
except:    
    print("Apka input wrong hai please enter integer input ex. 1234: ")

else : 
    print("error nhi aaya ")

finally:
    print("ye hamesha run hota h")


# try: 
#     num1 = int(input("enter any number : "))    # 3
#     num2 = int(input("enter any number : "))    # 0

#     op = input("Enter Operator ex. +, _ , *, / : ")   # /

#     if op == "+":
#         print(num1 + num2)

#     elif op == "-" :
#         print(num1 - num2)

#     elif op == "*" :
#         print(num1 * num2)

#     elif op == "/" :
#         print(num1 / num2)
#     else:
#         print("invaild OP")    

# except :
#     print("undefine")

    

    









