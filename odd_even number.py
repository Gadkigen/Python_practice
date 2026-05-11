number = int(input("Enter a number: "))
if number %2==0 and number >0:
    print(f"{number} is positive even")
elif number %2==1 and number >0:
    print(f"{number} is positive odd")
else:
    print("zero")