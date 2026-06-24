students = []

while True:
    print("\n--- Student Record App ---")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        age = input("Enter student age: ")

        student = {"name": name, "age": age}
        students.append(student)
        print("Student added successfully")

    elif choice == "2":
        if len(students) == 0:
            print("No students found")
        else:
            for student in students:
                print("Name:", student["name"], "| Age:", student["age"])

    elif choice == "3":
        search_name = input("Enter student name to search: ")
        found = False

        for student in students:
            if student["name"] == search_name:
                print("Student found")
                print("Name:", student["name"], "| Age:", student["age"])
                found = True
                break

        if found == False:
            print("Student not found")

    elif choice == "4":
        delete_name = input("Enter student name to delete: ")
        found = False

        for student in students:
            if student["name"] == delete_name:
                students.remove(student)
                print("Student deleted successfully")
                found = True
                break

        if found == False:
            print("Student not found")

    elif choice == "5":
        print("App closed")
        break

    else:
        print("Invalid choice")