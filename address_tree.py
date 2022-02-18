from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
from xml.dom.pulldom import END_ELEMENT
# from tree_database import TreeDatabase

debug = False

root = Tk()
root.title("Address Book")
root.geometry("700x455")


# Faux data
# entries = [
#     [1, "Rachel", "Green", "123 Park Avenue", "New York", "NY", "95123"],
#     [2, "Ross", "Geller", "123 Park Avenue", "New York", "NY", "95123"],
#     [3, "Joey", "Tribbiani", "456 Rosten Road", "New York", "NY", "95123"],
#     [4, "Chandler", "Bing", "789 Primrose Street", "New York", "NY", "95123"],
#     [5, "Monica", "Geller", "012 Hatten Drive", "New York", "NY", "95123"],
#     [6, "Phoebe", "Buffet", "345 Rosita Avenue", "New York", "NY", "95123"],
#     [7, "Sheldon", "Cooper", "678 Linwood Road", "Santa Monica", "CA", "94567"],
#     [8, "Leonard", "Hofstader", "678 Linwood Road", "Santa Monica", "CA", "94567"],
#     [9, "Rajesh", "Koothrapalli", "678 Linwood Road", "Santa Monica", "CA", "94567"],
#     [10, "Howard", "Wolowitz", "678 Linwood Road", "Santa Monica", "CA", "94567"],
#     [11, "Douglas", "Heffernan", "901 Woodrow Drive", "Trentor", "NJ", "94789"],
#     [12, "Carrie", "Heffernan", "901 Woodrow Drive", "Trentor", "NJ", "94789"],
#     [13, "Arthur", "Spooner", "901 Woodrow Drive", "Trentor", "NJ", "94789"],
#     [14, "Jerry", "Seinfeld", "234 State Avenue", "New York", "NY", "92345"],
#     [15, "Kramer", "Kramer", "234 State Avenue", "New York", "NY", "92345"],
#     [16, "George", "Costanza", "234 State Avenue", "New York", "NY", "92345"],
#     [17, "Elaine", "Bennis", "234 State Avenue", "New York", "NY", "92345"],
#     [18, "Mindy", "Lahiri", "567 Goldberg Way", "San Francisco", "CA", "96543"],
#     [19, "Danny", "Castellano", "567 Goldberg Way", "San Francisco", "CA", "96543"],
#     [20, "Morgan", "Tookers", "567 Goldberg Way", "San Francisco", "CA", "96543"],
#     [21, "Jeremy", "Reed", "567 Goldberg Way", "San Francisco", "CA", "96543"]
# ]

# Database
connection = sqlite3.connect("tree_database.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY AUTOINCREMENT, first_name text, last_name text, address text, city text, state text, zipcode text)")

# Add entries to table
# for entry in entries:
#     cursor.execute("INSERT or IGNORE INTO contacts VALUES (NULL, :first_name, :last_name, :address, :city, :state, :zipcode)", 
#     { 
#         "first_name": entry[1],
#         "last_name": entry[2],
#         "address": entry[3],
#         "city": entry[4],
#         "state": entry[5],
#         "zipcode": entry[6]
#     })

connection.commit()
connection.close()

def fetch_entries():
    if debug: print("initialized fetch_entries()")

    connection = sqlite3.connect("tree_database.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM contacts")
    friends = cursor.fetchall()
    
    for friend in friends:
        if debug: print(friend)

        address_tree.insert(parent="", index="end", text="", values=(friend[0], friend[1], friend[2], friend[3], friend[4], friend[5], friend[6]))

    connection.commit()
    connection.close()

