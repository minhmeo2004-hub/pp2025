import math
from .domains.classes import Student, Course

def input_courses(system):
    course_number = int(input("Number courses: "))
    for i in range(course_number):
        while True:
            course_id = int(input("Course ID: "))
            course_name = input("Course name: ")
            credits = int(input("Credits: ")) 
            print("-------------------------")

            duplicate = False
            for course in system.courses:
                if course_id == course.get_id() or course_name == course.get_name():
                    print("Can not duplicate ID or Name of course")
                    duplicate = True
                    break

            if credits <= 0:
                print("Credit can not be lower than or equal to 0!!")
                duplicate = True
            
            if not duplicate:
                course_infor = Course(course_id, course_name, credits) 
                system.courses.append(course_infor)
                break

def input_student(system):
    student_number = int(input("Number Student: "))
    for i in range(student_number):
        while True:
            student_id = input("StudentID: ")
            duplicate = False
            for student in system.students:
                if student_id == student.get_id():
                    print("Can not duplicate StudentID!!")
                    duplicate = True
                    break
            if not duplicate:
                student_name = input("Student Name:")
                student_dob = input("Enter (DD/MM/YY): ")
                student_infor = Student(student_id, student_name, student_dob)
                system.students.append(student_infor)
                print("-------------------------")
                break

def input_marks(system):
    if not system.courses or not system.students:
        print("Please input courses and students first.")
        return
        
    while True:
        select_course = int(input("Enter CourseID to mark:"))
        found = False
        for course in system.courses:
            if select_course == course.get_id():
                found = True
                break
        if found == False:
            print(f"Cant found COURSE with this ID:{select_course}\nPls Enter ID again")
        else:
            for student in system.students:
                s_id = student.get_id()
                s_name = student.get_name()
                
                mark_input = float(input(f"Mark (will be rounded down):\n{s_name} | {s_id} | "))
                
                while mark_input < 0:
                    print("Mark cant be lower than 0")
                    mark_input = float(input("Pls enter mark that allowed!!\nMark:"))
                
                rounded_mark = math.floor(mark_input * 10) / 10
                system.marks[s_id, select_course] = rounded_mark
                print(f"-> Mark recorded as: {rounded_mark}")
            break