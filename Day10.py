#while loop - kisi kam ya task ko bar bar dohrane k liye 
            # mainly iska use infinity loop me hot hai 

# rule - start , end , ya wo infinity tk chalge 

#syntex 

# while Condition :
    #while ka block 
    #varibale increment

#  1- 10 table 

# i = 1

# while  i <= 10 :    #11 <= 10 ......10 <= 10 
#     print(i)
#     i+=1


strtTable = int(input("Table strt kaha se kre : ")) 
endTable = int(input("Table end kaha se kre : "))   

#2
#3 
#4
#5

while strtTable <= endTable :   #2 <= 4 = T, #3 <= 4 = T, 4 <= 4 = T,  5 <= 4 = F
    print(f"{strtTable} ka table ")
  
    i = 1
    while  i <= 10 :    #1 <= 10 T....#11 <= 10 F
      print(f"{i} x {strtTable} : {i*strtTable}")   #1 X 2 : 2
      i+=1
    strtTable+=1
    
print("table end ho gya hai")   














