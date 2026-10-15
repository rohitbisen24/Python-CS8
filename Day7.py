# String -> words y txt ko hi python ne string  bolte h

# String Basics

name = "Rahul Sharma"
# print(name)
# print(type(name))


# String Indexing - konsa character kis index pr hai

#basic structure 
# R  a  h  u  l  _  S  h   a   r   m   a  - charaters(txt)
# 0  1  2  3  4  5  6  7   8   9   10  11   - positive index
#-12                  -5   -4  -3  -2  -1

# print(name[2])
# print(name[8])
# print(name[11])
# print(name[6])
# print(name[-2])


# String Slicing -> string ka ek part print
#varibaleName[strt:end-1]
print(name[2:5])
print(name[-5:-2]) 


# String Methods (upper, lower, strip) -

print(name.upper())
print(name.lower())

name2  =  "    ravi     "
print(name2)
print(name2.strip())


# F-strings Formatting

print(f"heelo {name} how r u")