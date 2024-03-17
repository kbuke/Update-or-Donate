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

def b_0(prev_page="Home"):
    print("                                    OR Press")
    print("")
    print(f"                   (B) -> To go back to {prev_page} Menu")
    print("")
    print("                             (0) -> To exit app")

if __name__ == "__main__":
    main()
