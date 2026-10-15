# asignment op - =,  +=, -=, *=, /=, %=

age = 21

number1 = int(input("Enter any number : ")) #5

# number1+=15 
# #number1 = number1 +  15
# # number1 = 5 + 15 =>  20

# number1-=15 
# #number1 = number1- 15
# # number1 = 10 - 15 => -5

# number1*=5
# #number1 = number1 * 15
# # number1 = 10 * 15 => 25

# Identity Operators -   is , is not
x = ["apple", "banana"]

#x k type list
#x ka adress 12321xcdc
#variable name  is x
#adress alg hota hai or variable ka value alg hota hai

y = ["apple", "banana"]
z = x  #z ke ander x ki value hai

#ye varible k address ko check krta hai
print(x is z)   #true
print(x is y)   #false

#ye variable k value ko check krta h
print(x == y)   #true

# Membership Operators - in , in not

fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)  #true
print("banana" not in  fruits)  #false


