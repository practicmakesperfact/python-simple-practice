
# print("  Student Grade Calculator \n\n")
# while True:
#    totalGrade=0
   
#    name=input("Please Enter Your name: ")
#    courses_number=int(input("how many courses do you take:"))
#    x=0
#    while x<courses_number:
#         grade=float(input("please Enter Each Grade(100%): "))
#         totalGrade+=grade
#         x+=1
#    average=totalGrade/courses_number
#    if average>=90:
#         grade="A"
#    elif average >=80 and average <90:
#         grade="B"
#    elif average >=70 and average <80:
#         grade= "C"
#    elif average >=50 and average <70:
#         grade ="D"
#    else:
#         grade = "F"
#    if grade == "F":
#         print(f"{name}, your score is:{average}, and your grade is: {grade}, you fail exams please read more.")
#    else:
#         print(f"{name},your score is:{average}, and your grade is: {grade} passed!")
#    inputValue=input("Do you want to add other student(y/n)?")
#    if inputValue!='y'and inputValue!='Y':
#        break

while True:
     name = input("Enter your name: ")
     totalGrade=0
     n_courses =int(input("how many courses you take: "))
     x=0

     while x < n_courses:
          grade = float(input("Enter each grade (100%): "))
          totalGrade+=grade
          x+=1

     average=totalGrade/n_courses
     if average >=50:
       print(f"{name} , your score is {average}, you pass!")
     else:
          print(f"{name} , your score is {average},you failed! please read more.")

     inputvalue = input("Do you add an other student? (y/n): ")
     if inputvalue!='y' and inputvalue!='Y':
            break
 