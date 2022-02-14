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

    def edit(self, id, first_name, last_name, address, city, state, zipcode):
        self.cursor.execute("UPDATE addresses SET first_name=?, last_name=?, address=?, city=?, state=?, zipcode=? WHERE id=?", (first_name, last_name, address, city, state, zipcode, id))
        self.connect.commit()

    def delete_all(self):
        self.cursor.execute("DROP TABLE addresses")

    def __del__(self):
        self.connect.close()

    
database = Database("address_book.db")
# database.add("Shelby", "Kim", "230 Wilde Avenue", "San Francisco", "CA", "94134")
# database.add("Michelle", "Lassiter", "10168 Foothill Boulevard", "Oakland", "CA", "94605")
# database.add("Mikae", "Lam", "455 West 200 North", "Salt Lake City", "UT", "84103")
# database.add("Lima", "Gamboa", "7589 State Hwy 120", "Groveland", "CA", "95321")