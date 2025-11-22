# 📊 Expense Tracker (Python + SQLite)

A simple and efficient **command-line Expense Tracker** built using **Python** and **SQLite**.  
This project allows users to **add, view, update, delete, search, and filter expenses** easily.

---

## 🚀 Features

### ✔ Add Expense
Add a new expense with:
- **Title**
- **Amount**
- **Category**
- **Date (YYYY-MM-DD)**

### ✔ View All Expenses
Displays all stored expense records.

### ✔ Delete Expense
Delete an expense using its **unique ID**.

### ✔ Update Expense
Modify:
- Title  
- Amount  
- Category  
- Date  

### ✔ Filter by Category
View expenses belonging to a specific category.

### ✔ Filter by Date Range
Useful for **weekly or monthly expense tracking**.

### ✔ Search Expenses
Search using partial keywords in:
- Title  
- Date  

---

## 🛠 Technologies Used
- **Python**
- **SQLite**
- **SQL Queries**
- **VS Code**

### Project Modules
- `main.py` → Menu + user input  
- `crud_operations.py` → All database operations  
- `db_setup.py` → Database creation  

---

## 📁 Project Structure

Expense-Tracker/
│
├── main.py # Handles menu + user input
├── crud_operations.py # Add, view, update, delete, filter, search functions
├── db_setup.py # Creates SQLite database + table
├── expense.db # Auto-generated SQLite database file
└── README.md # Project documentation



---

## ▶️ How to Run the Project

### 1️⃣ Create the Database
Run this file once:
```sh
python db_setup.py
```



### 2️⃣ Start the Expense Tracker
Run the main program
```sh
python main.py
```