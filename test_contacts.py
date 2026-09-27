"""
tests/test_contacts.py
Run with: python -m unittest discover -v
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from contacts import add_contact, find_contacts, delete_contact, sorted_by_name


class TestContactBook(unittest.TestCase):
    def setUp(self):
        self.contacts = []

    def test_add_contact(self):
        c = add_contact(self.contacts, "Asha Patel", "9876543210", "asha@mail.com")
        self.assertEqual(c["name"], "Asha Patel")
        self.assertEqual(len(self.contacts), 1)

    def test_add_empty_name_raises(self):
        with self.assertRaises(ValueError):
            add_contact(self.contacts, "  ", "9876543210", "a@mail.com")

    def test_add_bad_phone_raises(self):
        with self.assertRaises(ValueError):
            add_contact(self.contacts, "Bob", "12a45", "bob@mail.com")

    def test_add_bad_email_raises(self):
        with self.assertRaises(ValueError):
            add_contact(self.contacts, "Bob", "9876543210", "bobmail.com")

    def test_add_duplicate_name_raises(self):
        add_contact(self.contacts, "Bob", "9876543210", "bob@mail.com")
        with self.assertRaises(ValueError):
            add_contact(self.contacts, "bob", "1112223333", "bob2@mail.com")

    def test_find_contacts(self):
        add_contact(self.contacts, "Asha Patel", "9876543210", "asha@mail.com")
        add_contact(self.contacts, "Ravi Kumar", "9123456789", "ravi@mail.com")
        results = find_contacts(self.contacts, "asha")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "Asha Patel")

    def test_delete_contact(self):
        add_contact(self.contacts, "Asha Patel", "9876543210", "asha@mail.com")
        deleted = delete_contact(self.contacts, "asha patel")
        self.assertTrue(deleted)
        self.assertEqual(len(self.contacts), 0)

    def test_delete_missing_contact(self):
        deleted = delete_contact(self.contacts, "Nobody")
        self.assertFalse(deleted)

    def test_sorted_by_name(self):
        add_contact(self.contacts, "Zara", "9876543210", "z@mail.com")
        add_contact(self.contacts, "Asha", "9123456789", "a@mail.com")
        names = [c["name"] for c in sorted_by_name(self.contacts)]
        self.assertEqual(names, ["Asha", "Zara"])


if __name__ == "__main__":
    unittest.main()
