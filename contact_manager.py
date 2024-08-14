import tkinter as tk
from tkinter import messagebox
import json
import os

# File to store contacts
CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return {}

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file)

# Add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()

    if name == "" or phone == "" or email == "":
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    if name in contacts:
        messagebox.showwarning("Input Error", "Contact with this name already exists!")
        return

    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    update_contact_list()
    clear_entries()

# Update the contact list display
def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for name in contacts:
        contact_listbox.insert(tk.END, name)

# Clear input fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

# View selected contact details
def view_contact():
    try:
        selected_contact = contact_listbox.get(contact_listbox.curselection())
        contact = contacts[selected_contact]
        name_entry.delete(0, tk.END)
        name_entry.insert(0, selected_contact)
        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, contact["phone"])
        email_entry.delete(0, tk.END)
        email_entry.insert(0, contact["email"])
    except tk.TclError:
        messagebox.showwarning("Selection Error", "Please select a contact to view!")

# Edit an existing contact
def edit_contact():
    selected_contact = contact_listbox.get(contact_listbox.curselection())
    if selected_contact in contacts:
        new_name = name_entry.get()
        new_phone = phone_entry.get()
        new_email = email_entry.get()

        if new_name == "" or new_phone == "" or new_email == "":
            messagebox.showwarning("Input Error", "All fields are required!")
            return

        # Update contact
        del contacts[selected_contact]
        contacts[new_name] = {"phone": new_phone, "email": new_email}
        save_contacts(contacts)
        update_contact_list()
        clear_entries()
    else:
        messagebox.showwarning("Selection Error", "Please select a contact to edit!")

# Delete a contact
def delete_contact():
    try:
        selected_contact = contact_listbox.get(contact_listbox.curselection())
        if messagebox.askyesno("Delete Confirmation", f"Are you sure you want to delete {selected_contact}?"):
            del contacts[selected_contact]
            save_contacts(contacts)
            update_contact_list()
            clear_entries()
    except tk.TclError:
        messagebox.showwarning("Selection Error", "Please select a contact to delete!")

# Create the main application window
app = tk.Tk()
app.title("Contact Management System")

# Contacts in memory
contacts = load_contacts()

# GUI Elements

# Labels and Entry widgets for contact information
tk.Label(app, text="Name").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(app)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(app, text="Phone").grid(row=1, column=0, padx=10, pady=5)
phone_entry = tk.Entry(app)
phone_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(app, text="Email").grid(row=2, column=0, padx=10, pady=5)
email_entry = tk.Entry(app)
email_entry.grid(row=2, column=1, padx=10, pady=5)

# Listbox to display contacts
contact_listbox = tk.Listbox(app, width=50)
contact_listbox.grid(row=0, column=2, rowspan=6, padx=10, pady=5)

# Buttons for actions
add_button = tk.Button(app, text="Add Contact", command=add_contact)
add_button.grid(row=3, column=0, columnspan=2, pady=5)

view_button = tk.Button(app, text="View Contact", command=view_contact)
view_button.grid(row=4, column=0, columnspan=2, pady=5)

edit_button = tk.Button(app, text="Edit Contact", command=edit_contact)
edit_button.grid(row=5, column=0, columnspan=2, pady=5)

delete_button = tk.Button(app, text="Delete Contact", command=delete_contact)
delete_button.grid(row=6, column=0, columnspan=2, pady=5)

# Initialize the contact list display
update_contact_list()

# Run the application
app.mainloop()
