import numpy as np

from .input import input_courses, input_student, input_marks
from .output import list_course, list_student, list_display

class System:
    """Class chứa dữ liệu chính của hệ thống."""
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

def cal_GPA(system):
    """Tính GPA trung bình có trọng số cho tất cả sinh viên."""
    for student in system.students:
        student_id = student.get_id()
        marks_ls = []
        credits_ls = []
        
        for course in system.courses:
            course_id = course.get_id()
            key = (student_id, course_id)

            if key in system.marks:
                mark = system.marks[key]
                credits = course.get_credits()
                marks_ls.append(mark)
                credits_ls.append(credits)

        marks_array = np.array(marks_ls)
        credits_array = np.array(credits_ls)

        if len(credits_array) > 0 and np.sum(credits_array) > 0:
            weight_sum = np.sum(marks_array * credits_array)
            total_credits = np.sum(credits_array)
            gpa = weight_sum / total_credits
            student.set_gpa(gpa)
        else:
            student.set_gpa(0.0)

def sort_by_gpa(system):
    """Sắp xếp danh sách sinh viên theo GPA giảm dần."""
    cal_GPA(system)
    system.students.sort(key=lambda s: s.get_gpa(), reverse=True)
    print("\n*** Students sorted by GPA (Descending) ***")


def main():
    system = System()
    
    print("\n--- 1. INPUT COURSES ---")
    input_courses(system)
    
    print("\n--- 2. INPUT STUDENTS ---")
    input_student(system)
    
    print("\n--- 3. INPUT MARKS ---")
    input_marks(system)

    sort_by_gpa(system)
    list_course(system)
    list_student(system)
    list_display(system)

if __name__ == "__main__":
    main()