# Typecasting (flaot - int)  ->  datatype ko change krna
#  

# #float
# persent =  76.43

# #float to int 
# updatePersent = int(persent)

# print(persent)
# print(type(persent))   

# print(updatePersent)
# print(type(updatePersent))   

#float
# number =  76

# #int to float
# updateNumber = float(number)

# print(number)
# print(type(number))   

# print(updateNumber)
# print(type(updateNumber))


#operater ->  mathematic calculation perform  krne ya comparisation krne k liye

# 1. athmatic op -  +, -, *, / , %, 

# number1 = int(input("Enter first number : "))   #4
# number2 = int(input("Enter second number : "))   #2

# print(f"{number1} + {number2} : ",number1+number2)  #6
# print(f"{number1} - {number2} : ",number1-number2)   #2
# print(f"{number1} * {number2} : ",number1*number2)   #8

# print(f"{number1} / {number2} : ",number1/number2)   #2.0
# print(f"{number1} % {number2} : ",number1%number2)   #0

# print(f"{number1} // {number2} : ",number1%number2)   #2.4 -> 2
# print(f"{number1} ** {number2} : ",number1%number2)   #4x4 -> 16


# note: input() funtion by defult data string(txt) me leta hai 
# iske liye typecasing ka use krna pdhta hai

# comparision op -  ==, != , >  , < , >= , <=

# number1 = int(input("Enter first number : "))   #4
# number2 = int(input("Enter second number : "))   #2

# print(f"{number1} == {number2} : ",number1 == number2)  #False
# print(f"{number1} != {number2} : ",number1 != number2)  #True
# print(f"{number1} > {number2} : ",number1 > number2)  #True
# print(f"{number1} < {number2} : ",number1 != number2)  #False

# print(f"{number1} >= {number2} : ",number1 != number2)  # 4 >= 2 -> True
# print(f"{number1} <= {number2} : ",number1 != number2)   # 4 <= 2 -> false

# logical op - and(dono condition true) , or(ek condition True) , not

number1 = int(input("Enter first number : "))   #3
number2 = int(input("Enter second number : "))   #7


print(number1 == number2 and number1 < number2 ) #false
# 4 == 2 and  4 < 2    

print(number1 >= number2 or number1 != number2 ) #true
# 3 >= 7 or  3 != 7 

print(not(number1 == number2 and number1 < number2 )) #
# 3 == 7  not  3 < 7 -> false -> true