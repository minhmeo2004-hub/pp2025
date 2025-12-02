students=[]
courses=[]
marks={}            #make dict: (student_id,course_id):mark value


def input_data():
    course_number=int(input("Number courses: "))
    for i in range(course_number):
        while True:
            course_id=int(input("Course ID: "))
            course_name=input("Course name: ")
            print("-------------------------")

            duplicate = False
            for course in courses:
                if course_id == course[0]or course_name==course[1]:
                    print("Can not duplicate ID or Name of course")
                    duplicate = True
                    break
            if not duplicate:
                course_infor=[course_id, course_name]
                courses.append(course_infor)
                break


    student_number=int(input("Number Student: "))
    for i in range(student_number):
        while True:
            student_id=input("StudentID: ")

            duplicate = False
            for student in students:
                if student_id==student[0]:
                    print("Can not duplicate StudentID!!")
                    duplicate = True
                    break
            if not duplicate:
                student_name=input("Student Name:")
                student_dob=input("Enter (DD/MM/YY): ")
                student_infor=[student_id, student_name, student_dob]
                students.append(student_infor)
                print("-------------------------")
                break

    
    while True:
        select_course = int(input("Enter CourseID to mark:"))

        found = False
        for course in courses:
            if select_course ==course[0]:
                found=True
                break
        if found==False:
            print(f"Cant found COURSE with this ID:{select_course}\nPls Enter ID again")
        else:
            for student in students:
                s_id=student[0]
                s_name=student[1]
                mark=float(input(f"Mark:\n{s_name} | {s_id} | "))

                while mark<0:
                    print("Mark cant be lower than 0")
                    mark=float(input("Pls enter mark that allowed!!\nMark:"))
                marks[s_id,select_course]=mark
            break

    
    print("\n\n")
    print("_____Courses_____")
    for course in courses:
        print(course)
    print("_____Student_____")
    for student in students:
        print(student)
    print("_____DISPLAY_____ ")
    for key,value in marks.items():
        print(f"StudentID:{key[0]} | CourseID:{key[1]} | Mark:{value}")

input_data()