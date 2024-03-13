#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.charity import Charity
from models.donator import Donator
from models.charity_type import Charity_Type
import ipdb

def reset_database():
    Donator.drop_table()
    Charity.drop_table()
    Charity_Type.drop_table()
    Donator.create_table()
    Charity.create_table()
    Charity_Type.create_table()

    #seed data
    food = Charity_Type.create("Food")
    education = Charity_Type.create("Education")
    wildlife = Charity_Type.create("Wildlife")

    unicef = Charity.create("Unicef", "New York, USA", food.id)
    solving7 = Charity.create("Solving7", "Johannesburg, South Africa", education.id)
    wwf = Charity.create("World Wild Fund for Nature", "Gland, Switzerland", wildlife.id)

    Donator.create("Kaan", "London, UK", 65.24, solving7.id, education.id)
    Donator.create("Zahra", "Johannesburg, South Africa", 73.00, unicef.id, food.id)
    Donator.create("Louis", "Belfast, Ireland", 1000.79, wwf.id, wildlife.id)
    
reset_database()
ipdb.set_trace()
