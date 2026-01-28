num=int(input("enter number: "))
match num:
    case n if n>0:
        print("positive")
    case n if n<0:
        print("negative")
    case _:
        print("zero")