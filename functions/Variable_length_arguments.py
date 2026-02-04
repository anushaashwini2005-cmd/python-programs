def find_max(*num):
    max_val=num[0]
    for n in num:
        if n>max_val:
            max_val=n
    return max_val
print(f"Maximum number is : {find_max(4,7,2,9,1,25)}")



def employee(id,**info):
    print("Id: ",id)
    for k,v in info.items():
        print(k,":",v)
employee(101,Name="Ram",Salary=45000,City="Mysore")
