"""
main.py
Menu-driven command-line interface for the Contact Book.
Run with: python main.py
"""

from contacts import (
    load_contacts,
    save_contacts,
    add_contact,
    find_contacts,
    delete_contact,
    sorted_by_name,
)

MENU = """
===== CONTACT BOOK =====
1. Add contact
2. View all contacts
3. Search contact
4. Delete contact
5. Exit
=========================
"""


def print_contact(c: dict) -> None:
    print(f"  Name : {c['name']}")
    print(f"  Phone: {c['phone']}")
    print(f"  Email: {c['email']}")
    print("  " + "-" * 20)


def handle_add(contacts: list) -> None:
    name = input("Name: ")
    phone = input("Phone (digits only): ")
    email = input("Email: ")
    try:
        contact = add_contact(contacts, name, phone, email)
        save_contacts(contacts)
        print(f"Added '{contact['name']}' successfully.")
    except ValueError as e:
        print(f"Could not add contact: {e}")


def handle_view(contacts: list) -> None:
    if not contacts:
        print("No contacts saved yet.")
        return
    print(f"\n{len(contacts)} contact(s):\n")
    for c in sorted_by_name(contacts):
        print_contact(c)


def handle_search(contacts: list) -> None:
    keyword = input("Search by name: ")
    results = find_contacts(contacts, keyword)
    if not results:
        print("No matching contacts.")
        return
    for c in results:
        print_contact(c)


def handle_delete(contacts: list) -> None:
    name = input("Name to delete: ")
    if delete_contact(contacts, name):
        save_contacts(contacts)
        print(f"Deleted '{name}'.")
    else:
        print(f"No contact named '{name}' found.")


def main() -> None:
    contacts = load_contacts()
    actions = {
        "1": handle_add,
        "2": handle_view,
        "3": handle_search,
        "4": handle_delete,
    }

    while True:
        print(MENU)
        choice = input("Choose an option (1-5): ").strip()

        if choice == "5":
            print("Goodbye!")
            break
        elif choice in actions:
            actions[choice](contacts)
        else:
            print("Invalid choice, please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
