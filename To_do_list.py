tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added")

def view_task():
    if not task:
        print("No tasks yet!")
    else:
        for i, task in enumerate(task, 1):
            print(f"{i}, {task}")

def delete_task(number):
    num = int(input("Enter number to delete: "))
    if 0 < number <= len(tasks):
        removed = task.pop(number -1)
        print(f"Task '{removed}' deleted!")
    else:
        print("Invalid input")


while True:

    print("welcome to the to do list app")
    print("1. add_task")
    print("2. view_tasks") 
    print("3. delete_task")
    print("4. exit")

    
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter a task: ")
        add_task(task)

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        delete_task()
        num = int(input("Enter number to delete: "))
        delete_task(num)

    elif choice == "4":
        print("Goodbye!!")
        break