print("welcome to the student data organizer!")

students = []

all_subjects = set()

while True:
    print("Welcome to the Student Data Organizer!")
    print("press 1 for Add Student")
    print("press 2 for Display All Students")
    print("press 3 for Update a Student")
    print("press 4 for Delete a Student")
    print("press 5 for Display Subjects Offered")
    print("6. Exit")
    print()

    choice = int(input("Enter your choice: "))

    match choice:

        
        case 1:
            print("\nEnter student details:")

            student_id = int(input("Enter Student ID: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            grade = input("Enter Grade: ")
            dob = input("Date of Birth (YYYY-MM-DD): ")

            student_info = (student_id, dob)
            subjects = input("Subjects (comma-separated): ").split(",")
            subjects = [sub.strip() for sub in subjects]

            student = {
                "id": student_info[0],
                "dob": student_info[1],
                "name": name,
                "age": age,
                "grade": grade,
                "subjects": subjects
            }

            
            students.append(student)

            print("Student added successfully!")
            print()

        
        case 2:
            print("Display All Students ---")

            if len(students) == 0:
                print("No student records found.")

            else:
                for s in students:
                    print(f"Student ID: {s['id']} | "
                          f"Name: {s['name']} | "
                          f"Age: {s['age']} | "
                          f"Grade: {s['grade']} | "
                          f"Subjects: {', '.join(s['subjects'])}")
                    print()

        
        case 3:
            sid = int(input("\nEnter Student ID to update: "))

            found = False

            for s in students:
                if s["id"] == sid:
                    found = True

                    s["name"] = input("Enter new name: ")
                    s["age"] = int(input("Enter new age: "))
                    s["grade"] = input("Enter new grade: ")

                    new_subjects = input(
                        "Enter new subjects (comma-separated): "
                    ).split(",")

                    new_subjects = [sub.strip() for sub in new_subjects]

                    all_subjects.update(new_subjects)

                    print("Student information updated successfully!")

            if not found:
                print("Student not found.")
                print()

        
        case 4:
            sid = int(input("\nEnter Student ID to delete: "))

            found = False

            for s in students:
                if s["id"] == sid:
                    students.remove(s)
                    found = True
                    print("Student deleted successfully!")
                    break

            if not found:
                print("Student not found.")
                print()

        
        case 5:
            print("Subjects Offered:")
            for subject in all_subjects:
                print(subject)
                print()

        
        case 6:
            print("Exiting program...")
            break
            print()

        
        case _:
            print("Invalid choice! Please try again.")
