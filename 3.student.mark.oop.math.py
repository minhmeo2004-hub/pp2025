import math
import numpy as np

class Student:
    def __init__(self,id,name,dob):
        self.__id =id
        self.__name=name
        self.__dob=dob
        self.__gpa=0.0

    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def set_gpa(self,gpa):
        self.__gpa=gpa
    def get_gpa(self):
        return self.__gpa
    def __str__(self):
        return f"StudentID:{self.__id} | Name:{self.__name} | DoB:{self.__dob} | GPA:{self.__gpa:.2f}"
    
class Course:
    def __init__(self,id,name,credits):
        self.__id=id
        self.__name=name
        self.__credits=credits

    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_credits(self):
        return self.__credits
    def __str__(self):
        return f"courseID:{self.__id} | CourseName:{self.__name} | Credits:{self.__credits}"
    
class System:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def input_courses(self):
        course_number=int(input("Number courses: "))
        for i in range(course_number):
            while True:
                course_id=int(input("Course ID: "))
                course_name=input("Course name: ")
                credits = int(input("Cresdits: "))
                print("-------------------------")

                duplicate = False
                for course in self.courses:
                    if course_id == course.get_id() or course_name==course.get_name():
                        print("Can not duplicate ID or Name of course")
                        duplicate = True
                        break

                if(credits<0):
                    print("Credit can be lower than 0!!")
                    duplicate=True

                if not duplicate:
                    course_infor= Course(course_id, course_name,credits)
                    self.courses.append(course_infor)
                    break
    
    def input_student(self):
        student_number=int(input("Number Student: "))
        for i in range(student_number):
            while True:
                student_id=input("StudentID: ")
                duplicate = False
                for student in self.students:
                    if student_id== student.get_id():
                        print("Can not duplicate StudentID!!")
                        duplicate = True
                        break
                if not duplicate:
                    student_name=input("Student Name:")
                    student_dob=input("Enter (DD/MM/YY): ")
                    student_infor= Student(student_id, student_name, student_dob)
                    self.students.append(student_infor)
                    print("-------------------------")
                    break

    def input_marks(self):
        while True:
            select_course = int(input("Enter CourseID to mark:"))
            found = False
            for course in self.courses:
                if select_course ==course.get_id():
                    found=True
                    break
            if found==False:
                print(f"Cant found COURSE with this ID:{select_course}\nPls Enter ID again")
            else:
                for student in self.students:
                    s_id=student.get_id()
                    s_name=student.get_name()
                    mark=float(input(f"Mark:\n{s_name} | {s_id} | "))
                    while mark<0:
                        print("Mark cant be lower than 0")
                        mark=float(input("Pls enter mark that allowed!!\nMark:"))
                    self.marks[s_id,select_course]=mark
                break
    
    def cal_GPA(self):
        for student in self.students:
            student_id=student.get_id()
            marks_ls=[]
            credits_ls=[]
            for course in self.courses:
                course_id=course.get_id()
                key=(student_id,course_id)

                if key in self.marks:
                    mark=self.marks[key]
                    credits=course.get_credits()
                    marks_ls.append(mark)
                    credits_ls.append(credits)

            marks_array=np.array(marks_ls)
            credits_array=np.array(credits_ls)

            if len(credits_array)>0 and np.sum(credits_array)>0:
                weight_sum=np.sum(marks_array*credits_array)
                total_credits=np.sum(credits_array)
                gpa=weight_sum/total_credits
                student.set_gpa(gpa)
            else:
                student.set_gpa(0.0)

    def sort_by_gpa(self):
        self.cal_GPA()
        self.students.sort(key=lambda s: s.get_gpa(), reverse=True)
        print()

    def list_course(self):
        print("\n\n")
        print("_____Courses_____")
        for course in self.courses:
            print(course)
    def list_student(self):
        print("_____Student_____")
        for student in self.students:
            print(student)
    def list_display(self):
        print("_____DISPLAY_____ ")
        for key,value in self.marks.items():
            print(f"StudentID:{key[0]} | CourseID:{key[1]} | Mark:{value}")

system= System()
system.input_courses()
system.input_student()
system.input_marks()
system.sort_by_gpa()
system.list_course()
system.list_student()
system.list_display()