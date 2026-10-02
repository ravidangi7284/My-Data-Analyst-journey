import os
import pyperclip

FILE_NAME = "passwords.txt"
def save_password():
    website = input("Enter the website: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")

    with open(FILE_NAME, "a") as f:
        f.write(f"{website},{username},{password}\n")

def get_password():
    website = input("Enter the website to retrieve the password: ")
    found = False

    if not os.path.exists(FILE_NAME):
        print("No passwords saved yet.")
        return

    with open(FILE_NAME, "r") as f:
        for line in f:
            saved_website, saved_username, saved_password = line.strip().split(",")
            if saved_website == website:
                print(f"Username: {saved_username}")
                print(f"Password: {saved_password}")
                pyperclip.copy(saved_password)
                print("Password copied to clipboard.")
                found = True
                break

    if not found:
        print("No password found for the given website.")

def main():
    while True:
        print("Password Manager")
        print("1. Save Password")
        print("2. Get Password")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            save_password()
        elif choice == "2":
            get_password()
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

main()