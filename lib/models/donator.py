from models.__init__ import CONN, CURSOR
from models.charity import Charity
from models.charity_type import Charity_Type

class Donator:

    all = {}

    def __init__(self, name, location, amount_donated, charity_id, charity_type_id, id=None):
        self.name = name
        self.location = location
        self.amount_donated = amount_donated
        self.charity_id = charity_id
        self.charity_type_id = charity_type_id
    
    def __repr__(self):
        charity_name = Charity.find_by_id(self.charity_id).name if self.charity_id in Charity.all else ""
        return f"<{self.name} from {self.location} has donated £{self.amount_donated} to {charity_name}!"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("name must be a non-empty string")
    
    @property
    def location(self):
        return self._location 
    
    @location.setter
    def location(self, location):
        if isinstance(location, str) and len(location):
            self._location = location
        else:
            raise ValueError("location muct be a non-empty string")
    
    @property
    def amount_donated(self):
        return self._amount_donated
    
    @amount_donated.setter
    def amount_donated(self, amount_donated):
        if isinstance(amount_donated, float) and amount_donated > 0.0:
            self._amount_donated = amount_donated
        else:
            raise ValueError("amount_donated must be a float higher than 0.0")
        
    @property
    def charity_id(self):
        return self._charity_id
    
    @charity_id.setter
    def charity_id(self, charity_id):
        if Charity.find_by_id(charity_id):
            self._charity_id = charity_id
        else:
            raise ValueError("charity_id must be part of Charity class")
    
    @property
    def charity_type_id(self):
        return self._charity_type_id
    
    @charity_type_id.setter
    def charity_type_id(self, charity_type_id):
        if Charity_Type.find_by_id(charity_type_id):
            self._charity_type_id = charity_type_id
        else:
            raise ValueError("charity_type_id must be part of Charity_Type class")
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS donators (
                id INTEGER PRIMARY KEY,
                name TEXT,
                location TEXT,
                amount_donated REAL,
                charity_id INTEGER,
                charity_type_id INTEGER,
                FOREIGN KEY (charity_id) REFERENCES charity(id),
                FOREIGN KEY (charity_type_id) REFERENCES charity_types(id)
            )
        """
        try:
            CURSOR.execute(sql)
            CONN.commit()
            print("Table created successfully")
        except Exception as exc:
            print("Error creating table:", exc)
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS donators;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        sql = """
            INSERT INTO donators(name, location, amount_donated, charity_id, charity_type_id)
            VALUES (?, ?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.location, self.amount_donated, self.charity_id, self.charity_type_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """
            UPDATE donators
            SET name = ?, location = ?, amount_donated = ?, charity_id = ?, charity_type_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.location, self.amount_donated, 
                            self.charity_id, self.charity_type_id, self.id))
        CONN.commit()
    
    def delete(self):
        sql = """
            DELETE FROM donators
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, name, location, amount_donated, charity_id, charity_type_id):
        donator = cls(name, location, amount_donated, charity_id, charity_type_id)
        donator.save()
        return donator

    @classmethod
    def instance_from_db(cls, row):
        donator = cls.all.get(row[0])
        if donator:
            donator.name = row[1]
            donator.location = row[2]
            donator.amount_donated = row[3]
            donator.charity_id = row[4]
            donator.charity_type_id = row[5]
        else:
            donator = cls(row[1], row[2], row[3], row[4], row[5])
            donator.id = row[0]
            cls.all[donator.id] = donator
        return donator
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM donators
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM donators
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        if row:
            return cls.instance_from_db(row)
        else:
            return None
    
    @classmethod
    def find_by_charity_id(cls, charity_id):
        sql = """
            SELECT *
            From donators
            WHERE charity_id = ?
        """
        rows = CURSOR.execute(sql, (charity_id,)).fetchall()
        if rows:
            return [cls.instance_from_db(row) for row in rows]
        else:
            return None
    
    @classmethod
    def find_by_charity_type_id(cls, charity_type_id):
        sql = """
            SELECT *
            FROM donators
            WHERE charity_type_id = ?
        """
        rows = CURSOR.execute(sql, (charity_type_id,)).fetchall()
        if rows:
            return [cls.instance_from_db(row) for row in rows]
        else:
            return None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM donators
            WHERE name = ?
        """
        row = CURSOR.execute(sql,(name,)).fetchone()
        if row:
            return cls.instance_from_db(row)
        else:
            return None
    
    
    

    

    

    




