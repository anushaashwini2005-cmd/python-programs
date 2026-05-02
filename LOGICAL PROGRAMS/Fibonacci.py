num=int(input("Enter the number: "))
a,b=0,1
fib_sequence=[]
while a<=num:
    fib_sequence.append(a)
    a,b=b,a+b
print(f"Fibonacci sequence:{fib_sequence}")
