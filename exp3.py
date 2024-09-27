students={}

num_id=int(input("enter the number of student we want to enter:"))

for i in range(num_id):
    name=input("enter the student name:")
    scores=int(input("enter the student score:"))
    students={'Name':name,'Scores':scores}



for student in students:
    print(students)

