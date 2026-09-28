def attendance_percentage(records):
    t_days = len(records)
    if t_days == 0:
        return 0
    p_days = sum(records)
    percentage = (p_days / t_days) * 100
    return percentage


def at_percent(attendance):
    print("----- Attendance Percentage Of Students -----")
    for name, records in attendance.items():
        percentage = attendance_percentage(records)
        print(f"{name}: {percentage:.2f}%")


def analyze_attendance(attendance):
    print("\n----- Attendance Analysis Of Students -----")
    for name, records in attendance.items():
        percentage = attendance_percentage(records)
        if percentage >= 75:
            status = "Eligible"
        else:
            status = "Not Eligible"
        print(f"{name}: {percentage:.2f}% - {status}")


def highest(attendance):
    high_stu = ""
    high_per = -1
    for name, records in attendance.items():
        percentage = attendance_percentage(records)
        if percentage > high_per:
            high_per = percentage
            high_stu = name
    if high_stu != "":
        print(
            f"Highest Attendance: {high_stu} "
            f"({high_per:.2f}%)"
        )
    else:
        print("No attendance records available.")


def lowest(attendance):
    low_stu = ""
    low_per = 101
    for name, records in attendance.items():
        percentage = attendance_percentage(records)
        if percentage < low_per:
            low_per = percentage
            low_stu = name
    if low_stu != "":
        print(
            f"Lowest Attendance: {low_stu} "
            f"({low_per:.2f}%)"
        )
    else:
        print("No attendance records available.")