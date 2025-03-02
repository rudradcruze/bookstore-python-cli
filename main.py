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


BOOK_FIELDNAMES = ['title', 'author', 'isbn', 'genre', 'price', 'quantity', 'publisher', 'year_published']
USER_FIELDNAMES = ['username', 'password', 'full_name', 'email', 'role', 'date_joined']
PURCHASE_FIELDNAMES = ['username', 'isbn', 'title', 'quantity', 'total_amount', 'payment_method', 'purchase_date']


ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

def display_header():
    """Display a stylized header for the application."""
    print("\n" + "=" * 60)
    print("█▓▒░  BOOK STORE MANAGEMENT SYSTEM  ░▒▓█".center(60))
    print("=" * 60)

def display_login_menu():
    """Display the initial login menu with styling."""
    display_header()
    print("\n" + "-" * 30 + " LOGIN OPTIONS " + "-" * 30)
    print("│ 1. Login to Existing Account                                            │")
    print("│ 2. Register (Create a New Account)                                      │")
    print("│ 3. Exit Application                                                     │")
    print("-" * 74)
    return get_menu_choice(3)

def display_admin_menu(username):
    """Display the administrator menu with styling."""
    display_header()
    print(f"\n📚 Welcome, Administrator {username}! 📚".center(60))
    print("\n" + "-" * 28 + " ADMIN MENU " + "-" * 29)
    print("│ 1.  📕 Add New Book                                               │")
    print("│ 2.  📋 View All Books                                             │")
    print("│ 3.  📝 Update Book Details                                        │")
    print("│ 4.  🗑️  Delete Book                                                │")
    print("│ 5.  🔍 Search Books                                               │")
    print("│ 6.  👤 Create New User                                            │")
    print("│ 7.  👥 View All Users                                             │")
    print("│ 8.  ✏️  Update User Details                                        │")
    print("│ 9.  ❌ Delete User                                                │")
    print("│ 10. 💰 View All Purchases                                         │")
    print("│ 11. 🚪 Logout and Exit                                            │")
    print("-" * 70)
    return get_menu_choice(11)

def display_customer_menu(username):
    """Display the customer menu with styling."""
    display_header()
    print(f"\n📚 Welcome, {username}! 📚".center(60))
    print("\n" + "-" * 27 + " CUSTOMER MENU " + "-" * 27)
    print("│ 1. 📋 Browse All Books                                    │")
    print("│ 2. 🔍 Search for Books                                    │")
    print("│ 3. 🛒 Purchase Books                                      │")
    print("│ 4. 📜 View My Purchase History                            │")
    print("│ 5. 🚪 Logout and Exit                                     │")
    print("-" * 74)
    return get_menu_choice(5)

def get_menu_choice(max_option):
    """Get and validate user menu choice."""
    while True:
        try:
            choice = input("\n🔸 Please select an option: ").strip()
            choice_num = int(choice)
            if 1 <= choice_num <= max_option:
                return choice_num
            else:
                print(f"❌ Error: Please enter a number between 1 and {max_option}.")
        except ValueError:
            print("❌ Error: Please enter a valid number.")

def display_table_header(headers):
    """Display a formatted table header."""
    header_text = " │ ".join(h.center(15) for h in headers)
    print("┌" + "─" * (len(header_text) + 4) + "┐")
    print("│ " + header_text + " │")
    print("├" + "─" * (len(header_text) + 4) + "┤")

def display_table_row(data):
    """Display a formatted table row."""
    row_text = " │ ".join(str(d).center(15) for d in data)
    print("│ " + row_text + " │")

def display_table_footer(header_length):
    """Display a formatted table footer."""
    print("└" + "─" * header_length + "┘")

def get_input(prompt, is_password=False):
    """Get user input with a styled prompt."""
    if is_password:
        return input(f"🔹 {prompt}: ")
    return input(f"🔹 {prompt}: ").strip()

def display_success(message):
    """Display a success message with styling."""
    print(f"\n✅ SUCCESS: {message}")

def display_error(message):
    """Display an error message with styling."""
    print(f"\n❌ ERROR: {message}")

def display_info(message):
    """Display an informational message with styling."""
    print(f"\nℹ️  INFO: {message}")

def confirmation_prompt(message):
    """Display a confirmation prompt and return True if user confirms."""
    response = input(f"\n⚠️ {message} (y/n): ").strip().lower()
    return response == 'y'


def main():
    book_handler = DataHandler('books.csv', BOOK_FIELDNAMES)
    user_handler = DataHandler('users.csv', USER_FIELDNAMES)
    purchase_handler = DataHandler('purchases.csv', PURCHASE_FIELDNAMES)

    choice = display_login_menu()
    
    if choice == 3:
        display_info("Thank you for using Book Store Management System. Goodbye!")
        return

    current_user = None
    if choice == 1:
        
        print("\n" + "-" * 30 + " USER LOGIN " + "-" * 30)
        username = get_input("Enter username")
        password = get_input("Enter password", is_password=True)
        
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            current_user = User(ADMIN_USERNAME, ADMIN_PASSWORD, "Admin User", "admin@bookstore.com", "admin")
        else:
            users = user_handler.load_data()
            for user_data in users:
                user = User(user_data['username'], user_data['password'], user_data['full_name'],
                            user_data['email'], user_data['role'])
                if user.username == username and user.check_password(password):
                    current_user = user
                    break
                    
        if not current_user:
            display_error("Invalid username or password")
            return
            
    elif choice == 2:
        
        create_user(user_handler)
        display_success("Account created successfully!")
        
        print("\n" + "-" * 30 + " USER LOGIN " + "-" * 30)
        username = get_input("Enter username")
        password = get_input("Enter password", is_password=True)
        
        users = user_handler.load_data()
        for user_data in users:
            user = User(user_data['username'], user_data['password'], user_data['full_name'],
                        user_data['email'], user_data['role'])
            if user.username == username and user.check_password(password):
                current_user = user
                break
                
        if not current_user:
            display_error("Login failed after registration")
            return


    while True:
        if current_user.is_admin():
            choice = display_admin_menu(current_user.username)
            
            if choice == 1:
                add_book(book_handler)
            elif choice == 2:
                view_all_books(book_handler)
            elif choice == 3:
                update_book(book_handler)
            elif choice == 4:
                delete_book(book_handler)
            elif choice == 5:
                search_book(book_handler)
            elif choice == 6:
                create_user(user_handler)
            elif choice == 7:
                read_users(user_handler)
            elif choice == 8:
                update_user(user_handler)
            elif choice == 9:
                delete_user(user_handler)
            elif choice == 10:
                view_purchases(purchase_handler, book_handler=book_handler, user_handler=user_handler,)
            elif choice == 11:
                display_info(" Logging out. Thank you for using Book Store Management System!")
                break
        else:
            choice = display_customer_menu(current_user.username)
            
            if choice == 1:
                view_all_books(book_handler)
            elif choice == 2:
                search_book(book_handler)
            elif choice == 3:
                buy_book(book_handler, purchase_handler, current_user)
            elif choice == 4:
                view_purchases(purchase_handler, book_handler=book_handler, user_handler=user_handler, username=current_user.username)
            elif choice == 5:
                display_info("Logging out. Thank you for using Book Store Management System!")
                break
                
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()