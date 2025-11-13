from src.services.student_service import add_student, view_students, update_student, delete_student

def main():
    while True:
        print("\n=== STUDENT MANAGEMENT SYSTEM ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Select: ")

        if choice == "1":
            name = input("Name: ")
            age = int(input("Age: "))
            major = input("Major: ")
            add_student(name, age, major)
        elif choice == "2":
            students = view_students()
            for s in students:
                print(s)
        elif choice == "3":
            name = input("Name to update: ")
            age = input("New age (or skip): ")
            major = input("New major (or skip): ")
            update_student(name, int(age) if age else None, major if major else None)
        elif choice == "4":
            name = input("Name to delete: ")
            delete_student(name)
        elif choice == "5":
            print("Bye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
