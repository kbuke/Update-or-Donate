# lib/helpers.py
from models.charity_type import Charity_Type
from models.charity import Charity
from models.donator import Donator

def exit_program():
    print("Goodbye!")
    exit()

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



