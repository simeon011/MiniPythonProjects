import random
import string
import json
import os

FILE_NAME = "passwords.json"


def create_random_password():
    length_password = int(input("Enter the length of password: "))
    characters = string.printable
    print(f"Your generated password: {''.join(random.choice(characters) for _ in range(length_password))}")


def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as file:
            json.dump({}, file, indent=4)


def load_passwords():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)


def save_passwords(data):
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)


def add_password():
    site = input("Enter the site name: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    data = load_passwords()
    data[site] = {"username": username, "password": password}
    save_passwords(data)
    print("Password added successfully")


def show_password():
    data = load_passwords()

    if not data:
        print("⚠ No passwords saved yet.")
        return
    print("\n🔐 Saved passwords:")
    print(f"🌐 Site   | 👤   Username     |   🔑  Passwords")
    for site, info in data.items():
        print(f"🌐 {site} | 👤 {info['username']} | 🔑 {info['password']}")
    print()


def delete_password():
    data = load_passwords()

    if not data:
        print("⚠ No passwords saved yet.")
        return
    password_for_delete = input("Enter the site name: ")
    if password_for_delete not in data:
        print("❌ This site is not in your password list.")
        return
    answer = input("Are you sure you want to delete this password?[Y/N]")
    if answer == "Y" or answer == "y":
        del data[password_for_delete]
        save_passwords(data)
        print("🗑 Password deleted successfully")
        return
    else:
        print("❌ The delete process has been cancelled")


def menu():
    create_file()

    while True:
        print("===== HELLO IN PASSWORD MANAGER ======")
        print("1. Create a new password")
        print("2. Add a password")
        print("3. Show all passwords")
        print("4. Delete a password")
        print("5. Exit")

        choices = input("Enter your choice: ")

        if choices == "1":
            create_random_password()
        elif choices == "2":
            add_password()
        elif choices == "3":
            show_password()
        elif choices == "4":
            delete_password()
        elif choices == "5":
            print("👋 Bye!")
            break
        else:
            print("❌ Invalid option!")


menu()
