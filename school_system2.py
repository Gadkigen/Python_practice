students = []

while True:
    print("\nENTER STUDENT DETAILS")
    print("=" * 60)

    name = input("Name: ")
    admission = input("Admission: ")
    age = int(input("Age: "))
    course = input("Course: ")
    level = input("level: ")
    module = int(input("Module: "))

    students.append([name, age, admission, course, level, module])

    more = input("Add another student? (yes/no): ") .lower()
    if more != "yes":
        break


    print("\nSTUDENTS INFORMATION SYSTEM")
    print("=" * 100)

    print(f"{'Name': <15}{'Admission': <15}{'Age': <10}{'Course': <30}{'Level':<10}{'Module':<15}")

    print("=" * 100)

    for s in students:
        print(f"{s[0]:<15}{s[1]:<15}{s[2]:<10}{s[3]:<30}{s[4]:<10}{s[5]:<15}")

    print("=" * 100)