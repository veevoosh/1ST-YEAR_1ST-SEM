prelim = int(input("Enter Prelim Grade: "))

midterm = int(input("Enter Midterm Grade: "))

final = int(input("Enter Final Grade: "))

ave_grade = round((prelim + midterm + final) / 3)

if ave_grade <= 74 :
    print("Grade is:" , ave_grade)
    print("The equivalent letter grade of" , ave_grade , "is F")

elif ave_grade <= 82 :
    print("Grade is:" , ave_grade)
    print("The equivalent letter grade of" , ave_grade , "is D")

elif ave_grade <= 89 :
    print("Grade is:" , ave_grade)
    print("The equivalent letter grade of" , ave_grade , "is C")

elif ave_grade <= 94 :
    print("Grade is:" , ave_grade)
    print("The equivalent letter grade of" , ave_grade , "is B")

else :
    ave_grade <= 100
    print("Grade is:" , ave_grade)
    print("The equivalent letter grade of" , ave_grade , "is A")
