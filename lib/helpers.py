# lib/helpers.py
from models.charity_type import Charity_Type
from models.charity import Charity
from models.donator import Donator

def exit_program():
    print("Goodbye!")
    exit()

#----------------------------------------------------------------------------------------------

#Check charity types exist
def check_charity_type(user_input):
    if Charity_Type.find_by_category(user_input):
        return True
    else:
        print(f"{user_input} does not exist on this apps database")

#Check charity exists
def check_charity(user_input):
    if Charity.find_by_name(user_input):
        return True
    else:
        print(f"{user_input} does not exist on this apps database")

#Check donor exists
def check_donor(user_input):
    if Donor.find_by_name(user_input):
        return True
    else:
        print(f"The app has not received a donation from {user_input} yet")

#----------------------------------------------------------------------------------------------

#Show all available charity types
def show_all_charity_types():
    charity_types = Charity_Type.get_all()
    print("")
    print("-----------------------------------------------------------------------")
    for count, charity_type in enumerate(charity_types):
        print(f"                              {count + 1} -> {charity_type}")
        print("-----------------------------------------------------------------------")

#Show all available charities
def show_all_charities():
    charities = Charity.get_all()
    print("-----------------------------------------------------------------------")
    for count, charity in enumerate(charities):
        print(f"           {count + 1} -> {charity}")
        print("-----------------------------------------------------------------------")

#Show all donors
def show_all_donors():
    donors = Donor.get_all()
    print("The following donors have donated on this app:")
    for count, donor in enumerate(donors):
        print(f"{count + 1} -> {donor}")

#----------------------------------------------------------------------------------------------

#Update charity types
def update_charity_type(charity_type):
    if charity_type := Charity_Type.find_by_category(charity_type):
        try:
            new_charity_type = input("Enter UPDATED charity type: ")
            charity_type.category = new_charity_type
            charity_type.update()
            print(f"Success! {charity_type} has been updated to {new_charity_type}")
        except Exception as exc:
            print(f"Error updating {charity_type}", exc)
    else:
        print(f"{charity_type} is not a registered charity category on this app")


#Update charities
def update_charity(charity):
    if charity_info := Charity.find_by_name(charity):
        try:
            update_name = input("Enter updated name: ")
            charity_info.name = update_name
            update_location = input("Enter updated location: ")
            charity_info.location = update_location
            updated_category = input("Enter the updated charity category: ")
            charity_type_info = Charity_Type.find_by_category(updated_category)
            if charity_type_info:
                updated_type_id = charity_type_info.id
                charity_info.charity_type_id = updated_type_id
                charity_info.update()
        except Exception as exc:
            print(f"Error updating {charity}", exc)
  

#Update donors donation to specific charity
def update_donation_to_chosen_charity(donate_name, charity):
    if donor_info := Donor.find_by_name(donate_name):
        try:
            update_name = input("Enter updated name: ")
            donor_info.name = update_name
            update_location = input("Enter updated location: ")
            donor_info.location = update_location
            update_donate = input("Enter updated donation: £")
            donor_info.amount_donated = float(update_donate)
            charity_info = Charity.find_by_name(charity)
            if charity_info:
                donor_info.charity_id = charity_info.id
                donor_info.charity_type_id = charity_info.charity_type_id
                donor_info.update()
        except Exception as exc:
            print(f"Error updating {donate_name}'s donation", exc)
    else:
        print(f"{donate_name} has not made a donation to {charity}")

#----------------------------------------------------------------------------------------------

#Show all charities of a chosen type
def show_charities_of_certain_type(selected_charity_type):
    charity_type_info = Charity_Type.find_by_category(selected_charity_type)
    if charity_type_info:
        charity_type_id = charity_type_info.id 
        charities_info = Charity.find_by_charity_type_id(charity_type_id)
        if charities_info:
            print(f"               The following charities are {selected_charity_type} charities:")
            print("")
            print("---------------------------------------------------------------------------------------------------")
            for count, charity_info in enumerate(charities_info):
                print(f"                     {count + 1} -> {charity_info}")
                print("---------------------------------------------------------------------------------------------------")
        else:
            print(f"               {selected_charity_type} has no registered charities yet")
    else:
        print(f"               {selected_charity_type} is not a registered category on this app")

#Show all donors to a certain charity
def show_certain_donors(selected_charity):
    charity_info = Charity.find_by_name(selected_charity)
    if charity_info:
        charity_id = charity_info.id
        donors_info = Donor.find_by_charity_id(charity_id)
        if donors_info:
            print(f"                 The following have donated to {selected_charity}:")
            print("-----------------------------------------------------------------------")
            for count, donor_info in enumerate(donors_info):
                print(f"          {count + 1} -> {donor_info}")
                print("-----------------------------------------------------------------------")
        else:
            print(f"{selected_charity} has received no donations yet")
    else:
        print(f"{selected_charity} is not a registered charity on this app")

#----------------------------------------------------------------------------------------------

#Add a new charity type to database
def add_new_charity_type(new_type):
    if not check_charity_type(new_type):
        Charity_Type.category = new_type
        Charity_Type.create(new_type)
        print("")
        print(f"Adding {new_type} to the apps database")
        print("")
        print(f"{new_type} has been added to the list of available charity types")
    else:
        print(f"{new_type} Category is already registered on this apps database")

#Add a new charity to database
def add_new_charity(new_charity_type):
    charity_type_info = Charity_Type.find_by_category(new_charity_type)
    if charity_type_info:
        new_name = input("Enter the name of your charity: ")
        new_location = input("Enter the location of your charity: ")
        new_type = charity_type_info.id
        Charity.create(new_name, new_location, new_type)
    else:
        print(f"{new_charity_type} is not a registered charity type on this app")
    

#Add a new donor to the database
def add_new_donor(new_donation):
    charity_info = Charity.find_by_name(new_donation)
    if charity_info:
        print(charity_info.charity_type_id)
        new_name = input("Enter your name: ")
        new_location = input("Enter your location: ")
        new_donation = input("Enter the amount to donate: £")
        new_charity_id = charity_info.id
        new_charity_type_id = charity_info.charity_type_id
        Donor.create(new_name, new_location, float(new_donation), new_charity_id, new_charity_type_id)
    else:
        print(f"{new_donation} is not a registered charity on this app")

#----------------------------------------------------------------------------------------------



