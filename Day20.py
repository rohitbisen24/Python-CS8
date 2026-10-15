# file handling - files ko manage krne k liye

# open() - kisi  bhi  file ko first time use krne ya create krne 
# close() - file ko end me close krne k liye
# with... as (keyword) - iska use krne se file close 
# nhi bhi kre to bhi kam chal jata h

# mode
# x	- Create new file
# r - Read
# w	- Write
# a	- Append

# syntex  
# VariableName =open("Filename", "Mode")

# file create
# file = open("Day01.py","x")
# file.close()
# print("file created")

# file write 
# file = open("Day01.py","w")
# file.write("Connect shiksha coding clasess")
# file.close()
# print("file updated")

#file read
# file = open("Day01.py","r")
# data=file.read()
# print(data)
# file.close()
# print("file read")

# file append
# file = open("Day01.py","a")
# file.write("\nbalaghat ")
# file.close()
# print("file me data add ho gya")

# # without close()
with open("Day01.py","a") as file: 
    file.write("\n9131782103")
    print("file updated")



