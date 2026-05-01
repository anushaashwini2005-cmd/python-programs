class Book:
    
    # Constructor Dunder Method
    def __init__(self, title, price):
        self.title = title
        self.price = price

    # String Representation
    def __str__(self):
        return f"Book Name: {self.title}, Price: {self.price}"

    # Official Representation
    def __repr__(self):
        return f"Book('{self.title}', {self.price})"

    # Add Two Objects
    def __add__(self, other):
        return self.price + other.price

    # Compare Two Objects
    def __lt__(self, other):
        return self.price < other.price

b1 = Book("Python", 500)
b2 = Book("Advanced Python", 700)
# Calling Dunder Methods
print(b1) 
print(b2)             # __str__
print(repr(b1))        # __repr__
print(b1 + b2)         # __add__
print(b1 < b2)         # __lt__
