# Types of Inheritance in Python

# 1. Single Inheritance
class Parent:
    def show(self):
        print("This is Parent class")

class Child(Parent):
    def display(self):
        print("This is Child class")

obj1 = Child()
obj1.show()
obj1.display()


# 2. Multiple Inheritance
class Father:
    def father_skill(self):
        print("Father's skill")

class Mother:
    def mother_skill(self):
        print("Mother's skill")

class Son(Father, Mother):
    pass

obj2 = Son()
obj2.father_skill()
obj2.mother_skill()


# 3. Multilevel Inheritance
class Grandparent:
    def gp_method(self):
        print("Grandparent method")

class Parent2(Grandparent):
    def parent_method(self):
        print("Parent method")

class Child2(Parent2):
    def child_method(self):
        print("Child method")

obj3 = Child2()
obj3.gp_method()
obj3.parent_method()
obj3.child_method()


# 4. Hierarchical Inheritance
class Parent3:
    def common(self):
        print("Common method")

class ChildA(Parent3):
    pass

class ChildB(Parent3):
    pass

obj4 = ChildA()
obj5 = ChildB()

obj4.common()
obj5.common()


# 5. Hybrid Inheritance
class A:
    def method_a(self):
        print("Class A")

class B(A):
    def method_b(self):
        print("Class B")

class C(A):
    def method_c(self):
        print("Class C")

class D(B, C):
    def method_d(self):
        print("Class D")

obj6 = D()
obj6.method_a()
obj6.method_b()
obj6.method_c()
obj6.method_d()