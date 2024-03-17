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
        print("")
        print("------------------------------")
        choice = input("> ")
        print("------------------------------")
        print("")
        if choice == "0":
            print(exit_program())

        #View all charity types
        elif choice == "a":
            while True:
                charity_type_menu()
                print("------------------------------")
                charity_type_choice = input("> ")
                print("------------------------------")

                #Add a new charity type
                if charity_type_choice.lower() == "a":
                    new_type = input("Enter new charity type: ")
                    add_new_charity_type(new_type)
                    continue
                
                #Remove charity type
                if charity_type_choice.lower() == "r":
                    charity_type_choice = input("Enter the charity category you want to delete: ")
                    if check_charity_type(charity_type_choice):
                        delete_charity_type(charity_type_choice)
                        continue
                
                #Return to home page
                elif charity_type_choice.lower() == "b":
                    break

                #Exit program
                elif charity_type_choice == "0":
                    print(exit_program())
                
                #Go to a specific category menu
                elif check_charity_type(charity_type_choice):
                    prev_page = "Charity Types Menu"
                    while True:
                        specific_charity_type_menu(charity_type_choice, prev_page)
                        edit_charity_type = input("> ")

                        #Add a new charity (of specific category)
                        if edit_charity_type == "a":
                            add_new_charity(charity_type_choice)
                            continue

                        #Update a charity (of specific category) 
                        elif edit_charity_type.lower() == "u":
                            charity_name = input("Enter the name of the charity you wish to update: ")
                            update_charity(charity_name)
                        
                        #Delete a charity (of specific category)
                        elif edit_charity_type.lower() == "d":
                            print("------------------------------")
                            charity_name = input("Enter charity name: ")
                            print("------------------------------")
                            delete_charity(charity_name)
                            continue

                        #Returns to all charity types meny 
                        elif edit_charity_type.lower() == "b":
                            break
                        
                        elif edit_charity_type == "0":
                            print(exit_program())

                        #Go to a specific charities menu
                        elif check_charity(edit_charity_type):
                            while True:
                                prev_page = charity_type_choice + " Category"
                                specific_charity_menu(edit_charity_type, prev_page)
                                print("------------------------------")
                                donate_update_or_delete = input("> ")
                                print("------------------------------")

                                #Add a new donor
                                if donate_update_or_delete.lower() == "a":
                                    add_new_donor(edit_charity_type)

                                #Update a donation ------------------ Not working
                                elif donate_update_or_delete.lower() == "u":
                                    donor_name = input("Enter the name the previous donation was made under: ")
                                    update_donation_to_chosen_charity(donor_name, edit_charity_type)
                                
                                #Delete a donation
                                elif donate_update_or_delete.lower() == "d":
                                    print("------------------------------")
                                    donor_name = input("Enter name of donor you wish to delete: ")
                                    print("------------------------------")
                                    delete_donor(donor_name)
                                
                                #Return to previous screen
                                elif donate_update_or_delete.lower() == "b":
                                    break
                                
                                elif donate_update_or_delete == "0":
                                    print(exit_program())

        #Take user to all charities menu
        elif choice.lower() == "b":
            while True:
                charity_menu()
                charity_input = input("> ")

                #Create a new charity
                if charity_input.lower() == "a":
                    print("Please select the TYPE of charity you wish to CREATE from the following: ")
                    show_all_charity_types()
                    charity_type_choice = input("> ")
                    if check_charity_type(charity_type_choice):
                        add_new_charity(charity_type_choice)
                    else:
                        print(f"{charity_type_choice} is not valid")
                    continue
                
                if charity_input == "0":
                    print(exit_program())
                
                #Make a donation to an existing charity
                elif charity_input.lower() == "d":
                    print("Please enter the name of the charity you wish to donate to: ")
                    show_all_charities()
                    charity_choice = input("> ")
                    if check_charity(charity_choice):
                        add_new_donor(charity_choice)
                    continue
                
                #Update a charity 
                elif charity_input.lower() == "u":
                    charity_name = input("Enter the name of the charity ypu want to donate to: ")
                    update_charity(charity_name)
                
                #Remove a charity
                elif charity_input.lower() == "r":
                    print("Please enter the name of the charity you wish to delete:")
                    show_all_charities()
                    charity_choice = input("> ")
                    if check_charity(charity_choice):
                        delete_charity(charity_choice)
                
                #Take to specific charity
                elif check_charity(charity_input):
                    prev_page = "Charity"
                    while True:
                        specific_charity_menu(charity_input, prev_page)
                        print("------------------------------")
                        donate_update_or_delete = input("> ")
                        print("------------------------------")

                        #Add a new donation
                        if donate_update_or_delete.lower() == "a":
                            add_new_donor(charity_input)

                        #Update a donation ------------------ Not working
                        elif donate_update_or_delete.lower() == "u":
                            donor_name = input("Enter the name the previous donation was made under: ")
                            update_donation_to_chosen_charity(donor_name, charity_input)
                        
                        #Delete a donation
                        elif donate_update_or_delete.lower() == "d":
                            print("------------------------------")
                            donor_name = input("Enter name of donor you wish to delete: ")
                            print("------------------------------")
                            delete_donor(donor_name)
                        
                        #Retrun to previous page
                        elif donate_update_or_delete.lower() == "b":
                            break
                        
                        #Close app
                        elif donate_update_or_delete == "0":
                            print(exit_program())
                
                #Return to home page (from all charity menu)
                elif charity_input.lower() == "b":
                    break

        #Close program
        elif charity_type_choice == "0":
                    print(exit_program())

        #Invalid option
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
