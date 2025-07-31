#INITIAL COMMENT FOR FILE CREATION
"""
This script is written for self learn pyhthon concept
this script will simulate university course managment system
Data Structures:

Use a list of dictionaries to store student data.
Use a dictionary of sets to store course enrollments.
Use a tuple to represent immutable course details (course code, name).
Use a dictionary of lists to represent departments and their courses.

"""

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

dprt = {
    "Mathamatics":["MATH101","MATH102"],
    "Computer Science":["CS101","DS101"],
    "Electronics":["ECE101"],
    "Electrical":["EEE101"],
    "Information":["IT101"],
    "Machanical":["MECH101"]
}

print(course,"\n\n\n\n\n",dprt)