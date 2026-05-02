list_items=input("Enter elements seperated by spaces: ").split()
unique_list=[]
for item in list_items:
    if item not in unique_list:
        unique_list.append(item)
print("Original list: ",list_items)
print("List after removing duplicates: ",unique_list)
