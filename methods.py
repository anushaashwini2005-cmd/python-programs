# Program for all types of methods in Python

class Student:
    
    # Constructor Method
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Instance Method
    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

    # Instance Method with calculation
    def grade(self):
        if self.marks >= 90:
            print("Grade: A")
        elif self.marks >= 75:
            print("Grade: B")
        else:
            print("Grade: C")

    # Class Method
    @classmethod
    def school_name(cls):
        print("School Name: ABC Public School")

    # Static Method
    @staticmethod
    def info():
        print("Static Method: This class stores student details")


# Creating Object
s1 = Student("Anusha", 88)

# Calling Instance Methods
s1.display()
s1.grade()

# Calling Class Method
Student.school_name()

# Calling Static Method
Student.info()
