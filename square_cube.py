def square_cube(num):
    return num**2,num**3
num=int(input("Enter a number: "))
sq,cu=square_cube(num)
print("Square: ",sq)
print("Cube: ",cu)