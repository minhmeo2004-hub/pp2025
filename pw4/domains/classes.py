class Student:
    def __init__(self, id, name, dob):
        self.__id = id
        self.__name = name
        self.__dob = dob
        self.__gpa = 0.0

    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def set_gpa(self, gpa):
        self.__gpa = gpa
    def get_gpa(self):
        return self.__gpa
    def __str__(self):
        return f"StudentID:{self.__id} | Name:{self.__name} | DoB:{self.__dob} | GPA:{self.__gpa:.2f}"
    
class Course:
    def __init__(self, id, name, credits):
        self.__id = id
        self.__name = name
        self.__credits = credits

    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_credits(self):
        return self.__credits
    def __str__(self):
        return f"courseID:{self.__id} | CourseName:{self.__name} | Credits:{self.__credits}"