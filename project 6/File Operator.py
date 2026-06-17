import os
from datetime import datetime


class JournalManager:
    def __init__(self, filename="journal.txt"):
        self.filename = filename

    
    def add_entry(self):
        entry = input("Enter your journal entry:")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            # Append mode (a)
            with open(self.filename, "a", encoding="utf-8") as file:
                file.write(f"[{timestamp}]")
                file.write(entry + "")
                file.write("-" * 40 + "\n")

            print("Entry added successfully!")

        except Exception as e:
            print(f"Error while adding entry: {e}")

    # 2. View All Entries
    def view_entries(self):
        try:
            # Read mode (r)
            with open(self.filename, "r", encoding="utf-8") as file:
                content = file.read()

                if content.strip():
                    print("Your Journal Entries:")
                    print("-" * 40)
                    print(content)
                else:
                    print("No journal entries found.")

        except FileNotFoundError:
            print("Error: The journal file does not exist. Please add a new entry first.")

        except Exception as e:
            print(f"Error: {e}")

    # 3. Search Entry
    def search_entry(self):
        keyword = input("Enter a keyword or date to search: ").lower()

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                lines = file.readlines()

            matching_entries = []
            temp_entry = ""

            for line in lines:
                temp_entry += line

                if "-" * 40 in line:
                    if keyword in temp_entry.lower():
                        matching_entries.append(temp_entry)
                    temp_entry = ""

            if matching_entries:
                print("Matching Entries:")
                print("-" * 40)
                for entry in matching_entries:
                    print(entry)
            else:
                print(f"No entries were found for the keyword: {keyword}")

        except FileNotFoundError:
            print("Error: The journal file does not exist.")

        except Exception as e:
            print(f"Error: {e}")

    # 4. Delete All Entries
    def delete_entries(self):
        try:
            if os.path.exists(self.filename):

                confirm = input(
                    "Are you sure you want to delete all entries? (yes/no): "
                ).lower()

                if confirm == "yes":
                    os.remove(self.filename)
                    print("All journal entries have been deleted.")
                else:
                    print("Deletion cancelled.")
            else:
                print("No journal entries to delete.")

        except PermissionError:
            print("Permission denied while deleting the file.")

        except Exception as e:
            print(f"Error: {e}")

    
    def menu(self):
        while True:
            print("\n" + "=" * 50)
            print("Welcome to Personal Journal Manager!")
            print("Please select an option:")
            print("1. Add a New Entry")
            print("2. View All Entries")
            print("3. Search for an Entry")
            print("4. Delete All Entries")
            print("5. Exit")
            print("=" * 50)

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_entry()

            elif choice == "2":
                self.view_entries()

            elif choice == "3":
                self.search_entry()

            elif choice == "4":
                self.delete_entries()

            elif choice == "5":
                print("Thank you for using Personal Journal Manager. Goodbye!")
                break

            else:
                print("Invalid option. Please select a valid option from the menu.")


# Main Program
journal = JournalManager()
journal.menu()
