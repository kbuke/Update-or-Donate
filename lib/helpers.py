# lib/helpers.py
from models.charity_type import Charity_Type
from models.charity import Charity
from models.donator import Donator

def exit_program():
    print("Goodbye!")
    exit()

#charity_type file helper functions
def show_all_charity_types():
    available_chaity_types = Charity_Type.get_all()
    for available_chaity_type in available_chaity_types:
        print(available_chaity_type)

def add_charity_type():
    new_charity_type = input("Enter new charity type: ")
    try:
        Charity_Type.create(new_charity_type)
    except Exception as exc:
        print("Error creating charity type ", exc)

def update_charity_type():
    updated_charity_type = input("Enter OLD charity type: ")
    if charity_type := Charity_Type.find_by_category(updated_charity_type):
        try:
            new_charity_type = input("Enter NEW charity type: ")
            charity_type.category = new_charity_type
            charity_type.update()
            print(f"Success, {updated_charity_type} has been updated to {new_charity_type}")
        except Exception as exc:
            print("Error updating charity type ", exc)
    else:
        print(f"{updated_charity_type} was not found")

def delete_charity_type():
    charity_type_to_delete = input("Enter the charity type you want to delete: ")
    print(f"Charity type entered: {charity_type_to_delete}")
    if charity_type := Charity_Type.find_by_category(charity_type_to_delete):
        print("Charity type found in the database")
        charity_type.delete()
        print(f"Success, {charity_type_to_delete} has been deleted")
    else:
        print(f"{charity_type_to_delete} was not found")


def calculate_amount_donated_to_each_type():
    charity_type = input("Enter the charity type: ")
    charity_type_info = Charity_Type.find_by_category(charity_type)
    donations = []
    if charity_type_info:
        charity_type_id_number = charity_type_info.id
        donators_info = Donator.find_by_charity_id(charity_type_id_number)
        if donators_info:
            for donor in donators_info:
                donations.append(donor.amount_donated)

            total_amount = round(sum(donations),2)
            print(f"So far {charity_type} charities have raised £{total_amount}")
        else:
            print(f"No donations found for {charity_type} charities")
    else:
        print(f"{charity_type} type of charities are not in the database")

#charity helper functions
def show_all_charities():
    charities = Charity.get_all()
    for charity in charities:
        print(f"{charity}")

def find_charity_by_name():
    charity_name = input("Enter charities name: ")
    charity = Charity.find_by_name(charity_name)
    if charity:
        print(f"{charity}")
    else:
        print(f"{charity} not found")

def find_charity_by_id():
    charity_id = input("Enter charities id: ")
    charity = Charity.find_by_id(charity_id)
    if charity:
        print(f"{charity}")
    else:
        print(f"{charity_id} id number was not found")

def create_charity():
    charity_name = input("Enter new charity name: ")
    charity_location = input("Enter new charity location: ")
    charity_category = input("Enter new charity type: ")
    new_charity_info = Charity_Type.find_by_category(charity_category)
    if new_charity_info:
        foreign_key = new_charity_info.id
        try:
            Charity.create(charity_name, charity_location, foreign_key)
        except Exception as exc:
            print("Error creating charity ", exc)

def update_charity():
    charity_name = input("Enter charities name: ")
    if charity_info := Charity.find_by_name(charity_name):
        updated_name = input("Enter UPDATED charity name: ")
        updated_location = input("Enter UPDATED charity location: ")
        updated_category = input("Enter UPDATED charity category: ")
        updated_charity_info = Charity_Type.find_by_category(updated_category)
        if updated_charity_info:
            foreign_key = updated_charity_info.id
            try:
                charity_info.name = updated_name
                charity_info.location = updated_location
                charity_info.charity_type_id = foreign_key
                charity_info.update()
                print(f"Success, {updated_name} has been updated")
            except Exception as exc:
                print(f"Error updating {charity_name} ", exc)
        else:
            print(f"{updated_category} is not a valid charity type")
    else:
        print(f"{charity_name} is not a registered charity")

