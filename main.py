import stu_manage
import attendance
import att_analyse

def main():

    while True:

        print("""\n
==============================================
    STUDENT ATTENDANCE MANAGEMENT SYSTEM
==============================================""")

        print("1. Management Of Students")
        print("2. Management Of Attendance ")
        print("3. Attandance Analysis")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            while True:

                print("\n---------- MANAGE STUDENTS ----------")
                print("1. Add Student")
                print("2. Remove Student")
                print("3. Search Student")
                print("4. View All Students")
                print("5. Back to Menu")

                option = input("\nEnter your choice: ")

                if option == "1":
                    stu_manage.add_stu(stu_data)

                elif option == "2":
                    stu_manage.remove_stu(stu_data)

                elif option == "3":
                    stu_manage.search_stu(stu_data)

                elif option == "4":
                    stu_manage.view_stu(stu_data)

                elif option == "5":
                    for student_id, name in stu_data.items():
                        attendance[name] = []
                    break

                else:
                    print("Invalid")

        elif choice == "2":

            while True:

                print("\n---------- MANAGE ATTENDANCE ----------")
                print("1. Mark Present")
                print("2. Mark Absent")
                print("3. View Attendance")
                print("4. Back to Menu")

                option = input("\nEnter your choice: ")

                if option == "1":
                    attendance.mark_p(attendance)

                elif option == "2":
                    attendance.mark_a(attendance)

                elif option == "3":
                    attendance.view_att(attendance)

                elif option == "4":
                    break

                else:
                    print("Invalid")

        elif choice == "3":

            while True:

                print("\n---------- ANALYSIS ----------")
                print("1. Attandance Percentage")
                print("2. Eligibility To Pass(75%)")
                print("3. Highest Attendance")
                print("4. Lowest Attendance")
                print("5. Back to Menu")

                option = input("\nEnter your choice: ")

                if option == "1":
                    att_analyse.at_percent(attendance)

                elif option == "2":
                    att_analyse.analyze_attendance(attendance)

                elif option == "3":
                    att_analyse.highest(attendance)

                elif option == "4":
                    att_analyse.lowest(attendance)

                elif option == "5":
                    break

                else:
                    print("Invalid")

        elif choice == "4":

            print("\nThank you for using Student Attandance Management System!")
            break

        else:

            print("\nInvalid . Please enter 1, 2, 3 or 4.")

stu_data={}
attendance={}
main()