def add_entry():
    if debug: print("initialized add_entry()")

    if first_name_entry.get() == "" or last_name_entry.get() == "" or address_entry.get() == "" or city_entry.get() == "" or state_entry.get() =="" or zipcode_entry.get() == "":
        messagebox.showerror("Required Fields", "All fields are required")
        return

    connection = sqlite3.connect("tree_database.db")
    cursor = connection.cursor()

    cursor.execute("INSERT INTO contacts VALUES (NULL, :first_name, :last_name, :address, :city, :state, :zipcode)", 
        {
            # "ID": count, 
            "first_name": first_name.get(), 
            "last_name": last_name.get(), 
            "address": address.get(),
            "city": city.get(),
            "state": state.get(),
            "zipcode": zipcode.get()
        })

    connection.commit()
    connection.close()

    for row in address_tree.get_children():
        address_tree.delete(row)

    address_tree.insert("", END, values=(first_name_entry.get(), last_name_entry.get(), address_entry.get(), city_entry.get(), state_entry.get(), zipcode_entry.get()))

    clear_input()
    fetch_entries()

def remove_entry():
    if debug: print("initialized remove_entry()")

    connection = sqlite3.connect("tree_database.db")
    cursor = connection.cursor()

    selected_entry = address_tree.item(address_tree.focus(), "values")
    id = selected_entry[0]

    if debug: print(id)

    cursor.execute(f"DELETE FROM contacts WHERE ID='{id}'")

    connection.commit()
    connection.close()

    for entry in address_tree.selection():
        if debug: print(address_tree.selection)

        address_tree.delete(entry)

    clear_input()

def select_entry(event):  
    first_name_entry.delete(0, END)
    last_name_entry.delete(0, END)
    address_entry.delete(0, END)
    city_entry.delete(0, END)
    state_entry.delete(0, END)
    zipcode_entry.delete(0, END)

    selected_entry = address_tree.item(address_tree.focus(), "values")

    if debug: print(selected_entry)

    if not selected_entry:
        if debug: print(selected_entry[0])
        return

    first_name_entry.insert(END, selected_entry[1])
    last_name_entry.insert(END, selected_entry[2])
    address_entry.insert(END, selected_entry[3])
    city_entry.insert(END, selected_entry[4])
    state_entry.insert(END, selected_entry[5])
    zipcode_entry.insert(END, selected_entry[6])

def update_entry():
    if debug: print("initialized update_entry()")

    connection = sqlite3.connect("tree_database.db")
    cursor = connection.cursor()

    selected_entry = address_tree.item(address_tree.focus(), "values")
    id = selected_entry[0]

    if debug: print(id)

    cursor.execute(f"UPDATE contacts SET first_name=?, last_name=?, address=?, city=?, state=?, zipcode=? WHERE ID=?", (first_name, last_name, address, city, state, zipcode, id))

    connection.commit()
    connection.close()

    address_tree.item(address_tree.focus(), text="", values=(selected_entry[0], first_name_entry.get(), last_name_entry.get(), address_entry.get(), city_entry.get(), state_entry.get(), zipcode_entry.get()))

    first_name_entry.delete(0, END)
    last_name_entry.delete(0, END)
    address_entry.delete(0, END)
    city_entry.delete(0, END)
    state_entry.delete(0, END)
    zipcode_entry.delete(0, END)

def clear_input():
    if debug: print("initialized clear_input()")

    first_name_entry.delete(0, END)
    last_name_entry.delete(0, END)
    address_entry.delete(0, END)
    city_entry.delete(0, END)
    state_entry.delete(0, END)
    zipcode_entry.delete(0, END)

def delete_all():
    if debug: print("initialized delete_all()")

    response = messagebox.askyesno("askyesno", "Are you sure you want to delete ALL records?")

    if response == 1:
        connection = sqlite3.connect("tree_database.db")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM contacts")
        connection.commit()
        connection.close()

        for entry in address_tree.get_children():
            address_tree.delete(entry)

#  Address Treeview
address_tree = ttk.Treeview(root, height=11)
address_tree.grid(row=7, column=0, columnspan=7, padx=(20,0), pady=(20,0), sticky=W)

# Columns
address_tree["columns"] = ("ID", "First Name", "Last Name", "Address", "City", "State", "Zipcode")

