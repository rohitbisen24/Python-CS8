# 🔹 Task 1
# Write a program to print the table of 2 using a while loop.

# Example:
# 2 x 1 = 2
# 2 x 2 = 4
# ...
# 2 x 10 = 20

# rule - start , end ya wo infinity tk chalge 

# steps = 2

# while steps <= 10 :   #1 <= 10 - T
#     print(steps*2, end=", ")
#     steps+=1


number =int(input("enter any number : "))  #123


# strt value/point 
# condition
# variable increment

count = 0

while number > 0 :
    number = number // 10  
    count+=1 

print(f"total digits : {count}")


# break  -> loop ko rokne k liye
# continue  -> kisi ek step ko skip krne


# strt value/point 
# condition
# variable increment

# i = 1

# while  i <= 10 :

#     if i == 5 :
#         break

#     print(i)
#     i+=1


i = 1

while  i <= 10 :  
# 1 <= 10 , 2 <= 10 3 <= 10 4 <= 10 5 <= 10 6 <= 10 7 <= 10 7 <= 10 7 <= 10 7 <= 10
    
    if i == 7:  # 1 == 7 , 2 == 7
        i+=1
        continue

    print(i, end=", ")
    i+=1

# Output - 1 2 3 4 5 6 8 9 10    