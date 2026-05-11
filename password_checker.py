common_passwords = ["124567890", "qwertyui", "password"]
special_character = "!@#$%^&*()-=+\\.,<>"
while True:
    score = 0
    password = input("Enter your password: ")

    if len (password)>=8:
        print("Good length")
        score += 1
    else:
        print("Password too short")

    #uppercase cheker
    if any (char.isupper() for char in password):
        print("Has uppercase letter")
        score += 1
    else:
        print("missing uppercase letter")

    if any (char.islower() for char in password):
        print("Has lowercase letter")
        score += 1
    else:
        print("missing lowercase letter")

    if any (char in special_character for char in password):
        print("Has special_character")
        score += 1
    else:
        print("missing special_character")

    if any (char.isdigit() for char in password):
        print("Has a number")
        score += 1
    else:
        print("missing a number")

    if password in common_passwords:
        print("very common password")
        score += 1
    else:
        print("password not common")

    print("\npassword score:", score, "/6")

    if score >= 5:
        print ("very strong password")
    elif score >= 4:
        print("medium password")
    else:
        print("weak password")

    again = input ("Try again? yes/no: ")
    if again == "no":
        break