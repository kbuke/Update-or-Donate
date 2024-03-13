# lib/cli.py

from helpers import (
    exit_program,
    show_all_charity_types,
    add_charity_type,
    update_charity_type,
    delete_charity_type,
    show_all_charities,
    find_charity_by_name,
    find_charity_by_id,
    create_charity,
    update_charity,
    delete_charity,
    calculate_amount_donated_to_each_type,
    amount_donated_to_each_charity,
    how_many_donations,
    show_all_donaters,
    new_donation,
    update_donation,
    find_donor_by_name,
    find_donor_by_id,
    delete_donor
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            show_all_charity_types()
        elif choice == "2":
            add_charity_type()
        elif choice == "3":
            update_charity_type()
        elif choice == "4":
            delete_charity_type()
        elif choice == "5":
            calculate_amount_donated_to_each_type()
        elif choice == "6":
            show_all_charities()
        elif choice == "7":
            find_charity_by_name()
        elif choice == "8":
            find_charity_by_id()
        elif choice == "9":
            create_charity()
        elif choice == "10":
            update_charity()
        elif choice == "11":
            delete_charity()
        elif choice == "12":
            amount_donated_to_each_charity()
        elif choice == "13":
            how_many_donations()
        elif choice == "14":
            show_all_donaters()
        elif choice == "15":
            new_donation()
        elif choice == "16":
            update_donation()
        elif choice == "17":
            find_donor_by_name()
        elif choice == "18":
            find_donor_by_id()
        elif choice == "19":
            delete_donor()
        elif choice == "20":
            calculate_amount_donated_to_each_type()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Show all available charity types")
    print("2. Add a new type of charity")
    print("3. Update the type of charity")
    print("4. Delete a type of charity")
    print("5. Show amount a charity category has raised")
    print("6. Show all charities")
    print("7. Find charity by name")
    print("8. Find charity by id")
    print("9. Create a new charity")
    print("10. Update an existing charity")
    print("11. Delete a charity")
    print("12. Show how much each charity has raised")
    print("13. Show how many donations have been made to your charity")
    print("14. Show all donors")
    print("15. Make a new donation")
    print("16. Update an existing donation")
    print("17. Find donor by name")
    print("18. Find donor by id")
    print("19. Delete donor")
    print("20. Calculate amount donated to each charity type")

if __name__ == "__main__":
    main()
