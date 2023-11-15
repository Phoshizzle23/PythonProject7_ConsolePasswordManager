# Project #5 - Password Managers

'''The following code implements a simple password manager
using the Fernet encryption from the cryptography library.
The code allows the user to view existing passwords or add new ones.
The passwords are stored in a file called passwords.txt, and the master
password provided by the user is used to generate an encryption key.
The passwords are encrypted before storing and decrypted when viewed.
The main loop allows the user to choose between viewing existing passwords,
adding new passwords, or quitting the program.'''

from cryptography.fernet import Fernet

'''def write_key():
    key = Fernet.generate_key()
    with open("Key.key", "wb") as key_file:
        key_file.write(key)

write_key() '''

def load_key():
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    return key

master_pwd = input("What is the master password?: ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            if "|" in data:
                user, passw = data.split("|")
                print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())
            else:
                print("Invalid data format:", data)

def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add, quit = q): ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
