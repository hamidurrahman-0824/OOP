class Student:
    def __init__(self, name, studnt_id):
        self.courses= []
        self.name = name
        self.student_id = studnt_id
    def enroll(self,course):
        if  course not in self.courses:
            self.courses.append(course)
            print('Enrolment Success.')
        else:
            print(f"Not eligible for {course}")       
    def  drop(self,course):
        if course in self.courses:
            self.courses.remove(course)
            print(f"Warning! You dropped {course}")
        else:
            print(f"{course} do not exists in enrolled list")
    def show_courses(self):
        return f"Studnt ID: {self.student_id}\nStudent Name: {self.name}\nEnrolled Course/s:{self.courses}"
class Course(Student):
    def __init__(self, course_name):
        self.course_name = course_name
        self.stdunets = []
        self.courses = []
    def add_course(self,course):
        if course not in self.courses:
            self.courses.append(course)
    def add_student(self,student):
       self.stdunets.append(student)
       print("Student adding success.")
       return self.stdunets
    def remove_student(self,student):
        self.stdunets.remove(student)
        print("Student removal success.")
        return self.stdunets
    def show_students(self):
        print(f"There are {len(self.stdunets)} students enrolled as given below:\n{self.stdunets}")
    def is_student(self, student):
        if student in self.stdunets:
            return True
        else:
            return False
    def __str__(self,student):
        if student.is_student():
            return f"{student} currently enrolled at {self.course_name} "
 
