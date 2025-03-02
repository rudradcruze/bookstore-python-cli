from user.user import User
from data_handler import DataHandler
from book.add_book import add_book
from book.delete_book import delete_book
from book.update_book import update_book
from book.search_book import search_book
from book.view_all_books import view_all_books
from user.create_user import create_user
from user.read_users import read_users
from user.update_user import update_user
from user.delete_user import delete_user
from buy_book import buy_book
from view_purchases import view_purchases

# Fieldnames for CSV files
BOOK_FIELDNAMES = ['title', 'author', 'isbn', 'genre', 'price', 'quantity', 'publisher', 'year_published']
USER_FIELDNAMES = ['username', 'password', 'full_name', 'email', 'role', 'date_joined']
PURCHASE_FIELDNAMES = ['username', 'isbn', 'title', 'quantity', 'total_amount', 'payment_method', 'purchase_date']

# Predefined admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

def login(user_handler):
    print("\n=== Login ===")
    users = user_handler.load_data()
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        return User(ADMIN_USERNAME, ADMIN_PASSWORD, "Admin User", "admin@bookstore.com", "admin")
    for user_data in users:
        user = User(user_data['username'], user_data['password'], user_data['full_name'],
                    user_data['email'], user_data['role'])
        if user.username == username and user.check_password(password):
            return user
    print("Error: Invalid username or password.")
    return None

def display_menu(is_admin):
    print("\n=== Book Store Management System ===")
    if is_admin:
        print("1. Add Book")
        print("2. View All Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Search Books")
        print("6. Create User")
        print("7. View All Users")
        print("8. Update User")
        print("9. Delete User")
        print("10. View All Purchases")
        print("11. Exit")
    else:
        print("1. View All Books")
        print("2. Search Books")
        print("3. Buy Book")
        print("4. Exit")
    print("==============================")

def main():
    book_handler = DataHandler('books.csv', BOOK_FIELDNAMES)
    user_handler = DataHandler('users.csv', USER_FIELDNAMES)
    purchase_handler = DataHandler('purchases.csv', PURCHASE_FIELDNAMES)

    print("Welcome to the Book Store Management System!")
    print("1. Login")
    print("2. Register (Create an Account)")
    print("3. Exit")
    
    choice = None
    while choice is None:
        choice_input = input("Select an option (1-3): ").strip()
        if choice_input not in ['1', '2', '3']:
            print("Error: Please select 1, 2, or 3.")
        else:
            choice = choice_input

    if choice == '3':
        print("Goodbye!")
        return

    current_user = None
    if choice == '1':
        current_user = login(user_handler)
        if not current_user:
            print("Login failed. Exiting.")
            return
    elif choice == '2':
        create_user(user_handler)
        print("Account created! Please login.")
        current_user = login(user_handler)
        if not current_user:
            print("Login failed after registration. Exiting.")
            return

    is_admin = current_user.is_admin()
    print(f"\nLogged in as: {current_user.username} ({current_user.role})")
    while True:
        display_menu(is_admin)
        option = input("Select an option: ").strip()

        if is_admin:
            if option == '1':
                add_book(book_handler)
            elif option == '2':
                view_all_books(book_handler)
            elif option == '3':
                update_book(book_handler)
            elif option == '4':
                delete_book(book_handler)
            elif option == '5':
                search_book(book_handler)
            elif option == '6':
                create_user(user_handler)
            elif option == '7':
                read_users(user_handler)
            elif option == '8':
                update_user(user_handler)
            elif option == '9':
                delete_user(user_handler)
            elif option == '10':
                view_purchases(purchase_handler)
            elif option == '11':
                print("Goodbye!")
                return
            else:
                print("Error: Invalid option.")
        else:
            if option == '1':
                view_all_books(book_handler)
            elif option == '2':
                search_book(book_handler)
            elif option == '3':
                buy_book(book_handler, purchase_handler, current_user)
            elif option == '4':
                print("Goodbye!")
                return
            else:
                print("Error: Invalid option.")

if __name__ == "__main__":
    main()