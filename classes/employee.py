class employee:
    def __init__(self,name,designation,salary=30000):
        self.name=name
        self.designation=designation
        self.salary=salary
    def display(self):
        print(f"Name of employee is {self.name} , Designation is {self.designation} , Salary is {self.salary}")
employee1=employee("Ram","HR")
employee2=employee("Sam","Manager",45000)
employee3=employee("Ramya","CEO",50000)
employee1.display()
employee2.display()
employee3.display()
