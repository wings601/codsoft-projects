import tkinter as tk
from tkinter import messagebox

# Sample data structure for contacts
contacts = []

# Function to add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contacts.append({"Name": name, "Phone": phone, "Email": email, "Address": address})
        messagebox.showinfo("Success", "Contact added successfully!")
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)
        view_contacts()
    else:
        messagebox.showwarning("Input Error", "Name and Phone are required.")

# Function to display the contact list
def view_contacts():
    listbox.delete(0, tk.END)
    for contact in contacts:
        listbox.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")

# Function to search contacts
def search_contact():
    query = search_entry.get().lower()
    listbox.delete(0, tk.END)
    for contact in contacts:
        if query in contact['Name'].lower() or query in contact['Phone']:
            listbox.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")

# Function to delete a contact
def delete_contact():
    selected_contact = listbox.curselection()
    if selected_contact:
        del contacts[selected_contact[0]]
        view_contacts()
    else:
        messagebox.showwarning("Selection Error", "Please select a contact to delete.")

# GUI setup
root = tk.Tk()
root.title("Contact Management System")

# Input fields for adding a contact
tk.Label(root, text="Name").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Phone").grid(row=1, column=0)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1)

tk.Label(root, text="Email").grid(row=2, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1)

tk.Label(root, text="Address").grid(row=3, column=0)
address_entry = tk.Entry(root)
address_entry.grid(row=3, column=1)

tk.Button(root, text="Add Contact", command=add_contact).grid(row=4, columnspan=2)

# Search bar and listbox for displaying contacts
tk.Label(root, text="Search").grid(row=5, column=0)
search_entry = tk.Entry(root)
search_entry.grid(row=5, column=1)
tk.Button(root, text="Search", command=search_contact).grid(row=5, column=2)

listbox = tk.Listbox(root)
listbox.grid(row=6, columnspan=3, sticky='nsew')

tk.Button(root, text="Delete Contact", command=delete_contact).grid(row=7, columnspan=3)

# Main loop
view_contacts()
root.mainloop()
