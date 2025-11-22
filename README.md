📊 Expense Tracker (Python + SQLite)

A simple and efficient command-line Expense Tracker built using Python + SQLite.
This project helps you track your daily expenses with features to add, view, update, delete, search, and filter expenses easily.

🚀 Features
✔ Add Expense

Add a new expense with:

Title

Amount

Category

Date (YYYY-MM-DD)

✔ View All Expenses

Displays all stored expenses in a clean tabular format.

✔ Delete Expense

Delete any expense using its unique ID.

✔ Update Expense

Modify existing records:

Title

Amount

Category

Date

✔ Filter by Category

View expenses belonging to a specific category.

✔ Filter by Date Range

Useful for weekly, monthly, or custom range reports.

✔ Search Expenses

Search using partial text in:

Title

Date

🛠️ Technologies Used

Python

SQLite

SQL Queries

VS Code

📁 Project Structure
Expense-Tracker/
│
├── main.py               # Handles menu + user interaction
├── crud_operations.py    # Add, view, update, delete, filter, search functions
├── db_setup.py           # Creates SQLite database + table
├── expense.db            # Auto-generated SQLite database file
└── README.md             # Project documentation

▶️ How to Run the Project
1️⃣ Create the Database

Run this file once:

python db_setup.py

2️⃣ Start the Expense Tracker

Run the main program:

python main.py

🖼️ Screenshots
🔹 Main Menu
<img src="https://github.com/professor66607/Expense-Tracker/blob/main/Screenshot%202025-11-22%20212139.png?raw=true" width="600px">




🔹 Add Expense
<img src="https://github.com/professor66607/Expense-Tracker/blob/main/Screenshot%202025-11-22%20212203.png?raw=true" width="600px">





👤 Author

Yashwanth Gowda
Developer | Python Enthusiast
Feel free to connect or contribute 😊

📜 License

This project is licensed under the MIT License.
