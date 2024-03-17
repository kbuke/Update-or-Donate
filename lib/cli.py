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
    print("          ____________________________________________________________")
    print("          --------------------------Home Menu-------------------------")
    print("          ____________________________________________________________")
    print("")
    print("                                     Press:")
    print("")
    print("             (A) -> To view all available charity types on the app")
    print("")
    print("               (B) -> To view all available charities on this app")
    print("")
    print("                    (0) -> To view exit the application")

if __name__ == "__main__":
    main()
