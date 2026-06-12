print("python oop project: Employee managemnet system")

class Person:
    def _init_(self):
        self.__name = ""
        self.__age = 0

    # Setter 
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    # Getter 
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def display(self):
        print("Person Details")
        print("Name :", self.get_name())
        print("Age  :", self.get_age())


class Employee(Person):
    def _init_(self):
        super()._init_()
        self.__emp_id = ""
        self.__salary = 0

    # Setter 
    def set_emp_id(self, emp_id):
        self.__emp_id = emp_id

    def set_salary(self, salary):
        self.__salary = salary

    # Getter 
    def get_emp_id(self):
        return self.__emp_id

    def get_salary(self):
        return self.__salary

    def display(self):
        print("Employee Details")
        print("Name        :", self.get_name())
        print("Age         :", self.get_age())
        print("Employee ID :", self.get_emp_id())
        print("Salary      :", self.get_salary())


class Manager(Employee):
    def _init_(self):
        super()._init_()
        self.__department = ""

    # Setter
    def set_department(self, department):
        self.__department = department

    # Getter
    def get_department(self):
        return self.__department

    def display(self):
        print("Manager Details")
        print("Name        :", self.get_name())
        print("Age         :", self.get_age())
        print("Employee ID :", self.get_emp_id())
        print("Salary      :", self.get_salary())
        print("Department  :", self.get_department())


# Objects
person = None
employee = None
manager = None

# Menu
while True:
    print("--- Python OOP Project: Employee Management System ---")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        person = Person()
        person.set_name(input("Enter Name: "))
        person.set_age(int(input("Enter Age: ")))
        print("Person created successfully.")

    elif choice == 2:
        employee = Employee()
        employee.set_name(input("Enter Name: "))
        employee.set_age(int(input("Enter Age: ")))
        employee.set_emp_id(input("Enter Employee ID: "))
        employee.set_salary(float(input("Enter Salary: ")))
        print("Employee created successfully.")

    elif choice == 3:
        manager = Manager()
        manager.set_name(input("Enter Name: "))
        manager.set_age(int(input("Enter Age: ")))
        manager.set_emp_id(input("Enter Employee ID: "))
        manager.set_salary(float(input("Enter Salary: ")))
        manager.set_department(input("Enter Department: "))
        print("Manager created successfully.")

    elif choice == 4:
        print("1. Person")
        print("2. Employee")
        print("3. Manager")

        show = int(input("Enter your choice: "))

        if show == 1:
            if person:
                person.display()
            else:
                print("No Person record found.")

        elif show == 2:
            if employee:
                employee.display()
            else:
                print("No Employee record found.")

        elif show == 3:
            if manager:
                manager.display()
            else:
                print("No Manager record found.")

        else:
            print("Invalid choice!")

    elif choice == 5:
        print("Exiting the system...")
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
