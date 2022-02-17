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

    def update(self, id, first_name, last_name, address, city, state, zipcode):
        self.cursor.execute("UPDATE addresses SET first_name=?, last_name=?, address=?, city=?, state=?, zipcode=? WHERE id=?", (first_name, last_name, address, city, state, zipcode, id))
        self.connect.commit()

    def delete_all(self):
        self.cursor.execute("DELETE FROM addresses")
        self.connect.commit()

    def __del__(self):
        self.connect.close()

    
database = Database("address_book.db")
# database.add("Rachel", "Green", "123 Park Avenue", "New York", "NY", "95123")
# database.add("Ross", "Geller", "123 Park Avenue", "New York", "NY", "95123")
# database.add("Joey", "Tribbiani", "456 Rosten Road", "New York", "NY", "95123")
# database.add("Chandler", "Bing", "789 Primrose Street", "New York", "NY", "95123")
# database.add("Monica", "Geller", "012 Hatten Drive", "New York", "NY", "95123")
# database.add("Phoebe", "Buffet", "345 Rosita Avenue", "New York", "NY", "95123")
# database.add("Sheldon", "Cooper", "678 Linwood Road", "Santa Monica", "CA", "94567")
# database.add("Leonard", "Hofstader", "678 Linwood Road", "Santa Monica", "CA", "94567")
# database.add("Rajesh", "Koothrapalli", "678 Linwood Road", "Santa Monica", "CA", "94567")
# database.add("Howard", "Wolowitz", "678 Linwood Road", "Santa Monica", "CA", "94567")
# database.add("Douglas", "Heffernan", "901 Woodrow Drive", "Trentor", "NJ", "94789")
# database.add("Carrie", "Heffernan", "901 Woodrow Drive", "Trentor", "NJ", "94789")
# database.add("Arthur", "Spooner", "901 Woodrow Drive", "Trentor", "NJ", "94789")
# database.add("Jerry", "Seinfeld", "234 State Avenue", "New York", "NY", "92345")
# database.add("Kramer", "Kramer", "234 State Avenue", "New York", "NY", "92345")
# database.add("George", "Costanza", "234 State Avenue", "New York", "NY", "92345")
# database.add("Elaine", "Bennis", "234 State Avenue", "New York", "NY", "92345")
# database.add("Mindy", "Lahiri", "567 Goldberg Way", "San Francisco", "CA", "96543")
# database.add("Danny", "Castellano", "567 Goldberg Way", "San Francisco", "CA", "96543")
# database.add("Morgan", "Tookers", "567 Goldberg Way", "San Francisco", "CA", "96543")
# database.add("Jeremy", "Reed", "567 Goldberg Way", "San Francisco", "CA", "96543")
