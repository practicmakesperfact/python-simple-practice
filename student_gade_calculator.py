
# print("Student Grade Calculator \n\n")
# while True:
#    totalGrade=0
   
#    name=input("Please Enter Your name: ")
#    courses_number=int(input("how many courses do you take:"))
#    x=0
#    while x<courses_number:
#         grade=float(input(f"please Enter Grade {x+1}(100%): "))
#         totalGrade+=grade
#         x+=1
#    average=(totalGrade/courses_number)
#    if average <50:
#         print(f"{name}, your score is:{average:.2f},you fail exams please read more.")
#    else:
#         print(f"{name},your score is:{average:.2f}, passed!")
#    inputValue=input("Do you want to add other student(y/n)?")
#    if inputValue!='y'and inputValue!='Y':
#        break











#  Ezedin Gashaw ID 4348/14
# Bizualem Abebe  ID  2057/14
# Hamanot Asmare   ID 2594/14















# print("Student Grade Calculator\n")


# while True:
#     total_grade = 0

#     # Input student name
#     name = input("Please enter the student's name: ")
#     if not name:
#         print("Name cannot be empty. Please try again.")
#         continue

#     # Input number of courses
#     try:
#         courses_number = int(input(f"How many courses is the {name} take? "))
#         if courses_number <= 0:
#             print("Number of courses must be a positive integer. Please try again.")
#             continue
#     except ValueError:
#         print("Invalid input. Please enter a valid number.")
#         continue
#     # Collect grades with validation
#     for course in range(1, courses_number + 1):
#         while True:
#             try:
#                 grade = float(input(f"Please enter grade {course} (out of 100): "))
#                 if 0 <= grade <= 100:
#                     total_grade += grade
#                     break
#                 else:
#                     print("Grade must be between 0 and 100. Please try again.")
#             except ValueError:
#                 print("Invalid input. Please enter a number.")
#     # Calculate average and determine result
#     average = total_grade / courses_number
#     if average < 50:
#         print(f"\n{name}, your average score is: {average:.2f}. You failed. Please read more.")
#     else:
#         print(f"\n{name}, your average score is: {average:.2f}. Congratulations, you passed!")
#     # Ask to add another student
#     while True:
#         input_value = input("\nDo you want to add another student? (y/n): ").lower()
#         if input_value in ['y', 'n']:
#             break
#         else:
#             print("Invalid choice. Please enter 'y' for yes or 'n' for no.")
#     if input_value == 'n':
#         break





def get_float_input(prompt):
    """Function to ensure the input is a valid float."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    # Get the student's name
    student_name = input("Enter the student's name: ")

    # Get the number of courses
    num_courses = int(input("Enter the number of courses: "))

    # Initialize total grade sum
    total_grade = 0

    # Iterate for each course
    for i in range(1, num_courses + 1):
        print(f"\nCourse {i}:")
        course_name = input("Enter the name of the course: ")

        # Get the grade for this course, ensuring it's a valid float
        grade = get_float_input(f"Enter the grade for {course_name} (out of 100): ")

        # Add the grade to the total grade
        total_grade += grade

    # Calculate the average grade
    average_grade = total_grade / num_courses

    # Display the average grade and determine pass/fail
    print(f"\n{student_name}, your average grade for {num_courses} courses is: {average_grade:.2f}.")
    if average_grade < 50:
        print("You failed. Please read more.")
    else:
        print("Congratulations, you passed!")

# Check if the script is run directly
if __name__ == "__main__":
    main()