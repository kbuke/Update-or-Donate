# lib/cli.py

from helpers import (
    exit_program,
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        else:
            print("Invalid choice")


def menu():
    pass

if __name__ == "__main__":
    main()
