from models.__init__ import CONN, CURSOR

class Charity:
    
    all = {}

    def __init__(self, name, location, charity_type_id, id=None):
        self.name = name
        self.location = location
        self.charity_type_id = charity_type_id
    
    def __repr__(self):
        return f"{self.name} in {self.location}"
    
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
            raise ValueError("location must be a non-empty string")
        
    @property
    def charity_type_id(self):
        return self._charity_type_id
    
    @charity_type_id.setter
    def charity_type_id(self, charity_type_id):
        if Charity_Type.find_by_id(charity_type_id):
            self._charity_type_id = charity_type_id
        else:
            raise ValueError("charity_type_id must be part of the Charity_Type class")
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS charities(
                id INTEGER PRIMARY KEY,
                name TEXT, 
                location TEXT,
                charity_type_id INTEGER,
                FOREIGN KEY (charity_type_id) REFERENCES charity_type(id))
        """
        CURSOR.execute(sql)
        CONN.commit
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS charities
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        sql = """
            INSERT INTO charities (name, location, charity_type_id)
            VALUES(?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.location, self.charity_type_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, location, charity_type_id):
        charity = cls(name, location, charity_type_id)
        charity.save()
        return charity
    
    def update(self):
        sql = """
            UPDATE charities
            SET name = ?, location = ?, charity_type_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql,(self.name, self.location, self.charity_type_id, self.id))
        CONN.commit()
    
    def delete(self):
        sql = """
            DELETE FROM charities
            WHERE id = ?
        """
        CURSOR.execute(sql,(self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None
    
    @classmethod
    def instance_from_db(cls, row):
        charity = cls.all.get(row[0])
        if charity:
            charity.name = row[1]
            charity.location = row[2]
            charity.charity_type_id = row[3]
        else:
            charity = cls(row[1], row[2], row[3])
            charity.id = row[0]
            cls.all[charity.id] = charity
        return charity

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM charities
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM charities
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM charities
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def donators(self):
        from models.donator import Donator
        sql = """
            SELECT * FROM donators
            WHERE charity_id = ?
        """
        CURSOR.execute(sql, (self.id,),)
        rows = CURSOR.fetchall()
        return [
            Donator.instance_from_db(row) for row in rows
        ]
    
    @classmethod
    def find_by_charity_type_id(cls, charity_type_id):
        sql = """
            SELECT *
            FROM charities
            WHERE charity_type_id = ?
        """
        rows = CURSOR.execute(sql, (charity_type_id,)).fetchall()
        if rows:
            return [cls.instance_from_db(row) for row in rows]
        else:
            return None
    