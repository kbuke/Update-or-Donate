from models.__init__ import CONN, CURSOR

class Charity_Type():

    all = {}

    def __init__(self, category, id=None):
        self.category = category
    
    def __repr__(self):
        return f"{self.category}"
    
    @property
    def category(self):
        return self._category 
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category):
            self._category = category
        else:
            print("category must be a non empty string")
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS charity_types(
                id INTEGER PRIMARY KEY,
                category TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS charity_types
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        sql = """
            INSERT INTO charity_types(category)
            VALUES(?)
        """
        CURSOR.execute(sql, (self.category,))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    @classmethod
    def create(cls, category):
        charity_type = cls(category)
        charity_type.save()
        return charity_type
    
    def update(self):
        sql = """
            UPDATE charity_types
            SET category = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.category, self.id))
        CONN.commit()
    
    def delete(self):
        sql = """
            DELETE FROM charity_types
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None
    
    @classmethod
    def instance_from_db(cls, row):
        charity_type = cls.all.get(row[0])
        if charity_type:
            charity_type.category = row[1]
        else:
            charity_type = cls(row[1])
            charity_type.id = row[0]
            cls.all[charity_type.id] = charity_type
        return charity_type
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM charity_types
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM charity_types
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id, )).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_category(cls, category):
        category = category.strip()  # Remove leading and trailing whitespaces
        sql = """
            SELECT *
            FROM charity_types
            WHERE TRIM(LOWER(category)) = ?
        """
        row = CURSOR.execute(sql, (category.lower(),)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def charities(self):
        from models.charity import Charity 
        sql = """
            SELECT * FROM charities
            WHERE charity_type_id = ?
        """
        CURSOR.execute(sql, (self.id,),)
        rows = CURSOR.fetchall()
        return [
            Charity.instance_from_db(row) for row in rows
        ]
    
    def donators(self):
        from models.donator import Donator
        sql = """
            SELECT * FROM donators
            WHERE charity_type_id = ?
        """
        CURSOR.execute(sql, (self.id,),)
        rows = CURSOR.fetchall()
        return [
            Donator.instance_from_db(row) for row in rows
        ]