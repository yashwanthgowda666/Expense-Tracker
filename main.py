from crud_operations import *


def main():
    while True:
        print("\n===== EXPENSE TRACKER MENU =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Delete Expense")
        print("4. Update Expense")
        print("5. Filter by Category")
        print("6. Filter by Date Range")
        print("7. Search Expenses")
        print("8. Exit")
        
        
        
        choice = input("Enter your choice:\n")
        if choice == "1":
            title = input("Enter Title: ")
            amount = float(input("Enter Amount: "))
            category = input("Enter Category: ")
            date = input("Enter Date (YYYY-MM-DD): ")
            add_expense(title, amount, category, date)

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            expense_id = int(input("Enter Expense ID to delete: "))
            delete_expenses(expense_id)

        elif choice == "4":
            expense_id = int(input("Enter Expense ID to update: "))
            new_title = input("New Title: ")
            new_amount = float(input("New Amount: "))
            new_category = input("New Category: ")
            new_date = input("New Date (YYYY-MM-DD): ")
            update_expense(expense_id, new_title, new_amount, new_category, new_date)

        elif choice == "5":
            category = input("Enter Category: ")
            filter_by_category(category)

        elif choice == "6":
            start_date = input("Enter Start date (YYYY-MM-DD): ")
            end_date = input("Enter End date (YYYY-MM-DD): ")
            filter_by_date_range(start_date, end_date)

        elif choice == "7":
            keyword = input("Enter Keyword to search: ")
            search_expenses(keyword)
        elif choice == "8":
            print("Exiting program...")
            break
        else:
            print("Invalid choice, try again.")


main()