# Format columns
address_tree.column("#0", width=0, minwidth=0, stretch=NO)
address_tree.column("ID", anchor=CENTER, width=30)
address_tree.column("First Name", anchor=W, width=100)
address_tree.column("Last Name", anchor=W, width=100)
address_tree.column("Address", anchor=W, width=200)
address_tree.column("City", anchor=W, width=100)
address_tree.column("State", anchor=W, width=50)
address_tree.column("Zipcode", anchor=W, width=60)

# Headings
address_tree.heading("#0", text="", anchor=W)
address_tree.heading("ID", text="ID", anchor=CENTER)
address_tree.heading("First Name", text="First Name", anchor=W)
address_tree.heading("Last Name", text="Last Name", anchor=W)
address_tree.heading("Address", text="Address", anchor=W)
address_tree.heading("City", text="City", anchor=W)
address_tree.heading("State", text="State", anchor=W)
address_tree.heading("Zipcode", text="Zipcode", anchor=W)

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.grid(row=7, column=7, pady=(20,0), sticky=N+S+E)

# Attach scrollbar to address_tree
address_tree.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=address_tree.yview)

# Bind select
address_tree.bind("<<TreeviewSelect>>", select_entry)

# Labels and Entries
first_name = StringVar()
first_name_label = Label(root, text="First Name", font=("bold"))
first_name_label.grid(row=0, column=0, padx=(20,0), pady=(20,0), sticky=W)
first_name_entry = Entry(root, textvariable=first_name)
first_name_entry.grid(row=0, column=1, padx=20, pady=(20,0))

last_name = StringVar()
last_name_label = Label(root, text="Last Name", font=("bold"))
last_name_label.grid(row=0, column=2, padx=(20,0), pady=(20,0), sticky=W)
last_name_entry = Entry(root, textvariable=last_name)
last_name_entry.grid(row=0, column=3, padx=20, pady=(20,0))

address = StringVar()
address_label = Label(root, text="Address", font=("bold"))
address_label.grid(row=1, column=0, padx=(20,0), sticky=W)
address_entry = Entry(root, textvariable=address)
address_entry.grid(row=1, column=1, padx=20)

city = StringVar()
city_label = Label(root, text="City", font=("bold"))
city_label.grid(row=1, column=2, padx=(20,0), sticky=W)
city_entry = Entry(root, textvariable=city)
city_entry.grid(row=1, column=3, padx=20)

state = StringVar()
state_label = Label(root, text="State", font=("bold"))
state_label.grid(row=2, column=0, padx=(20,0), pady=(0, 20), sticky=W)
state_entry = Entry(root, textvariable=state)
state_entry.grid(row=2, column=1, padx=20, pady=(0, 20))

zipcode = StringVar()
zipcode_label = Label(root, text="Zipcode", font=("bold"))
zipcode_label.grid(row=2, column=2, padx=(20,0), pady=(0, 20), sticky=W)
zipcode_entry = Entry(root, textvariable=zipcode)
zipcode_entry.grid(row=2, column=3, padx=20, pady=(0, 20))

# Buttons 
add_button = Button(root, text="Add Entry", command=add_entry)
add_button.grid(row=6, column=0, padx=(20,0), pady=(0,10))
remove_button = Button(root, text="Remove Entry", command=remove_entry)
remove_button.grid(row=6, column=1, pady=(0,10))
update_button = Button(root, text="Update Entry", command=update_entry)
update_button.grid(row=6, column=2, pady=(0,10))
clear_button = Button(root, text="Clear Input", command=clear_input)
clear_button.grid(row=6, column=3, pady=(0,10))
delete_btn = Button(root, text="Delete All", command=delete_all)
delete_btn.grid(row=8, column=0, columnspan=4, padx=(65, 0), ipadx=80, pady=(8,20))
    
fetch_entries()

root.mainloop()