def delete_charity():
    charity_name = input("Enter the name of charity to delete: ")
    if charity := Charity.find_by_name(charity_name):
        charity.delete()
        print(f"{charity_name} has been deleted from databse.")
    else:
        print(f"{charity_name} is not in the database")

def amount_donated_to_each_charity():
    charity_name = input("Enter the name of the charity: ")
    charity_info = Charity.find_by_name(charity_name)
    if charity_info:
        donations = []
        charity_id_number = charity_info.id
        donators_info = Donator.find_by_charity_id(charity_id_number)
        if donators_info:
            for donator in donators_info:
                donations.append(donator.amount_donated)
                total_amount = round(sum(donations), 2)
                print(f"£{total_amount} has been donated to {charity_name} so far")
        else:
            print(f"No charity named {charity_name} found!")

def how_many_donations():
    charity_name = input("Enter the name of the charity: ")
    charity_info = Charity.find_by_name(charity_name)
    if charity_info:
        charity_id_number = charity_info.id
        donators_info = Donator.find_by_charity_id(charity_id_number)
        if donators_info:
            amount_of_donations = len(donators_info)
            print(f"{charity_name} has received {amount_of_donations} donations.")
        else:
            print(f"{charity_name} not found")

#donors.py helper functions
def show_all_donaters():
    donators = Donator.get_all()
    for donator in donators:
        print(donator)

def new_donation():
    charity_name = input("Enter name of the charity you wish to donate to: ")
    charity_info = Charity.find_by_name(charity_name)
    if charity_info:
        donator_name = input("Enter your name: ")
        donator_location = input("Enter your location: ")
        donated_amount = input("Enter amount you want to donate: ")
        charity_id = charity_info.id
        charity_type_foreign_key = charity_info.charity_type_id
        charity_type_info = Charity_Type.find_by_id(charity_type_foreign_key)
        print(f"{charity_type_info}")
        if charity_type_info:
            charity_type_id = charity_type_info.id
            try:
                donator = Donator.create(donator_name, donator_location, float(donated_amount), charity_id, charity_type_id)
                print(f"Success, {donator.name} made a donation")
            except Exception as exc:
                print("Error making donation", exc)
    else:
        print("Charity not found")

def update_donation():
    donator_name = input("Enter the name the donation was made under: ")
    if donator := Donator.find_by_name(donator_name):
        updated_donator_name = input("Enter updated name: ")
        updated_donator_location = input("Enter updated location: ")
        updated_donor_amount = input("Enter updated amount: ")
        updated_donator_charity_name = input("Enter updated charity name: ")

        charity_info = Charity.find_by_name(updated_donator_charity_name)
        if charity_info:
            updated_charity_id = charity_info.id
            charity_type_foreign_key = charity_info.charity_type_id

            charity_type_info = Charity_Type.find_by_id(charity_type_foreign_key)
            if charity_type_info:
                new_charity_type_id = charity_type_info.id
                try:
                    donator.name = updated_donator_name
                    donator.location = updated_donator_location
                    donator.amount_donated = float(updated_donor_amount)
                    donator.charity_id = updated_charity_id
                    donator.charity_type_id = new_charity_type_id
                    donator.update()
                    print(f"Success, {updated_donator_name}'s donation has been updated")
                except Exception as exc:
                    print("Error updating donation ", exc)
            else:
                print(f"Charity called {updated_donator_charity_name} not found")
        else:
            print(f"No donation under the name of {donator_name} found")


def find_donor_by_name():
    donator_name = input("Enter donators name: ")
    donator_info = Donator.find_by_name(donator_name)
    if donator_info:
        print(f"{donator_info}")
    else:
        print(f"{donator_name} was not found")

def find_donor_by_id():
    donator_id = input("Enter donators id: ")
    donator_info = Donator.find_by_id(donator_id)
    if donator_info:
        print(f"{donator_info}")
    else:
        print(f"{donator_id} was not found")

def delete_donor():
    donor_name = input("Enter donors name: ")
    if donor := Donator.find_by_name(donor_name):
        donor.delete()
        print(f"Donor number {donor_name} has been deleted.")
    else:
        print(f"Donor {donor_name} not found")



