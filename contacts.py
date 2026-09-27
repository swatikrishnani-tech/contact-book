"""
contacts.py
Core logic for the Contact Book. Plain functions + a JSON file for
storage -- no classes, no database -- to keep things beginner-friendly.

Each contact is a dictionary: {"name": ..., "phone": ..., "email": ...}
All contacts are stored together as a list in contacts.json.
"""

import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "contacts.json")


def load_contacts(file_path: str = DATA_FILE) -> list:
    """Load contacts from the JSON file. Returns an empty list if the
    file doesn't exist yet (first run) or is empty/corrupted."""
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, ValueError):
        return []


def save_contacts(contacts: list, file_path: str = DATA_FILE) -> None:
    """Write the contacts list back to the JSON file."""
    with open(file_path, "w") as f:
        json.dump(contacts, f, indent=2)


def add_contact(contacts: list, name: str, phone: str, email: str) -> dict:
    """Add a new contact and return it. Raises ValueError on bad input."""
    name = name.strip()
    phone = phone.strip()
    email = email.strip()

    if not name:
        raise ValueError("Name cannot be empty.")
    if not phone.isdigit() or len(phone) < 7:
        raise ValueError("Phone number must be at least 7 digits, numbers only.")
    if "@" not in email or "." not in email:
        raise ValueError("Email looks invalid (must contain '@' and '.').")
    if any(c["name"].lower() == name.lower() for c in contacts):
        raise ValueError(f"A contact named '{name}' already exists.")

    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    return contact


def find_contacts(contacts: list, keyword: str) -> list:
    """Case-insensitive search by name."""
    keyword = keyword.strip().lower()
    return [c for c in contacts if keyword in c["name"].lower()]


def delete_contact(contacts: list, name: str) -> bool:
    """Delete a contact by exact name (case-insensitive). Returns True if removed."""
    for i, c in enumerate(contacts):
        if c["name"].lower() == name.strip().lower():
            del contacts[i]
            return True
    return False


def sorted_by_name(contacts: list) -> list:
    return sorted(contacts, key=lambda c: c["name"].lower())
