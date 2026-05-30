
import json  

FILE_NAME = "expenses.json"

def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return[]
    
def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

def add_expenses(expenses):
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")

    expense = {
            "amount": amount,
            "category": category,
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expenses added succesfully!\n")


def view_expenses(expenses):
    if len(expenses) == 0:
        print("no expenses found\n")
        return
    
    print("\nYour Expenses: ")
    print("-" * 30)

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['category']} - {expense['amount']}")
        print("_" * 30 + "\n")

def total_spent (expenses):
    total = 0
    for expense in expenses:
        amount = expense.get("amount",0)
        try:
            total += float(amount)
        except:
            continue
    return total

def main():
    expenses = load_expenses()

    while True:
        print("=== EXPENSE TRACKER ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Spent")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expenses(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            print(f"Total spent: {total_spent(expenses)}")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.\n")

main()
