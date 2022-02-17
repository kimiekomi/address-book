import sqlite3

class TreeDatabase:
    def __init__(self, database):
        self.connection = sqlite3.connect("tree_database.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY, first_name text, last_name text, address text, city text, state text, zipcode text)")
        self.connection.commit()

    def fetch(self):
        self.cursor.execute("SELECT * FROM contacts")
        entries = self.cursor.fetchall()
        return entries
        
    def add(self, id, first_name, last_name, address, city, state, zipcode):
        self.cursor.execute("INSERT INTO contacts VALUES (NULL, ?, ?, ?, ?, ?, ?)", (first_name, last_name, address, city, state, zipcode))
        self.connection.commit()

    def remove(self, id):
        self.cursor.execute("DELETE FROM contacts WHERE id=?", (id,))
        self.connection.commit()

    def update(self, id, first_name, last_name, address, city, state, zipcode):
        self.cursor.execute("UPDATE contacts SET first_name=?, last_name=?, address=?, city=?, state=?, zipcode=? WHERE id=?", (first_name, last_name, address, city, state, zipcode, id))
        self.connection.commit()

    def delete_all(self):
        self.cursor.execute("DELETE FROM contacts")
        self.connection.commit()

    def __del__(self):
        self.connection.close()

tree_database = TreeDatabase("tree_database.db")
tree_database.add(1, "Rachel", "Green", "123 Park Avenue", "New York", "NY", "95123")