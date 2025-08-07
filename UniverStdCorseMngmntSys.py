#INITIAL COMMENT FOR FILE CREATION
"""
This script is written for self learn pyhthon concept
this script will simulate university course managment system
Data Structures:

Use a tuple to represent immutable course details (course code, name).
Use a dictionary of lists to represent departments and their courses.
Use a list of dictionaries to store student data.
Use a dictionary of sets to store course enrollments.


🔁 Data Manipulation & Queries
Find all students enrolled in a specific department.

Input: Department name
Output: List of student names
List all courses a student is enrolled in, with course names.

Input: Student ID or name
Output: Course codes and names
Find the most popular course (with the highest number of enrollments).

List students who are enrolled in more than 2 courses.

🧠 Intermediate Python Concepts
Add a new student and update all relevant data structures.

Input: Student ID, name, and course list
Remove a student and update enrollments accordingly.

Move a course from one department to another.

Detect and list students enrolled in courses from multiple departments.

📊 Data Analysis & Visualization (Optional with matplotlib/pandas)
Visualize the number of students per course using a bar chart.

Pie chart of student distribution across departments.

🧪 Advanced Challenges
Simulate course registration with constraints:
Max 3 courses per student
No duplicate enrollments
Export student data to a CSV file.

Import student data from a CSV file and update the system.

Build a simple CLI menu to interact with the system.

"""
#list of tuple
course = [
    ("ECE101","Electronics"),
    ("EEE101","Electrical"),
    ("CS101","Computer Science"),
    ("MECH101","Machanical"),
    ("IT101","Information Technology"),
    ("DS101","Data Science"),
    ("MATH101","Maths_leaner"),
    ("MATH102","Maths_Calc")

]

#dictinary of list
dptr_list = {
    "Mathamatics":["MATH101","MATH102"],
    "Computer Science":["CS101","DS101"],
    "Electronics":["ECE101"],
    "Electrical":["EEE101"],
    "Information":["IT101"],
    "Machanical":["MECH101"]
}
# list of dictinary
student_data =[
    {"id":"A001","name":"Sharan", "course":["MATH102","MATH101"]},
    {"id":"A002","name":"Sham", "course":["DS101"]},
    {"id":"A003","name":"Arun", "course":["CS101","MATH101"]},
    {"id":"A004","name":"Rahul", "course":["MATH102","IT101"]},
    {"id":"A005","name":"Ranjith", "course":["MATH102","MECH101"]},
    {"id":"A006","name":"vinith", "course":["MECH101"]},
    {"id":"A007","name":"lalith", "course":["ECE101","IT101"]},
    {"id":"A008","name":"karthi", "course":["ECE101","MATH101"]},
    {"id":"A009","name":"Naveen", "course":["EEE101","MATH101"]},
    {"id":"A010","name":"Ravi", "course":["EEE101","MATH101"]},
    {"id":"A011","name":"Thiru", "course":["DS101","ECE101"]}
]
# print(studen_data[0]["course"][0])

course_entrolment = {
    "ECE101":{"A007","A008","A011"},
    "EEE101":{"A009","A010"},
    "CS101":{"A003"},
    "MECH101":{"A005","A006"},
    "IT101":{"A004","A007"},
    "DS101":{"A002","A011"},
    "MATH101":{"A001","A003","A008","A009","A010",},
    "MATH102":{"A004","A005"},
}


#Find all students enrolled in a specific department.
def FindAllStudent_dptr(dptr_name:str):
    if dptr_name not in dptr_list:
        print(f"The {dptr_name} department is not available in this university")
#get the list of couse available in a department
    else:
        dptr = set(dptr_list[dptr_name])
        student_name = [
            x["name"] for x in student_data if any(code in dptr for code in x["course"] )
        ]
    for name in student_name:
        print(f"{dptr_name} is opted by {name}")

# Input: Student ID or name
# Output: Course codes and names
# Find the most popular course (with the highest number of enrollments).

def ToFindStuden_info(id:str = None ,student_name:str = None):
    for student in student_data:
        if id!=None or student_name!=None:
            if (id == student["id"] ) or (student_name == student["name"] ):
                data=[student["course"]] #example data = [['DS101', 'ECE101']]

    match_course = (dl in data for dl in dptr_list)
    print(match_course)
                    # print(f"The student name is {student['name']}")



ToFindStuden_info(None,"Thiru")
#FindAllStudent_dptr("Mathamatics")