# TOPIC - Multi-level Inheritance occure when a child class become parent of another child class

#parent class
class school:
    school_name="School A"
    school_location="Delhi"
    print("Welcome")

#child class of school A
class class_room(school):
    classroom_no="9"   # ask how to input from the user
    def school(self):
        print(f"School_name: {self.school_name}\nSchool_Location: {self.school_location}\n")

#class derived from class class_room
class student(class_room):
    def __init__(self,name,section,class_):
        self.name=name
        self.section=section
        self.class_=class_
    def student(self):
        print(f"Total no of classrooms are: {self.classroom_no}\n")
        print(f"Student-name: {self.name}\nStudent-Section: {self.section}\nStudent-age: {self.class_}\n")

c1 = class_room()
c1.school()

st1 = student("John","Science","12th")
st1.student()

st2 = student("Doe","Commerece","11th")
st2.student()