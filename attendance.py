def mark_p(attendance):
    name = input("Enter student name: ")
    if name in attendance:
        attendance[name].append(1)
        print(name, "marked Present.")
    else:
        print("Student not found.")

def mark_a(attendance):
    name = input("Enter student name: ")
    if name in attendance:
        attendance[name].append(0)
        print(name, "marked Absent.")
    else:
        print("Student not found.")

def view_att(attendance):
    if not attendance:
        print("No students present")
        return
    print("\n--- Attendance Record ---")
    for name, records in attendance.items():
        print(name, ":", records)
