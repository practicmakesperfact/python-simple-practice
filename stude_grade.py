def get_float_input(prompt):
    """Function to ensure the input is a valid float."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def get_string_input(prompt):
    while True:
        name = input(prompt)
        if name.isalpha():
            return name
        else:
            print("Please enter a string of chars only")
            continue


courses_value = []
students_info = []


def get_student_history_by_id(student_id):
    student_history = list(
        filter(lambda student: int(student["student_id"]) == int(student_id), students_info))
    print(student_history)
    selection()


def get_all_students_history():
    print(students_info)
    selection()


def calculate_rank():
    rank = 1
    students_info.sort(
        key=lambda student: student["average_grade"], reverse=True)
    for student in students_info:
        student["rank"] = rank
        rank += 1
    print(students_info)
    selection()


def delete_student_by_id(id):
    for index, student in enumerate(students_info):
        if int(student["student_id"]) == int(id):
            students_info.pop(index)
            selection()


def selection():
    selected_number = get_int_input(
        "If you want to continue please enter 1, If you want to get student history by student id enter 2, If you want to get all students history enter 3, If you want the ranks enter 4, If you want delete student history by id enter 5, If you want to quite enter other"
    )
    if selected_number == 1:
        calculate_average_grade()
    elif selected_number == 2:
        student_id = get_int_input("Please enter a student id")
        get_student_history_by_id(student_id)
    elif selected_number == 3:
        get_all_students_history()
    elif selected_number == 4:
        calculate_rank()
    elif selected_number == 5:
        student_id = get_int_input("Enter student ID")
        delete_student_by_id(student_id)
    else:
        with open("demoFile.txt", "a") as f:
            f.write(str(students_info))
        print("Thank you")


def calculate_average_grade():
    student_info = {}
    student_name = get_string_input("Enter student name: ")
    student_id = get_int_input("Enter student id: ")

    is_student_exists = list(filter(
        lambda student: student["student_id"] == student_id, students_info))
    if len(is_student_exists) > 0:
        print("Student already exists")
        selection()
    else:
        num_courses = get_int_input(
            f"{student_name}, please enter the number of courses: ")

        total_grade = 0
        entered_courses = set()

        for i in range(1, num_courses + 1):
            print(f"\nCourse {i}:")

            while True:
                course_name = input("Enter the name of the course: ")
                if course_name in entered_courses:
                    print("This course has already been entered. Please enter a different course.")
                else:
                    entered_courses.add(course_name)
                    break

            grade = get_float_input(f"Enter the grade for {course_name}: ")

            courses_value.append({"Course_name": course_name, "Grade": grade})
            total_grade += grade

        average_grade = total_grade / num_courses

        student_info["student_name"] = student_name
        student_info["student_id"] = student_id
        student_info["Courses_count"] = num_courses
        student_info["courses_name_value"] = courses_value
        student_info["average_grade"] = average_grade

        students_info.append(student_info)

        if average_grade >= 50:
            print(
                f"\nDear student {student_name}, the average grade for {num_courses} courses is: {average_grade:.2f} and the status is 'pass'")
            selection()
        else:
            print(
                f"\nDear student {student_name}, the average grade for {num_courses} courses is: {average_grade:.2f} and the status is 'Fail'. You have to work hard to pass.")
            selection()


calculate_average_grade()
