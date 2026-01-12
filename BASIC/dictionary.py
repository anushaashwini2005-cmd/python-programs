# 1. Creating Dictionary
d = {
    "name": "Anusha",
    "age": 20,
    "course": "BCA"
}
print("Initial Dictionary:", d)

# 2. Accessing Values
print("Name:", d["name"])
print("Age (using get):", d.get("age"))

# 3. Adding & Updating Elements
d["city"] = "Bangalore"
d["age"] = 21
print("After Add & Update:", d)

# 4. Deleting Elements
del d["course"]
print("After Deletion:", d)

# 5. Membership Test (Keys only)
print("Is 'name' key present?", "name" in d)

# 6. Built-in Functions
print("Length:", len(d))
print("Max key:", max(d))
print("Min key:", min(d))
print("Sorted keys:", sorted(d))

# 7. Dictionary Methods
print("Keys:", d.keys())
print("Values:", d.values())
print("Items:", d.items())

d.update({"gender": "Female", "college": "ABC College"})
print("After update:", d)

# 8. Nested Dictionary
student = {
    "name": "Anusha",
    "marks": {
        "maths": 85,
        "cs": 90,
        "physics": 88
    }
}
print("Nested Dictionary:", student)
print("CS Marks:", student["marks"]["cs"])

# 9. Clearing Dictionary
d.clear()
print("After clear:", d)