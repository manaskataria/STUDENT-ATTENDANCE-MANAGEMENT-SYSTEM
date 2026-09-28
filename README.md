# Student Attendance Management System

## 1. Project Title

**Student Attendance Management System**

## 2. Overview of the Project

The Student Attendance Management System is a simple console-based Python application for managing student information and attendance records.

The project is divided into separate Python modules so that student management, attendance management, and attendance analysis can be handled independently. The main program provides a menu-driven interface through which the user can access these functions.

The system allows the user to add, remove, search, and view students, record attendance, view attendance records, calculate attendance percentages, check eligibility based on a 75% attendance requirement, and identify the students with the highest and lowest attendance.

## 3. Features

### Student Management
- Add a student using a student ID and name.
- Remove an existing student.
- Search for a student using the student ID.
- View all registered students.

### Attendance Management
- Mark a student as Present.
- Mark a student as Absent.
- View attendance records of students.

### Attendance Analysis
- Calculate the attendance percentage of each student.
- Check whether a student meets the 75% attendance requirement.
- Find the student with the highest attendance.
- Find the student with the lowest attendance.

### Menu-Driven Interface
- Main menu for accessing different parts of the system.
- Separate menus for student management, attendance management, and attendance analysis.
- Option to return to the previous menu or exit the program.

## 4. Technologies / Tools Used

- **Python 3**
- Python functions
- Lists
- Dictionaries
- `if-elif-else` statements
- `for` and `while` loops
- Python modules
- Console input/output
- Git and GitHub for project version control

## 5. Project Structure

```text
Student-Attendance-Management-System/
│
├── main.py
├── stu_manage.py
├── attendance.py
├── att_analyse.py
├── README.md
└── statement.md
```

### Module Description

| File | Purpose |
|---|---|
| `main.py` | Controls the main menu and connects all modules |
| `stu_manage.py` | Handles adding, removing, searching, and viewing students |
| `attendance.py` | Handles marking and viewing attendance |
| `att_analyse.py` | Calculates attendance percentages and performs attendance analysis |
| `README.md` | Contains project documentation |
| `statement.md` | Contains the project problem statement and scope |

## 6. Steps to Install & Run the Project

### Prerequisites

Make sure **Python 3** is installed on your computer.

Check Python using:

```bash
python --version
```

If the command does not work, try:

```bash
python3 --version
```

### Step 1: Clone the Repository

```bash
git clone <your-github-repository-link>
```

### Step 2: Open the Project Folder

```bash
cd Student-Attendance-Management-System
```

### Step 3: Run the Main Program

```bash
python main.py
```

The program will display the Student Attendance Management System menu.

## 7. Instructions for Testing

The project can be tested through the options provided in the console menu.

### Test 1: Add Student

1. Run `main.py`.
2. Select **1. Management Of Students**.
3. Select **1. Add Student**.
4. Enter a student ID.
5. Enter the student's name.
6. Use **View All Students** to verify that the student was added.

### Test 2: Search Student

1. Open **Management Of Students**.
2. Select **Search Student**.
3. Enter an existing student ID.
4. Verify that the student's ID and name are displayed.

### Test 3: Remove Student

1. Open **Management Of Students**.
2. Select **Remove Student**.
3. Enter the ID of an existing student.
4. Verify that the student is removed.
5. Use **View All Students** to confirm.

### Test 4: Mark Attendance

1. Add at least one student.
2. Return to the main menu.
3. Select **Management Of Attendance**.
4. Select **Mark Present** or **Mark Absent**.
5. Enter the student's name.
6. Select **View Attendance** to verify the recorded attendance.

### Test 5: Attendance Analysis

1. Record several Present and Absent entries.
2. Open **Attendance Analysis**.
3. Check the attendance percentage.
4. Check the eligibility result.
5. Test the highest and lowest attendance options.

### Test 6: Invalid Menu Input

Enter a value other than the available menu options and verify that the program displays an invalid-choice message instead of terminating immediately.

## 8. Attendance Calculation

The attendance percentage is calculated using:

```text
Attendance Percentage = (Present Days / Total Days) × 100
```

The project uses **75%** as the attendance eligibility requirement.

For example:

```text
Present Days = 8
Total Days   = 10

Attendance Percentage = (8 / 10) × 100
                       = 80%
```

## 9. Screenshots

Screenshots are optional but recommended for the GitHub repository.

Suggested screenshots:

1. Main menu
2. Student management menu
3. Student details after adding a student
4. Attendance records
5. Attendance percentage and analysis

Add screenshots to the repository and reference them here, for example:

```markdown
![Main Menu](screenshots/main-menu.png)
```

## 10. Limitations

- Data is stored only while the program is running.
- The project does not currently use a database.
- The interface is console-based.
- Attendance is recorded using student names.
- Advanced authentication and user accounts are not included.

## 11. Future Improvements

Possible future improvements include:

- Saving student and attendance data permanently.
- Using a database for storing records.
- Adding date-wise attendance.
- Adding student details such as course and semester.
- Adding a graphical user interface.
- Adding better input validation.
- Generating attendance reports.

## 12. Project Purpose

This project is intended as a Python programming project for practising functions, dictionaries, lists, loops, conditional statements, modular programming, and basic data processing.
