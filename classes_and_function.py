# Wap to implement a Student class with information such as 
# roll_no,name,class,date_of_birth,contact_number,grade
#The information must be entered by the user.

class Student:

    def __init__(self,roll_no,name,student_class,grade,date_of_birth,Contact_number):
        self.roll_no=roll_no
        self.name=name
        self.student_class=student_class
        self.grade=grade
        self.date_of_birth=date_of_birth
        self.contact_number=Contact_number


    def display(self):
        print("Roll_no=",self.roll_no)
        print("name=",self.name)
        print("student_class=",self.student_class)
        print("grde=",self.grade)
        print("date_of_birth=",self.date_of_birth)
        print("contact_number=",self.contact_number)


students=[]
# how many student details we want to entered
number_of_student=int(input("enter the number of student we want to store="))

for i in range(number_of_student):
    roll_no=int(input("enter the roll number="))
    name=input("enter the name=")
    student_class=input("enter the class of the student=")
    grade=input("enter the student grade=")
    date_of_birth=input("enter the date of birth=")
    Contact_number=int(input("enter the contact number of student="))

    s1=Student(roll_no,name,student_class,grade,date_of_birth,Contact_number) # creating s1 object for class Student 
    students.append(s1)



#print(s1.__dict__) # printing the student details in dictionary form .

for student in students:
    student.display()
