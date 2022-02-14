
from tkinter import *
from database import Database

root = Tk()
root.title("Address Book")
root.geometry("665x400")

database = Database("adddress_book.db")

# Populate address_list
def populate_list():
    address_list.delete(0, END)
    for row in database.fetch():
        address_list.insert(END, row)
        
# Button Functions
def add(self):
    pass

def remove(self):
    pass

def edit(self):
    pass

def clear(self):
    pass


# Labels and Entries
first_name_label = Label(root, text="First Name", font=("bold"))
first_name_label.grid(row=0, column=0, padx=(20,0), pady=(20,0), sticky=W)
first_name = Entry(root)
first_name.grid(row=0, column=1, padx=20, pady=(20,0))

last_name_label = Label(root, text="Last Name", font=("bold"))
last_name_label.grid(row=0, column=2, padx=(20,0), pady=(20,0), sticky=W)
last_name = Entry(root)
last_name.grid(row=0, column=3, padx=20, pady=(20,0))

address_label = Label(root, text="Address", font=("bold"))
address_label.grid(row=1, column=0, padx=(20,0), sticky=W)
address = Entry(root)
address.grid(row=1, column=1, padx=20)

city_label = Label(root, text="City", font=("bold"))
city_label.grid(row=1, column=2, padx=(20,0), sticky=W)
city = Entry(root)
city.grid(row=1, column=3, padx=20)

state_label = Label(root, text="State", font=("bold"))
state_label.grid(row=2, column=0, padx=(20,0), pady=(0, 20), sticky=W)
state = Entry(root)
state.grid(row=2, column=1, padx=20, pady=(0, 20))

zipcode_label = Label(root, text="Zipcode", font=("bold"))
zipcode_label.grid(row=2, column=2, padx=(20,0), pady=(0, 20), sticky=W)
zipcode = Entry(root)
zipcode.grid(row=2, column=3, padx=20, pady=(0, 20))

# Buttons 
add_button = Button(root, text="Add Entry", command=add)
add_button.grid(row=6, column=0, padx=(20,0), pady=(0,10))
remove_button = Button(root, text="Remove Entry", command=remove)
remove_button.grid(row=6, column=1, pady=(0,10))
edit_button = Button(root, text="Edit Entry", command=edit)
edit_button.grid(row=6, column=2, pady=(0,10))
clear_button = Button(root, text="Clear Input", command=clear)
clear_button.grid(row=6, column=3, pady=(0,10))

# Address List
address_list = Listbox(root, height=11, width=68)
address_list.grid(row=7, column=0, columnspan=4, padx=(20,0), pady=(20,0), sticky=W)

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.grid(row=7, column=3, padx=(0, 25), sticky=E)

address_list.bind("<<")

# Set scrollbar to address_list
address_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=address_list.yview)

populate_list()


root.mainloop()