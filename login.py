import getpass

def login():
    username = input("Username: ")
    password = getpass.getpass("password: ")

    if username == "gad123" and password == "gad@123":
        print("login succesfull")
        return True
    else:
        print("invalid credential!!!")
        return False
    
login()