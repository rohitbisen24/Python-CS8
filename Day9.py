name = input("Enter your name : ")


print("plese add  your subject marks")

math = int(input("Enter math marks : "))
hindi = int(input("Enter hindi marks : "))
english = int(input("Enter english marks : "))
science = int(input("Enter science marks : "))

total = math + hindi + english + science 
persent = total/4

# note  divide(/) by defult float me result deta h

# 33 kam - fail  
# 33- 50 - pass, B
# 51 - 75 - pass, A
# 76 - 99 - pass, A+

if persent >= 76 and persent <=99 :
    print(f"Hello {name}, your total marks is {total} and persentage is {persent}%. your are pass and A+ grade")

elif persent >= 51 and persent <=75 :
    print(f"Hello {name}, your total marks is {total} and persentage is {persent}%. your are pass and A grade")

elif persent >= 33 and persent <=50 :
    print(f"Hello {name}, your total marks is {total} and persentage is {persent}%. your are pass and B grade")
else:
    print(f"Hello {name}, your total marks is {total} and persentage is {persent}%. your are fail...")


# print(name)
# print(total)
# print(persent)