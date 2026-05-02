rows=int(input("rows: "))
# prints the box like structure
for i in range(rows):
    print("*" * rows)
print("-"*21)

# prints right angled triangle
for i in range(1,rows+1):
    print("*" *i) 
print("-"*21)   

# prints inverted right angled triangle
for i in range(rows,0,-1):
    print("*" *i) 
print("-"*21)

# prints pyramid
for i in range(1,rows+1):
    print(" "*(rows-i)+"*" *(2*i-1))
print("-"*21)

# prints diamond like shape
for i in range(1,rows+1):
    print(" "*(rows-i)+"*" *(2*i-1))
for i in range(rows-1,0,-1):
    print(" "*(rows-i)+"*"*(2*i-1))


