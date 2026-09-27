# Contact Book (CLI)

A simple menu-driven contact book built in Python. Add, view, search,
and delete contacts from the terminal — contacts are saved to a local
JSON file so they persist between runs.

## Features
- Add a contact (name, phone, email) with basic input validation
- View all contacts, sorted alphabetically
- Search contacts by name
- Delete a contact by name
- Data persists in `contacts.json`, created automatically on first run
- Unit tests included

## Project Structure
```
contact-book/
├── main.py              # Menu-driven CLI (entry point)
├── contacts.py           # Core functions: add/find/delete/save/load
├── tests/
│   └── test_contacts.py
└── README.md
```

## Requirements
- Python 3.8 or higher
- No external dependencies — uses only the Python standard library
  (`json`, `os`)

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/{your-username}/{repo-name}.git
   cd {repo-name}
   ```

2. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. No dependencies to install — the project only uses the standard
   library.

## Usage

Run the program from the project root:
```bash
python main.py
```

You'll see a menu:
```
===== CONTACT BOOK =====
1. Add contact
2. View all contacts
3. Search contact
4. Delete contact
5. Exit
=========================
```
Type a number (1-5) and press Enter to choose an option.

## Running Tests
```bash
python -m unittest discover -v
```

## Notes
- `contacts.json` is created automatically in the project folder. Delete
  it any time to start with an empty contact book.
- Validation rules: name can't be empty or duplicate, phone must be at
  least 7 digits (numbers only), email must contain `@` and `.`.
