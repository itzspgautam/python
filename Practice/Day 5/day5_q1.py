class Student:
    def __init__ (self, name, age, roll_no):
        self.name=name
        self.age=age
        self.roll_no=roll_no
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no) 

name = input("Enter your name: ")
age = int(input("Enter your age: "))
roll_no = int(input("Enter your roll number: "))       

student1 = Student(name, age, roll_no)
student1.display()