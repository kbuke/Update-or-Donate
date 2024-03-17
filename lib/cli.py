# lib/cli.py

from helpers import(
    check_charity_type,
    check_charity,
    exit_program,
    show_all_charity_types,
    show_all_charities,
    show_all_donors,
    update_charity_type,
    update_charity,
    update_donation_to_chosen_charity,
    show_charities_of_certain_type,
    show_certain_donors,
    add_new_charity_type,
    add_new_charity,
    add_new_donor,
    delete_charity_type,
    delete_charity,
    delete_donor,
    calculate_amount_donated_to_type,
    calculate_amount_donated_to_charity
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

def charity_type_menu():
    prev_page = "Home"
    print("          ____________________________________________________________")
    print("          ---------------------Charity Types Menu---------------------")
    print("          ____________________________________________________________")
    print("")
    print("               We have the available charity types on this app:")
    show_all_charity_types()
    print("          Enter the charity CATEGORY to see more information about it")
    print("")
    print("                                    OR Press")
    print("")
    print("                (A) -> To add a NEW charity type to the app")
    print("")
    print("              (R) -> To remove a current charity type from app")
    print("")
    print("____________________________________________________________")
    b_0(prev_page)
    print("____________________________________________________________")

def specific_charity_type_menu(specific_type, prev_page):
    print("          ____________________________________________________________")
    print(f"         --------------------{specific_type} Menu--------------------")
    print("          ____________________________________________________________")
    print("")
    calculate_amount_donated_to_type(specific_type)
    print("")
    show_charities_of_certain_type(specific_type)
    print("")
    print(f"            Make changes to {specific_type} category by entering:")
    print("")
    print(f"               (A) -> Add a new {specific_type} charity to app")
    print("")
    print(f"                (U) -> Update a {specific_type} charity")
    print("")
    print(f"                (D) -> Delete a {specific_type} charity")
    print("")
    print("                                    OR")
    print("")
    print("            Enter the name of the charity to go to its profile")
    print("____________________________________________________________")
    b_0(prev_page)
    print("____________________________________________________________")

def charity_menu():
    print("          ____________________________________________________________")
    print("          ------------------------Charity Menu------------------------")
    print("          ____________________________________________________________")
    print("")
    print("              We have the available charities on this app:")
    print("")
    show_all_charities()
    print("")
    print("                Enter the CHARITY to see more information about it")
    print("")
    print("                                     OR PRESS")
    print("")
    print("                    (A) -> To add a NEW charity to the app")
    print("")
    print("               (D) -> To donate to one of the charities on the app")
    print("")
    print("                           (U) -> To update a charity")
    print("")
    print("                     (R) -> To remove a charity from the app")
    print("")
    print("____________________________________________________________")
    b_0()
    print("____________________________________________________________")

def specific_charity_menu(charity_name, prev_page):
    print("          ____________________________________________________________")
    print(f"         --------------------{charity_name} Menu--------------------")
    print("          ____________________________________________________________")
    print("")
    calculate_amount_donated_to_charity(charity_name)
    print("")
    show_certain_donors(charity_name)
    print("")
    print("                                PRESS:")
    print("")
    print(f"              (A) -> To add a donation to {charity_name}            ")
    print("")
    print(f"           (U) -> Update an existing donation to {charity_name}     ")
    print("")
    print(f"              (D) -> To delete a donation to {charity_name}")
    print("")
    print("____________________________________________________________")
    b_0(prev_page)
    print("____________________________________________________________")

def b_0(prev_page="Home"):
    print("                                    OR Press")
    print("")
    print(f"                   (B) -> To go back to {prev_page} Menu")
    print("")
    print("                             (0) -> To exit app")

if __name__ == "__main__":
    main()
