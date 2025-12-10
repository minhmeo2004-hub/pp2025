def list_course(system):
    print("\n\n")
    print("_____Courses_____")
    for course in system.courses:
        print(course)

def list_student(system):
    print("_____Student (Sorted by GPA) _____")
    for student in system.students:
        print(student)
        
def list_display(system):
    print("_____DISPLAY MARKS_____ ")
    for key, value in system.marks.items():
        print(f"StudentID:{key[0]} | CourseID:{key[1]} | Mark:{value}")