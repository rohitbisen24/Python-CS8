# A. Python Basics

# Introduction & Setup
# python setup ✅


# Comments 
# single line #
# multiple line 
"""jkjsdh
lsld
knfdk"""

# Indentation
# name = "zyxhj"
# if 20 < 30 :
#     print()


# First Program & print()
# print("hello")

# run the program
# terminal -> check same folder -> python filename.py

# Variables
name = "connect shiksha"

# name@ = "connect shiksha" ->error
# 1name = "connect shiksha" ->error
# full name  = "connect shiksha" ->error
# if = "connect shiksha" ->error


# Data Types
age = 21 
name = "connect shiksha"
persnt = 76.55
isValue  =  True


# Typecasting
# int -> float 
# num  = 20
# num2 = float(num)
# print(num)
# print(num2)  



# Input & User Interaction — input()
# age = int(input("enter age :  "))  #21
# name = input("enter name :  ")

# Strings 
# name = "rohit bisen"
# print(name)

# String Methods

# print(name.capitalize())

# Operators 
# Arithmetic - +, - * / % // ** 
# num1 = 10 
# num2 = 20
# total  = num1 + num2 
# print(total)

# logic -  and or not 
# comparision - > < => <= == !=

# asigments - = =- =+, =* =/ =%  =// =**
# num1 = 10 
# num1 += 20 #num1 = num1 + 20
# print(num1)

# # if / else 

# if 18>= age:
#     print("ap vote de skte h ")
# else:
#     print("vote nhi de skte ")   


# if 18>= age:
#     print("ap vote de skte h ")

# elif 100>= age:
#     print("ap over age hai  ap vote nhi de skte")
    
# else:
#     print("vote nhi de skte ")

# for Loop - 

# for i in range(2,21,2):
#     print(i)

# while Loop

# i  = 1

# while i < 10 :  # 1 < 10 -> T,  # 2 < 10 -> T,  # 2 < 10 -> T, # 10 < 10 -> F
#     print(i)
#     i +=1

# output : 
# 1 ,2,3,4,5,6,7,8,9

# break 
# continue 
# Pass

# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(i)

# for i in range(1, 11):
#     if i == 5:
#         break
#     print(i)
    
# Nested Conditions
# person_age = int(input("Enter age : "))
# persent10th = int(input("Enter persent : "))


# if person_age >= 18 :
#     if persent10th >=50 :
#         print("vote de skta hai")
#     else:
#          print("vote nhi de skta")     

# else :
#     print("vote nhi de skta")   

# for i in range(1, 4):   #1,2,3  
#     for j in range(3):  #0,1,2
#         print(i)
     
# 1 1 1 - 2 2 2 - 3 3 3



# for i in range(1,4):  #1 , 2  3   ek - ek step chal rha h
#     for j in range(1,4): #1 , 2  3  ek bar me 3 step chal rha
#         print( "*", end = " ")     
#     print()

# """ 
# output
# * * * 
# * * * 
# * * * 
# """

# for i in range(1,4):  #1 , 2  3   ek - ek step chal rha h
#     for j in range(1,4): #1 , 2  3  ek bar me 3 step chal rha
#         print( j, end = " ")     
#     print()

# """ 
# output
# 1 2 3 
# 1 2 3
# 1 2 3 
# """

# List 
# students_list = ["aaryan", "khushi", "zoya", "meeran"]

# print(students_list[1])
# students_list[2] = "Khushi"

# print(students_list)

# students_list.reverse()

# print(students_list)

# students_list.append("rohit")

# print(students_list)

# Tuple

# Set 
# students_set = {"aaryan", "khushi", "zoya", "meeran","zoya" }

# print(students_set)

# students_set.add("rohit")
# print(students_set)

# Dictionary
# student_profile = {
#     "name" : "Aaryan",
#     "age" :  22,
#     "branch" : "Btech",
#     "College" : 'Satpuda'
# } 

# print(student_profile)


#function
# pre define - Print(), type(),...etc
# user Define - programer apn need k according banata hai

# def FunctionName():
    #code ya Logic

# functionName()
# def sum(num1, num2):
#     total = num1+num2
#     print(total)
#     return total

# num1 = int(input()) #2
# num2 = int(input()) #5

# total_amount =sum(num1, num2)

# print(total_amount)

# Normal Function

# Task 1:
# Create a function welcome() that prints:

# Welcome to Python Programming

# Task 2:
# Create a function student_details() that prints:

# Name: Rahul
# Class: 10th
# Course: Python

# def student_details():
#     print("Name: Rahul")
#     print("Name: Rahul")
#     print("Name: Rahul")


# student_details()



# Function with Parameters

# Task 3:
# Create a function add(a, b) that takes two numbers as parameters and prints their sum.

# Task 4:
# Create a function area(length, width) that takes length and width as parameters and prints the area of a rectangle.


# def Area(x,y):
#     area = x * y
#     print(f"area of a rectangle is : {area}")

# length = int(input("enter length :  "))  #22
# width = int(input("enter width :  "))   #44

# Area(length,width)


# Function with Parameters and Return Type

# Task 5:
# Create a function multiply(a, b) that takes two numbers and returns their multiplication. Print the returned value.

# Task 6:
# Create a function calculate_percentage(m1, m2, m3) that takes 3 subject marks and returns the percentage. Print the result.


#file handling 

# file = open("new.txt","x")
# file.write("new file created")
# file.close()

# print("file folder me aa gya hogi")


#Error Handling



#Import and Libraries


# for i in range(1, 11):
#     file = open(f"file_{i}.txt", "w")
#     file.write(f"hello{i}")
#     file.close()


# error handling 

# try
# except

# else

# finally


# lirary





# Import & Libraries

import math

squre = math.sqrt(64)
print(squre)


x = math.ceil(5.1)  #6
y = math.floor(1.8)

print(x) 
print(y)

pi = math.pi

print(pi)






