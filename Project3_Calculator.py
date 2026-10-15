# calculator

# 2 number as user input
# input operator
# operations (+, _ , * ect)
# final output print


num1 =  int(input("enter number : "))
num2 =  int(input("enter number : "))

print("Select Operator")
print("1. +")
print("2. -")
print("3. *")
print("4. /")
print("5. %")


operator =  int(input("Select any option 1,2,3,4,5: ")) 

if  operator == 1:
    print(num1 + num2)

elif operator == 2:
    print(num1 - num2) 

elif operator == 3:
    print(num1 * num2)  

elif operator == 4:
    print(num1 / num2) 

elif operator == 5:
    print(num1 % num2)  

else:
    print("wrong input")