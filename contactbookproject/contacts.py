class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def display(self):
        print(f"{self.name} | {self.phone} | {self.email}")

# These live OUTSIDE the class - they operate on the whole list, not one contact
def add_contact(contacts, name, phone, email):
    new_contact = Contact(name, phone, email)
    contacts.append(new_contact)
    print(f"Added {name} to contacts.")

def del_contact(contacts, name):
    for contact in contacts:
        if contact.name == name:
            contacts.remove(contact)
            print(f"Deleted {name}")
            return
    print(f"{name} not found")

def view_contacts(contacts):
    if not contacts:
        print("No contacts saved")
    else:
        for contact in contacts:
            contact.display()
def save_contacts(contacts):
    with open("contacts.txt","w") as file:
        for contact in contacts:
            file.write(f"{contact.name},{contact.phone},{contact.email}\n")
def load_contacts():
    contacts = []
    try:
        with open("contacts.txt","r") as file:
            for line in file:
                name,phone,email = line.strip().split(",")
                contacts.append(Contact(name,phone,email))
    except FileNotFoundError :
        pass
    return contacts
contacts = []
contacts = load_contacts()
while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. View Contacts")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        add_contact(contacts, name, phone, email)
    elif choice == '2':
        name = input("Enter name to delete: ")
        del_contact(contacts, name)
    elif choice == '3':
        view_contacts(contacts)
    elif choice == '4':
        save_contacts(contacts)
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")