balance = 20000
attempt = 0
correct_pin = "!@#$%"
running = True

while running:
    pin = input("Enter your pin: ")
    if pin == correct_pin:
        print("✅Correct pin!!")
        while True:
            print("----MENU---")
            print("1. Check balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Quit")

            choice = input("Enter your choice: ")
            if choice == "1":
                print(f"Your balance is  $ {balance}")
            elif choice == "2":
                amount = int(input("Enter amount to deposit: "))
                balance = balance + int(amount)
                print(f"Your balance is $ {balance}")
            elif choice =="3":
                amount = int(input("Enter amount to withdraw: "))
                if amount > balance:
                    print("Insufficient funds")
                else:
                    balance = balance - int(amount)
                    print(f"Your balance is $ {balance}")
            else:
                choice == "4"
                print("👋Goodbye!!")
                running = False
                break

    elif pin != correct_pin:
        attempt = attempt +1 
        if attempt == 3:
            print("ACCOUNT BLOCKED")
            break