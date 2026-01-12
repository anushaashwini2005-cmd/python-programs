# Creating a list
fruits = ["apple", "banana", "cherry"]

# Accessing elements (Zero-indexed)
print(fruits[0])   # Output: apple
print(fruits[-1])  # Output: cherry (last item)

# Slicing [start:stop:step]
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4]) # Output: [1, 2, 3]

# Adding to the end
fruits.append("orange")
print(fruits)

# Inserting at a specific index
fruits.insert(1, "mango") # Inserts at index 1
print(fruits)
# Joining two lists
more_fruits = ["pear", "grape"]
fruits.extend(more_fruits)
print(fruits)
# Changing a value
fruits[0] = "strawberry"
print(fruits)
# Remove by value (removes first occurrence)
fruits.remove("banana")
print(fruits)
# Remove by index (and returns the item)
popped_item = fruits.pop(2)
print(fruits)
# Deleting using 'del' keyword
del fruits[0]
print(fruits)

# Reversing the order
fruits.reverse()
print(fruits)

# Clearing the entire list
fruits.clear()
print(fruits)