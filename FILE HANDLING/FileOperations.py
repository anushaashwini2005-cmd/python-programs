# 1. Create and Write File
file = open("demo.txt", "w")
file.write("Hello Python\n")
file.write("Welcome to File Handling\n")
file.close()

# 2. Read Full File
file = open("demo.txt", "r")
print("Reading Full File:")
print(file.read())
file.close()

# 3. Read Line by Line
file = open("demo.txt", "r")
print("Reading Line by Line:")
print(file.readline())
print(file.readline())
file.close()

# 4. Append Data
file = open("demo.txt", "a")
file.write("This is appended text\n")
file.close()

# 5. Read After Append
file = open("demo.txt", "r")
print("After Appending:")
print(file.read())
file.close()

# 6. Using with open() Method
with open("demo.txt", "r") as file:
    print("Using with open():")
    print(file.read())

# 7. Rename File
import os
os.rename("demo.txt", "newdemo.txt")

# 8. Delete File
os.remove("newdemo.txt")

print("File Renamed and Deleted Successfully")
