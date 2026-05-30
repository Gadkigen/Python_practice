while True:
    try:
        age=int(input("Enter your age: "))
        break
    except ValueError:
        print("invalid input. please enter your age as an whole number.")

print(f"you enterd:{age} years")
