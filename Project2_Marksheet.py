# Students result managemnt 

# students profile data
# persent calculate 
# grade calcualate
# marksheet print


Grade  =  None

Students_Profile = {"name" : "rohit",
                     "Class" : "12th",
                     "School" : "satpuda",
                     "hindi": 50, 
                     "english": 60,
                     "math" : 76}

total = Students_Profile["hindi"] +  Students_Profile["english"] + Students_Profile["math"]

persent = int(total / 3)

if persent >= 76 and persent <=99 :
    Grade = "A+"

elif persent >= 51 and persent <=75 :
    Grade = "A"

elif persent >= 33 and persent <=50 :
    Grade = "B"
else:
    Grade = "fail"


print("student marksheet")
print(f"Name : {Students_Profile["name"]} \nclass : {Students_Profile['Class']} \nSchool : {Students_Profile["School"]} \npersnt : {persent} \nGrade : {Grade}")