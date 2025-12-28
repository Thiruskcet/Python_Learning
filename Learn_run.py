exg = "dgbwjkbbc15463627ninisc@"
#String learning------Starting--------
print(exg.isalpha())
print(exg.upper())
print(exg.isalnum())
print(exg.title())
print(exg.replace(exg, "Hello"))
print(exg.title())
print(exg.find('gbw'))
print(len(exg))
print("Easy to \"Learn\"")
print(exg[0:3])
#Constant/Enum learning------Starting--------
from enum import Enum
class color(Enum):
    RED = 1
    GREEN = 2
    ORANGE = 3
print(color.RED)       #color.RED
print(color.RED.name)  #RED
print(color.RED.value) #1
for x in color:
    print(x)
#USER INPUT--------------------Starting------------
#print("\"Enter the input\"")
#Name=input()
#print("The Name is " + Name)
#COntrol statement--------------------Starting------------
x = int(100)
if x > 100:
    print("YES")
elif x < 100:
    print("NO")
elif x <= 100 or x >= 100:
    print(x)
#LIST IN python--------------------Starting------------
List_A = [1, "thiru", 500, "@", " "]
print(" " in List_A) # Search element in List
List_A.extend(["HI"])
List_A.append("Hello")
List_A.insert(3, "Hell")
for x in List_A:
    print(x)
#TUPLES IN python--------Immutable---------Starting------------
name = ("HI", "A", "B", "X", "XYH")
#print(name.sorted()) It will give an Error
#DICTINARIES IN python--------Immutable---------Starting------------
Dogs_={'key':242, 'name':'rocky', 'age':10}
print(Dogs_.keys())
print(Dogs_.values())
#SETS IN python--------Immutable---------Starting------------
set_1 = {"Rockey", "Syd"}
set_2 = {"Rockey"}
intersect = set_1 & set_2
union = set_1 | set_2
difference=set_1 - set_2
print(intersect)
print(union)
print(difference)
print("Thiru" in union)
#Functions IN python-----------------Starting------------
def Fun_test(name_, y):
    if y in name_:
        for index, value in enumerate(name_):
            if value == y:
                return value, 24, "Qualcomm"
    else:
        print("Enter valid Name")
set_={"thiru", "test", "Ajay"}
print("Enter a Name: ")
#y=input()
y="A"
result=Fun_test(set_, y)
print(result)
#LOOPS IN python-----------------Starting------------
list_X=[1,2,3,4,"Thiru"]
Tuble_x=(1,2,3,4,"test")
Disc_x={"a": 1, "b":2, "c":3, "d":"value"}
set_x={1,2,3,"Hello"}
x = 0
while (x+1) <= len(list_X):
    print(list_X[x])
    x=x+1
for x, y in enumerate(Tuble_x):
    print(x,y)
for x, v in Disc_x.items():
    print(f"{x} : {v}")
#CLASSES IN python-----------------Starting------------
class school:
    def __init__(self, name, Grade, rolno):
        self.n = name
        self.G = Grade
        self.r = rolno

    def __str__(self):   
        return (f"Name {self.n} Class {self.G} Roll_No: {self.r}")

    def lkg(self):
        print("LKG student")

state_1 = school("KOWSHIK", "LKG-C", 1856)
print(state_1)
state_2 = school(" ", "ENG-C", "15BB536@skcet")
state_2.name = "thiru"
print(state_2)

class game:
    def __init__(self, Game_name, Game_hour):
        self.GN = Game_name
        self.GH = Game_hour

    def Game_disp(self):
        return (self.GN, self.GH)

game1_data=game("temp_run", 2.5)
game1_data.GH=3.4
print(game1_data.Game_disp())
print(game1_data.GN)

class student_data:
    def __init__(self, std_Name, std_Marks, std_Grade):
        self.s_n=std_Name
        self.s_m=std_Marks
        self.s_g=std_Grade
    def print_std_inf(self):
        return (self.s_n,self.s_m,self.s_g)
Ravi_data = student_data("Ravi",[80,71,90,67,100],10)
Jhon_data = student_data("Jhon",[100,80,71,90,67],10)

print(Ravi_data.print_std_inf())
print(Jhon_data.print_std_inf())

#Libs/import libs IN python-----------------Starting------------
from sub_folder.sub_file import print_data
test_ = print_data(15, 50)

test_.print_info()
