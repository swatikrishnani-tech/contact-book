# Problem Statement

## Contact Book (CLI)

Keeping track of personal contacts — names, phone numbers, and email
addresses — is one of the most common small tasks a personal computer
is used for. In practice this information often ends up scattered
across notes apps, saved chat messages, or a phone's built-in address
book, none of which are easy to search, back up, or version-control.

Without a dedicated, lightweight tool, personal contact details tend
to accumulate in an unstructured way — spread across notes, messages,
and device-specific address books that are difficult to search
consistently or move between systems.

## The Problem

There is a need for a simple, dependency-free command-line application
that:

- Lets a user **add, view, search, and delete** contacts
- **Validates entries at the point of entry**, so obviously malformed
  data (an empty name, a non-numeric phone number, a malformed email)
  is rejected immediately rather than silently accepted
- **Persists the contact list** between sessions without requiring a
  database server or a graphical interface
- Is approachable to build and run as a first Python project — no
  external dependencies, no installation steps beyond having Python
  itself

## Solution

This project implements a menu-driven Contact Book that runs entirely
in the terminal, storing contacts in a local JSON file
(`contacts.json`). It uses only the Python standard library (`json`,
`os`) and separates the interactive menu (`main.py`) from the core
logic (`contacts.py`), keeping the logic independently testable.

See `README.md` for setup and usage instructions, and
`Contact_Book_Project_Report.docx` for the full project report.
