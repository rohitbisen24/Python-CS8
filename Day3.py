#id and pass login
# ex.  correct id =  rohit@123
# ex.  correct pss =  1234
# ex.  correct number =  123456789
# ex.  correct emial =  rohit@gmail.com

# ---------------------------------

id = input("Enter your id : ")   
email = input("Enter your email : ")   
number = input("Enter your number : ")   
password = input("Enter your pass : ") 

if (id == "rohit@123" or email == "rohit@gmail.com" or number == "123456789" ) and password == "1234":
    print("welcome to your profile....")

else: 
    print("recheck your id or password")      



