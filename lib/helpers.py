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

