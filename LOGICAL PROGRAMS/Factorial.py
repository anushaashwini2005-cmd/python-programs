num=int(input("enter the number: "))
fact=1
if num<0:
    print("Please enter positive number")
else:
    for i in range(1,num+1):
        fact*=i
    print(f"Factorial of {num} is {fact}")
