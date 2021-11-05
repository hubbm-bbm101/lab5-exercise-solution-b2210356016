def valid_email_check(email):
    if "@" in email :      
        if "." in email :
            return True
        else:
            return False
    else:
        return False
        
x=input("Enter an email:")
while not valid_email_check(x):
    print("Sorry,your email is not valid")
    x=input("Try again,Enter an email:")

print("Thank you, your email",x,"is valid")
