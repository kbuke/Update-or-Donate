from models.__init__ import CONN, CURSOR

    
class Donor:

    all = {}

    def __init__(self, name, location, amount_donated, charity_id, charity_type_id, id=None):
        self.name = name
        self.location = location
        self.amount_donated = amount_donated
        self.charity_id = charity_id
        self.charity_type_id = charity_type_id 