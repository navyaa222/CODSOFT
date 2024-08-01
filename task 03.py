
class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name} | {self.phone} | {self.email} | {self.address}"

contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact = Contact(name, phone, email, address)
    contacts.append(contact)
    print("Contact added successfully!")

def view_contacts():
    if contacts:
        for contact in contacts:
            print(contact)
    else:
        print("No contacts found.")

def search_contact():
    search_term = input("Enter name or phone number to search: ")
    found_contacts = [c for c in contacts if search_term in c.name or search_term in c.phone]
    if found_contacts:
        for contact in found_contacts:
            print(contact)
    else:
        print("No contacts found.")

def update_contact():
    search_term = input("Enter name or phone number of the contact to update: ")
    contact = next((c for c in contacts if search_term in c.name or search_term in c.phone), None)
    if contact:
        contact.name = input(f"Enter new name (current: {contact.name}): ") or contact.name
        contact.phone = input(f"Enter new phone number (current: {contact.phone}): ") or contact.phone
...     contact.email = input(f"Enter new email (current: {contact.email}): ") or contact.email
...     contact.address = input(f"Enter new address (current: {contact.address}): ") or contact.address
...         print("Contact updated successfully!")
...     else:
...         print("Contact not found.")
... 
... def delete_contact():
...     search_term = input("Enter name or phone number of the contact to delete: ")
...     global contacts
...     contacts = [c for c in contacts if not (search_term in c.name or search_term in c.phone)]
...     print("Contact deleted if it existed.")
... 
... def main():
...     while True:
...         print("\nContact Management System")
...         print("1. Add Contact")
...         print("2. View Contacts")
...         print("3. Search Contact")
...         print("4. Update Contact")
...         print("5. Delete Contact")
...         print("6. Exit")
... 
...         choice = input("Enter your choice (1-6): ")
... 
...         if choice == '1':
...             add_contact()
...         elif choice == '2':
...             view_contacts()
...         elif choice == '3':
...             search_contact()
...         elif choice == '4':
...             update_contact()
...         elif choice == '5':
...             delete_contact()
...         elif choice == '6':
...             print("Exiting the program.")
...             break
...         else:
...             print("Invalid choice. Please enter a number between 1 and 6.")
... 
... if __name__ == "__main__":
      main()
