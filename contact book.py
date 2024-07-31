contact_book = {}

while True:
    print("\nContact Book Menu:\n")
    print("1. Add a new contact")
    print("2. View all contacts")
    print("3. Update an existing contact")
    print("4. Delete a contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        name = input("Enter the contact name: ")
        phone = input("Enter the contact phone number: ")
        contact_book[name] = phone
        print(f"Contact {name} added successfully!")

    elif choice == '2':
        if not contact_book:
            print("No contacts found.")
        else:
            for name, phone in contact_book.items():
                print(f"Name: {name}, Phone: {phone}")

    elif choice == '3':
        name = input("Enter the contact name to update: ")
        if name in contact_book:
            phone = input(f"Enter the new phone number for {name}: ")
            contact_book[name] = phone
            print(f"Contact {name} updated successfully!")
        else:
            print(f"Contact {name} not found.")

    elif choice == '4':
        name = input("Enter the contact name to delete: ")
        if name in contact_book:
            del contact_book[name]
            print(f"Contact {name} deleted successfully!")
        else:
            print(f"Contact {name} not found.")

    elif choice == '5':
        print("Exiting contact book. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

