import sqlite3              # To interact with SQLite database
from datetime import datetime  # To validate the date format entered by user


def get_connection():
    """
    Creates and returns a connection object to the SQLite database.
    If 'expense.db' doesn't exist, SQLite automatically creates it.
    """
    return sqlite3.connect("expense.db")


def add_expense(title, amount, category, date):
    """
    Adds a new expense record to the database after validating input data.
    """

    # ----- VALIDATIONS -----

    # Title should not be empty or whitespace
    if not title.strip():
        print("Error: Title can't be empty.")
        return

    # Amount must be a positive number
    if amount <= 0:
        print("Amount must be greater than 0.")
        return

    # Validate if date follows correct format YYYY-MM-DD
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Error: Date format should be YYYY-MM-DD.")
        return

    # ----- DATABASE INSERTION -----

    try:
        conn = get_connection()      # Connect to DB
        cursor = conn.cursor()       # Create cursor to execute SQL commands

        # Insert new expense using parameterized queries (prevents SQL injection)
        cursor.execute(
            "INSERT INTO expenses (title, amount, category, date) VALUES (?, ?, ?, ?)",
            (title, amount, category, date)
        )

        conn.commit()                # Save changes to database
        print("Expense added successfully!")

    except sqlite3.Error as e:
        # Catch any database error (ex: missing table, syntax error, locked DB)
        print("Database Error:", e)

    finally:
        conn.close()   # Always close DB connection


def view_expenses():
    """
    Fetches and displays all expense records from the database.
    """

    try:
        conn = get_connection()     # Connect to DB
        cursor = conn.cursor()

        # Select all columns and rows from 'expenses'
        cursor.execute("SELECT * FROM expenses")
        rows = cursor.fetchall()    # Retrieve all rows as a list of tuples

        # If no expenses exist, show message
        if not rows:
            print("No Expenses Found.")
            return

        # Print each expense record
        for row in rows:
            print(row)

    except sqlite3.Error as e:
        print("Database Error:", e)

    finally:
        conn.close()   # Close database connection


def delete_expenses(expense_id):
    """
    Deletes a specific expense record by its ID after checking if it exists.
    """

    try:
        conn = get_connection()
        cursor = conn.cursor()

        # First check if the record exists
        cursor.execute("SELECT * FROM expenses WHERE id = ?", (expense_id,))
        record = cursor.fetchone()

        # If no record found with given ID
        if not record:
            print("No Records Found")
            return

        # Delete the expense
        cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        conn.commit()
        print("Expense Deleted Successfully!")

    except sqlite3.Error as e:
        print("Database Error:", e)

    finally:
        conn.close()   # Close connection



def update_expense(expense_id, new_title, new_amount, new_category, new_date):
    """
    Updates an existing expense record after validating ID and new values.
    """

    try:
        conn = get_connection()      # Connect to the database
        cursor = conn.cursor()       # Create cursor for SQL operations

        # ----- STEP 1: Check if record exists -----
        cursor.execute("SELECT * FROM expenses WHERE id = ?", (expense_id,))
        record = cursor.fetchone()   # Fetch the matched expense

        if not record:
            print("Error: No record found with this ID.")
            return

        # ----- STEP 2: Validate new title -----
        if not new_title.strip():
            print("Error: Title cannot be empty.")
            return

        # ----- STEP 3: Validate new amount -----
        if new_amount <= 0:
            print("Error: Amount must be greater than 0.")
            return

        # ----- STEP 4: Validate new date format -----
        try:
            datetime.strptime(new_date, "%Y-%m-%d")
        except ValueError:
            print("Error: Date format should be YYYY-MM-DD.")
            return

        # ----- STEP 5: Update the record in database -----
        cursor.execute("""
            UPDATE expenses
            SET title = ?, amount = ?, category = ?, date = ?
            WHERE id = ?
        """, (new_title, new_amount, new_category, new_date, expense_id))

        conn.commit()     # Save changes
        print("Expense updated successfully!")

    except sqlite3.Error as e:
        print("Database Error:", e)

    finally:
        conn.close()       # Ensure DB connection is closed




def filter_by_category(category):
    """
    Filters expenses based on category.
    """

    try:
        category = category.strip()      # Remove extra spaces

        if category == "":               # Validate category
            print("Input cannot be empty.")
            return 
        
        conn = get_connection()          # Connect
        cursor = conn.cursor()

        # Case-insensitive category match
        cursor.execute("""
            SELECT * FROM expenses
            WHERE LOWER(category) = LOWER(?)
        """, (category,))

        rows = cursor.fetchall()         # Fetch matches

        if not rows:                     # No records found
            print("Expenses not found for category:", category)
            return

        # Print all matching records
        for row in rows:
            print(f"ID:{row[0]} | Title:{row[1]} | Amount:{row[2]} | Category:{row[3]} | Date:{row[4]}")

    except sqlite3.Error as e:
        print("Database Error:", e)

    finally:
        conn.close()



def filter_by_date_range(start_date, end_date):
    """
    Filters all expenses between two given dates.
    """
    try:
        # Validate start date
        try:
            datetime.strptime(start_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid start date format")
            return

        # Validate end date
        try:
            datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid end date format")
            return

        conn = get_connection()          # Connect
        cursor = conn.cursor()

        # SQL BETWEEN gets all dates within range
        cursor.execute("""
            SELECT * FROM expenses
            WHERE date BETWEEN ? AND ?
        """, (start_date, end_date))

        rows = cursor.fetchall()

        if not rows:                     # No matches
            print(f"No expenses found between {start_date} and {end_date}.")
            return

        for row in rows:                 # Print results
            print(f"ID:{row[0]} | Title:{row[1]} | Amount:{row[2]} | Category:{row[3]} | Date:{row[4]}")

    except sqlite3.Error as e:
        print("Database Error:", e)

    finally:
        conn.close()



def search_expenses(keyword):
    """
    Searches expenses by title or date using partial matching.
    """
    try:
        keyword = keyword.strip()        # Clean input
        
        if keyword == "":                # Validate keyword
            print("Keyword cannot be empty.")
            return 

        conn  = get_connection()         # Connect
        cursor = conn.cursor()

        # SQL wildcard search with LIKE
        query = """
        SELECT id, title, amount, date 
        FROM expenses
        WHERE title LIKE ? OR date LIKE ?;
        """

        search_key = f"%{keyword}%"      # Allow partial matches anywhere

        cursor.execute(query, (search_key, search_key))  # Bind same key twice
        rows = cursor.fetchall()

        if not rows:
            print("No expenses matched your search keyword.")
            return
        
        for row in rows:                 # Print results
            print(f"ID:{row[0]} | Title:{row[1]} | Amount:{row[2]} | Date:{row[3]}")

    except sqlite3.Error as e:
        print("Database Error:", e)

    finally:
        conn.close()                     # Close connection