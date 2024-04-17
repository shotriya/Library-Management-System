 

import book_management
import user_management
import checkout_management

def main_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. List Books")
    print("3. Add User")
    print("4. Checkout Book")
    print("5. Exit")
    choice = input("Enter choice: ")
    return choice

def main():
    book_manager = book_management.BookManager()
    user_manager = user_management.UserManager()
    checkout_manager = checkout_management.CheckoutManager(book_manager, user_manager)

    while True:
        choice = main_menu()
        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            try:
                book_manager.add_book(title, author, isbn)
                print("Book added.")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == '2':
            book_manager.list_books()
        elif choice == '3':
            name = input("Enter user name: ")
            user_id = input("Enter user ID: ")
            try:
                user_manager.add_user(name, user_id)
                print("User added.")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == '4':
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to checkout: ")
            try:
                checkout_manager.checkout_book(user_id, isbn)
                print("Book checked out.")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == '5':
            print("Exiting.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
