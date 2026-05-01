def check_ecxeption(a,b):
    try:
        res=int(a)/int(b)
    except(ZeroDivisionError,ValueError)as e:
        print("Error occured: ",type(e))
    else:
        print(f"Result={res:4.2f}")
    finally:
        print("Exception of try-catch block is completed")
a=input("Enter first number: ")
b=input("Enter second number: ")
check_ecxeption(a,b)