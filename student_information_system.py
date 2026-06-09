
students = []
while True:

    print("\n=====STUDENTS DETAILS=====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student") 
    print("5. Exit")
    print('=' * 20)
    
    choice = int(input("Choose an option: "))

    if choice == 1:
    
        name = input("Name: ")
        admission = int(input("Admission: "))
        age = int(input("Age: "))
        course = input("Course: ")
        module = input("Module: ")
        level = int(input("Level: "))

        student = {
        "name": name,
        "admission": admission,
        "age": age,
        "course": course,
        "module": module,
        "level": level
        }
        students.append(student)
        print("Student added susccesfully!")

    elif choice == 2:
        print("\nSTUDENT DETAILS")

        for student in students:
              print("=" * 100)

        print(f"{'Name':<15}{'Admission':<15}{'Age':<15}{'Course':<25}{'Module':<15}{'level'}")

        print("-" * 100)

        for s in students:
            print(
                f"{s['name']:<15}",
                f"{s['admission']:<15}",
                f"{s['age']:<10}",
                f"{s['course']:<25}",
                f"{s['module']:<15}",
                f"{s['level']}"
            )

        print("=" * 100)

    elif choice == 3:
        adm = int(input("Enter admission number: "))

        for student in students:
            if student["admission"] == adm:
                print(student)

    elif choice == 4:
        adm = int(input("Enter admission to delete: "))
        
        for student in students:
            if adm == student["admission"]:
                students.remove(student)
                print("Student deleted!")
                

    elif choice == 5:
        print("Goodbye!")
        break