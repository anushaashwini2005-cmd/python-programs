# Creating a tuple
point = (10, 20)
colors = ("red", "green", "blue")
print(point,colors)

# A tuple with one item must have a trailing comma
single_item = ("apple",) 

# Accessing by index
print(colors[0])   # Output: red

# Slicing
print(colors[1:3]) # Output: ('green', 'blue')

# Negative indexing
print(colors[-1])  # Output: blue

#  Concatenation (Combining)
tuple1 = (1, 2, 3)
tuple2 = ("a", "b")
combined = tuple1 + tuple2  # Result: (1, 2, 3, 'a', 'b')
print(combined)
#  Repetition
repeated = ("Echo",) * 3    # Result: ('Echo', 'Echo', 'Echo')
print(repeated)
#  Membership Testing
fruits = ("apple", "banana", "cherry")
print("apple" in fruits)    # Output: True

#  Length
print(len(fruits))          # Output: 3

numbers = (1, 2, 3, 1, 1, 4)
print(numbers.count(1))  # Output: 3

colors = ("red", "green", "blue", "green")
print(colors.index("green"))  # Output: 1
