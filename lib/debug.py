#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.donor import Donor
import ipdb

def reset_database():
    Donor.drop_table()
    Donor.create_table()



    
reset_database()
ipdb.set_trace()
