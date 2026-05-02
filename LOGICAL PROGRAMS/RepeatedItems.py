items=input("Enter items seperated by spaces: ")
tuple_items=tuple(items.split())
repeated_items=[]
for item in tuple_items:
    if tuple_items.count(item)>1 and item not in repeated_items:
        repeated_items.append(item)
print(f"Tuple items:{tuple_items}")
if repeated_items:
    print(f"Repeated items in tuple: {tuple(repeated_items)}")
else:
    print(f"No repeated items in tuple")
