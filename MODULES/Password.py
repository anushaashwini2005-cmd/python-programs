import re  # pattern matching module
def validate(password):
    if(len(password)>=6 and len(password)<=20 and re.search("[a-z]",password) 
    and re.search("[A-Z]",password) and re.search("[0-9]",password) 
    and re.search("[_@$]",password) and not re.search("/s",password)):
        print("Valid password")
    else:
        print("Invalid password")
password=input("Enter the password: ")
validate(password)