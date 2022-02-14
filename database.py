import sqlite3

class Database:
    def __init__(self, database):
        self.connect = sqlite3.connect(database)
        self.cursor = self.connect.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS addresses (id INTEGER PRIMARY KEY, first_name, last_name, address, city, state, zipcode)")
        self.connect.commit()

    def fetch(self):
        self.cursor.execute("SELECT * FROM addresses")
        rows = self.cursor.fetchall()
        return rows

    def add(self, first_name, last_name, address, city, state, zipcode):
        self.cursor.execute("INSERT INTO addresses VALUES (NULL, ?, ?, ?, ?, ?, ?)", (first_name, last_name, address, city, state, zipcode))
        self.connect.commit()

    def remove(self, id):
        self.cursor.execute("DELETE FROM addresses WHERE id=?", (id,))
        self.connect.commit()

    def edit(self, first_name, last_name, address, city, state, zipcode):
        self.cursor.execute("UPDATE addresses SET first_name=?, last_name=?, address=?, city=?, state=?, zipcode=? WHERE id=?", (first_name, last_name, address, city, state, zipcode))
        self.connect.commit()

    def __del__(self):
        self.connect.close()

    
database = Database("address_book.db")
database.add("Shelby", "Kim", "123 Wilde Avenue", "San Jose", "CA", "94134")
database.add("Ashley", "Tanner", "456 Cunning Avenue", "San Francisco", "CA", "95634")
database.add("Jamie", "Kimble", "678 Homer Avenue", "San Diego", "CA", "97824")

