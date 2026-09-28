def add_stu(students):
    stu_id = int(input("Enter student ID: "))
    name = input("Enter student name: ")
    if stu_id in students:
        print("Student exists.")
    else:
        students[stu_id] = name
        print("Student added.")

def remove_stu(students):
    stu_id = int(input("Enter student ID: "))
    if stu_id in students:
        del students[stu_id]
        print("Student removed .")
    else:
        print("Student not found.")

def search_stu(students):
    stu_id = int(input("Enter student ID: "))
    if stu_id in students:
        print("Student ID:", stu_id)
        print("Student Name:", students[stu_id])
    else:
        print("Student not found.")

def view_stu(students):
    if len(students) == 0:
        print("No students.")
    else:
        print("\nStudents In Class:")
        for stu_id, name in students.items():
            print(stu_id, "-", name)