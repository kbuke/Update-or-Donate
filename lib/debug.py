#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
import ipdb

def reset_database():
    Donator.drop_table()
    Charity.drop_table()
    Charity_Type.drop_table()



    
reset_database()
ipdb.set_trace()
