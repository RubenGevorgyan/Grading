class Grades:

    def __init__(self, grade):
        self.__grade = grade

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        self.__grade = grade

        minumum=0
        maximum=100

    def check_if_valid(self,grade):
        if(grade<self.minimum or grade>self.maximum):
            print("You have inputted wrong value")
            print("/n Input grade")
            self.set_grade(self,input())


class Assignment:

    minimum=0
    maximum=100

    def __init__(self, name,perc,deadline):
        self.__name = name
        self.__deadline = deadline
        self.__perc = perc
        self.__grade=Grades.get_grade()

    def get_grade(self):
        return self.__grade

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_perc(self):
        return self.__perc

    def set_perc(self, perc):
        self.__perc = perc

    def get_deadline(self):
        return self.__deadline

    def set_deadline(self, deadline):
        self.__deadline = deadline

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def check_if_late(self,deadline):
        if(deadline>self.__deadline):
            self.__status=0
        else:
            self.__status=1
    def check_if_graded(self):
        if (Grades.get_grade()<=100 and Grades.get_grade()>=0):
            return 1
        else:
            return 0


class Course:
    
    def __init__(self, credits,students,code,name,inst_name):
        self.__inst_name=inst_name
        self.__credits = credits
        self.__students = students
        self.__code=code
        self.__name=name
        self.assignments = []

    def get_inst_name(self):
        return self.__inst_name

    def set_inst_name(self, inst_name):
        self.__inst_name = inst_name

    def get_credits(self):
        return self.__credits

    def set_credits(self, credits):
        self.__credits = credits

    def get_students(self):
        return self.__students

    def set_students(self, students):
        self.__students = students

    def get_code(self):
        return self.__code

    def set_code(self, code):
        self.__code = code


class User:
    def __init__(self,name,surname):
        self.__name=name
        self.__surname=surname

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name=name

    def get_surname(self):
        return self.__surname

    def set_surname(self,surname):
        self.__surname=surname


class Student(User):
    def __init__(self,name,surname):
        User.__init__(self,name,surname)
        self.courses = []
        self.grades = []

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name=name

    def get_surname(self):
        return self.__surname

    def set_surname(self,surname):
        self.__surname=surname

    def display_grades(self):
        for grade in self.Grades:
            print (Course.__name__+": "+ Assignment.get_grade()+": "+Student.get_name()+" "+Student.get_surname())


class Lecturer(User):
    def __init__(self,name,surname):
        User.__init__(self,name,surname)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_surname(self):
        return self.__surname

    def set_surname(self, surname):
        self.__surname = surname


class AssignmentGrade:
    def __init__(self, course, assignment,grade):
        self.course = course
        self.assignment = assignment
        self.grade = Grades(grade)
        self.state = 0
        
    def get_course(self):
        return self.course
    
    def set_course(self,course):
        self.course=course

    def get_assignment(self):
        return self.assignment

    def set_assignment(self, assignment):
        self.assignment = assignment

    def get_grade(self):
        return self.grade

    def set_grade(self, grade):
        self.grade = grade

def main():

    c1=Course(3,20,"ENGS115","Data Structures","Satenik")
    asgn1=Assignment("Assignment1",10,"2018-09-16")
    c1.assignments.append(asgn1)
    asggrade1=AssignmentGrade(c1,asgn1,30)
    st1=Student("Ruben","Gevorgyan")
    st1.courses.append(asggrade1)
    st1.display_grades()
    asgn1.set_name("GREATESTASSGNMENTEVER")
    st1.display_grades()
main()
