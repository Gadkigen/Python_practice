import random
import string

def menu():
    print("\n--- PASSWORD MANAGER---")
    print("1. Save password")
    print("2. View passwords")
    print("3. Generate password")
    print("4. Delete password")
    print("5. Delete all password")
    print("6. Quit")

def save_password():
    website = input("website: ")
    username = input("username: ")
    password = input("password: ")

    with open("password.txt", "a") as file:
        file.write(f"website: {website}\n")
        file.write(f"username: {username}\n")
        file.write(f"password: {password}\n")
        file.write(f"-" * 30 + "\n")

    print("password saved succesfully!")

def view_password():
    try:
        with open("password.txt", "r") as file:
            content = file.read()

            if content.strip() =="":
                print("No password saved yet.")
            else:
                print("\n---SAVED PASSWORD---")
                print(content)

    except FileNotFoundError:
        print("No password file found yet.")


def generate_password(length=10):

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password
print("Generated password:", generate_password())

def delete_password():
    service = input("Enter the service name to delete: ")

    try:
        with open("password.txt", "r") as file:
            lines = file.readlines()

        found = False
        with open("password.txt", "w") as file:
            for line in lines:
                if service.lower() not in line.lower():
                    file.write(line)
                else:
                    found = True

        if found:
            print(f"password for '{service}' deleted successfully!")
        else:
            print("No password found for '{service}'.")

    except FileNotFoundError:
        print("No passwords saved yet.")

def delete_all_password():
    confirm = input("Are you sure you want to delete All passwods? (yes/no): ")
    if confirm.lower() == "yes":
        with open("password.txt", "w") as file:
            file.write("")
        print("All passsword deleted succesfully!")
    else:
        print("Cancelled. no password were deleted.")

while True:
    menu()

    choice = input("Choose an option: ")

    if choice == "1":
        save_password()
    elif choice == "2":
        view_password()
    elif choice == "3":
        print("Generate password:", generate_password())
    elif choice == "4":
        delete_password()
    elif choice == "5":
        delete_all_password()
    elif choice == "6":
        print ("Goodbye!")
        break
