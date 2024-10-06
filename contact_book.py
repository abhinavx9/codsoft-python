#simplified contact book application in python
contacts = {}

# function to add a new contact
def add_contact():
    name = input("enter contact name:").strip()
    phone = input("enter phone number:").strip()
    contacts[name] = phone
    print(f"contact {name} added successfully!")
#function to view all contacts
def view_contact():
    if not contacts():
        print("No contact Found.")
    else:
        for name, phone in contacts.items():
            print(f"Name : {name}, Phone: {contacts}")
#function to search for contact by name
def search_contact():
    name = input("enter contact name to search: ").strip()
    if name in contacts:
        print(f"name: {name},Phone : {contacts}")
    else:
        print("contact not found.")
#function to delete contacts
def delete_contact():
    name=input("enter the name of the contact to delete;").strip()
    del contact[name]
    print(f"contect {name} deleted successfully!")
else:
print("contact not found.")
#function to display menu
def display_menu():
    print("/n--- Contact Manager ---")
    print("1. Add Contact")
    print("2. View all contact")
    print("3. search contact")
    print("4. Update Contact")
    print("5. Delete contact")
    print("6.Exit!!")
#main program loop
    while True:
        display_menu()
        choice = input("choose an option (1-6): ").strip()
    if choice == '1' :
        add_contact()
    elif choice == '2' :
        view_contact()
    elif choice == '3' :
        search_contact()
    elif choice == '4' :
        update_contact()
    elif choice == '5' :
        delete_contact()
    elif choice == '6' :
        print("Exiting")
        break
    else:
        print("Invalid option")