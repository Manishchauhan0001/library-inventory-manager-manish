# library-inventory-manager-manish
📚 Library Inventory Manager

A fully Object-Oriented, JSON-based, Menu-Driven Library Management System built with Python.

This CLI application helps manage a library’s book records with persistent storage, structured modules, and robust error handling—ideal for learning and demonstrating Python OOP and file handling concepts.

🚀 Key Highlights ✅ Object-Oriented Architecture

Book class with encapsulated fields & methods

LibraryInventory class for catalog management

✅ JSON Storage

Auto-load & auto-save book records

Graceful recovery from missing/corrupt JSON

✅ Menu-Based CLI

Add Book

Issue Book

Return Book

Search (Title / ISBN)

View All Books

✅ Error Handling + Logging

Input validation

File I/O error management

INFO & ERROR-level logging

✅ Clean & Modular Project Structure

Python package for logic

Separate CLI layer

Data + Test directories

📁 Project Structure library-inventory-manager-manish/ │ ├── library_manager/ │ ├── init.py │ ├── book.py │ ├── inventory.py │ ├── cli/ │ ├── main.py │ ├── data/ │ ├── books.json │ ├── tests/ │ ├── test_app.py │ ├── README.md ├── requirements.txt └── .gitignore

▶️ How to Run 1️⃣ Open Terminal / CMD cd library-inventory-manager

2️⃣ Run the Program

Recommended:

python -m cli.main

Or:

python cli/main.py

3️⃣ Use the Menu === Library Inventory Manager ===

Add Book
Issue Book
Return Book
View All Books
Search Book
Exit
🧩 Core Components 📘 Book Class

Handles:

Issue / Return operations

Availability checks

Conversion to/from dictionaries

📚 LibraryInventory Class

Responsible for:

Adding books

Saving/loading JSON

Searching by title/ISBN

Displaying full catalog
