# take input of 3 numbers and print which number  is user enter ex. positive, nagetive, or zero

# def Comparision(num):
#     if num > 0 :
#         print("positive")
#     elif num < 0 :
#         print("Negitive")
#     else : 
#         print("zero")        

# num = int(input("enter any number : ")) #12
# Comparision(num)

# take input of 3 numbers and print average

# def avg(num1, num2, num3):
#     avg = num1+ num2 +num3 
#     Final_avg = int(avg/3)
#     return Final_avg

# num1 = int(input("enter any number : "))
# num2 = int(input("enter any number : ")) 
# num3 = int(input("enter any number : "))

# Average = avg(num1, num2, num3)
# print(Average)

# -----------------------------------------------------------

# CS8 Python – Function Practice Tasks

# 1. Basic Function
# Task 1:
# Create a function hello() that prints:
# Hello, Python!

# Task 2:
# Create a function welcome() that prints your Name, Class and School.

# 2. Function with Parameters
# Task 3:
# Create a function add(a, b) that takes two numbers and prints their sum.

# Task 4:
# Create a function square(num) that takes a number and prints its square.


# 3. Function with Multiple Parameters

# Task 5:
# Create a function student(name, age, class_name) that takes 3 parameters and prints the student's details.

# Task 6:
# Create a function calculate(a, b, c) that takes 3 numbers and prints their total.

# 4. Function with Return Value

# Task 7:
# Create a function add(a, b) that takes two numbers and returns their sum. Print the returned value.

# Task 8:
# Create a function square(num) that takes a number and returns its square. Print the returned value.

# 1. Create a function calculate_result(m1, m2, m3) that takes marks of 3 subjects and returns:
# * Total marks
# * Average marks
# * Result (Pass/Fail)
# Pass if average is 40 or above.

# 2. Create a function find_largest(a, b, c) that takes 3 numbers and returns the largest number.


# price = int(input("enter item price  : ")) #100

# discount_amount = price *10 /100
# print(f"discount amount : {discount_amount}")

# final_price = price - discount_amount
# print(f"final amount : {final_price}")


def  discount_cal(price, discount_persent):
    discount_amount = price *discount_persent /100
    final_price = price - discount_amount
    return final_price


price = int(input("enter item price  : ")) #100
discount_persent = int(input("enter discount persent   : ")) #15

final_discounted_price = discount_cal(price, discount_persent)
print(f"final amount : {final_discounted_price}")