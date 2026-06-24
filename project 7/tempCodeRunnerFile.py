import datetime
import time
import math
import random
import uuid
import importlib
dir ("d:\AI MI DATA SCIENCE\Python\Project Work\project 7")

# ---------------- DATETIME MENU ----------------

def datetime_menu():

    while True:

        print("\nDatetime and Time Operations")
        print("1. Display Current Date and Time")
        print("2. Difference Between Two Dates")
        print("3. Format Date")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back")

        choice = int(input("Enter Choice: "))

        match choice:

            case 1:
                now = datetime.datetime.now()
                print("Current Date & Time :", now)

            case 2:
                date1 = input("Enter First Date (YYYY-MM-DD): ")
                date2 = input("Enter Second Date (YYYY-MM-DD): ")

                d1 = datetime.datetime.strptime(date1,"%Y-%m-%d")
                d2 = datetime.datetime.strptime(date2,"%Y-%m-%d")

                print("Difference :", abs((d2-d1).days),"days")

            case 3:
                date = input("Enter Date (YYYY-MM-DD): ")

                d = datetime.datetime.strptime(date,"%Y-%m-%d")

                print(d.strftime("%d/%m/%Y"))

            case 4:

                input("Press Enter To Start Stopwatch")

                start = time.time()

                input("Press Enter To Stop Stopwatch")

                end = time.time()

                print("Elapsed Time :", round(end-start,2),"seconds")

            case 5:

                sec = int(input("Enter Seconds : "))

                while sec:
                    print(sec)
                    time.sleep(1)
                    sec -= 1

                print("Time Up!")

            case 6:
                break

            case _:
                print("Invalid Choice")


# ---------------- MATH MENU ----------------

def math_menu():

    while True:

        print("\nMathematical Operations")
        print("1. Factorial")
        print("2. Compound Interest")
        print("3. Trigonometry")
        print("4. Area of Shapes")
        print("5. Back")

        choice = int(input("Enter Choice: "))

        match choice:

            case 1:

                num = int(input("Enter Number: "))
                print("Factorial =", math.factorial(num))

            case 2:

                p = float(input("Principal Amount: "))
                r = float(input("Rate (%): "))
                t = float(input("Time (Years): "))

                ci = p * math.pow((1+r/100),t)

                print("Compound Interest =", round(ci,2))

            case 3:

                angle = float(input("Enter Angle in Degrees: "))

                rad = math.radians(angle)

                print("Sin =", math.sin(rad))
                print("Cos =", math.cos(rad))
                print("Tan =", math.tan(rad))

            case 4:

                print("\n1.Circle")
                print("2.Rectangle")

                shape = int(input("Enter Choice: "))

                if shape == 1:

                    r = float(input("Radius : "))
                    area = math.pi * r * r

                    print("Area =", round(area,2))

                elif shape == 2:

                    l = float(input("Length : "))
                    b = float(input("Breadth : "))

                    print("Area =", l*b)

            case 5:
                break

            case _:
                print("Invalid Choice")


# ---------------- RANDOM MENU ----------------

def random_menu():

    while True:

        print("\nRandom Data Generation")
        print("1. Random Number")
        print("2. Random List")
        print("3. Random Password")
        print("4. Random OTP")
        print("5. Back")

        choice = int(input("Enter Choice: "))

        match choice:

            case 1:

                print(random.randint(1,100))

            case 2:

                lst = []

                for i in range(5):
                    lst.append(random.randint(1,100))

                print(lst)

            case 3:

                chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789@#$"

                length = int(input("Password Length : "))

                password = ""

                for i in range(length):
                    password += random.choice(chars)

                print("Password =", password)

            case 4:

                otp = random.randint(1000,9999)

                print("OTP =", otp)

            case 5:
                break

            case _:
                print("Invalid Choice")


# ---------------- UUID MENU ----------------

def uuid_menu():

    print("\nGenerated UUID")
    print(uuid.uuid4())


# ---------------- FILE MENU ----------------

def file_menu():

    while True:

        print("\nFile Operations")
        print("1. Create File")
        print("2. Write File")
        print("3. Read File")
        print("4. Append File")
        print("5. Back")

        choice = int(input("Enter Choice: "))

        match choice:

            case 1:
                filename = input("File Name : ")
                open(filename, "w").close()
                print("file created successfully!")
                print()

            case 2:

                filename = input("File Name : ")
                data = input("Enter Data : ")
                print()
                with open(filename, "w") as f:
                    f.write(data)
                print("data written successfully!")
                print()

            case 3:

                print()

                filename = input("Enter file name: ")

                print()

                try:
                      with open(filename, "r") as f:
                       print("File Content:")
                       print()
                       print(f.read())

                except FileNotFoundError:
                 print("File does not exist!")
                 print()

            case 4:

                filename = input("File Name : ")
                data = input("Enter Data : ")
                with open(filename, "a") as f:
                    f.write("\n" + data)
                print("data appended successfully!")


            case 5:
                break

            case _:
                print("Invalid Choice")


# ---------------- MODULE EXPLORER ----------------

def module_explorer():

    module_name = input("Enter Module Name : ")

    try:

        module = importlib.import_module(module_name)

        print(dir(module))

    except:

        print("Module Not Found")


# ---------------- MAIN MENU ----------------

def main():

    while True:

        print("\n==============================")
        print("Welcome To Multi Utility Toolkit")
        print("==============================")

        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate UUID")
        print("5. File Operations")
        print("6. Explore Module Attributes")
        print("7. Exit")

        choice = int(input("Enter Choice: "))

        match choice:

            case 1:
                datetime_menu()

            case 2:
                math_menu()

            case 3:
                random_menu()

            case 4:
                uuid_menu()

            case 5:
                file_menu()

            case 6:
                module_explorer()

            case 7:
                print("Thank You For Using Multi Utility Toolkit")
                break

            case _:
                print("Invalid Choice")


# ---------------- DRIVER CODE ----------------

if __name__ == "__main__":
    main()



