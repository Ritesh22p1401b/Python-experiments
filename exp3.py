'''students={}

num_id=int(input("enter the number of student we want to enter:"))

for i in range(num_id):
    name=input("enter the student name:")
    scores=int(input("enter the student score:"))
    students={'Name':name,'Scores':scores}



for student in students:
    print(students)'''


# Function to enter student details
def enter_student_details():
    student_dict = {}
    
    while True:
        name = input("Enter the student's name (or 'exit' to finish): ")
        if name.lower() == 'exit':
            break
        
        try:
            score = float(input(f"Enter the score for {name}: "))
            student_dict[name] = score
        except ValueError:
            print("Invalid input. Please enter a numeric score.")
    
    return student_dict

# Function to print students sorted by scores in descending order
def print_sorted_students(student_dict):
    # Sorting the dictionary by score in descending order
    sorted_students = sorted(student_dict.items(), key=lambda item: item[1], reverse=True)
    
    print("\nStudent Details (sorted by scores in descending order):")
    for name, score in sorted_students:
        print(f"Name: {name}, Score: {score}")

# Main function to run the program
def main():
    students = enter_student_details()
    print_sorted_students(students)

if __name__ == "__main__":
    main()

