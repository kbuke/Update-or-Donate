# lib/helpers.py
from models.charity_type import Charity_Type
from models.charity import Charity
from models.donator import Donator

def exit_program():
    print("Goodbye!")
    exit()

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



