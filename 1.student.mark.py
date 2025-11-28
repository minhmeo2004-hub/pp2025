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
                break

    print("-------------------------")
    select_course=input("Enter CourseID to mark: ")
    found_course = True
    for course in courses:
        if(select_course==courses[0]):
            found_course=True
            break
        if not found_course:
            print(f"There is no CourseID:{select_course} in Courses!!")
            return
    for student in students:
            lowest_mark =0
            mark=float(input(f"Mark for ID:{student_id} is "))
            if mark <0:
                print("Mark lowest allow is 0!!")
            while mark<lowest_mark:
                mark=float(input("Pls enter mark allowed!!\nMark:"))
                if mark>=lowest_mark:
                    break

            marks[student_id,select_course]=mark

    
    print("-+--+-COURSES-+--+-")
    print(courses)
    print("-+--+-students-+--+-")
    print(students)
    print("--------------------")
    for i in range(student_number):
        print(f"Mark:{marks}")


input_data()