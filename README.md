# 📚 Book Store Management System

A simple yet powerful command-line application for managing a bookstore's inventory, users, and purchases.

## 🚀 Overview

The **Book Store Management System** is a Python-based command-line application designed to streamline bookstore operations. It offers separate functionalities for administrators and customers through an intuitive interface with stylized menus, tables, and prompts. The system uses CSV files for persistent storage to manage books, user accounts, and purchase records, making it an efficient tool for small-scale bookstore management.

## 🌟 Features

### For Administrators:

-   📕 Add New Book: Add books with details such as title, author, ISBN, genre, price, quantity, publisher, and year published.
-   📋 View All Books: Display all books in a formatted table.
-   📝 Update Book Details: Edit book information using ISBN.
-   🗑️ Delete Book: Remove books from the inventory.
-   🔍 Search Books: Search by title, author, ISBN, or genre.
-   👤 Create New User: Register users with roles (admin or customer).
-   👥 View All Users: List all registered users in a table.
-   ✏️ Update User Details: Modify user information.
-   ❌ Delete User: Remove user accounts.
-   💰 View All Purchases: Access a full list of customer purchases.

### For Customers:

-   📋 Browse All Books: View the complete book inventory.
-   🔍 Search for Books: Find books by title, author, ISBN, or genre.
-   🛒 Purchase Books: Buy books and log transactions with payment details.
-   📜 View My Purchase History: Review personal purchase history.

## 🛠️ Installation

-   python 3 or higher

1. Clone the repository:

```bash
git clone https://github.com/rudradcruze/bookstore-python-cli.git
```

2. Navigate to the project directory:

```bash
cd bookstore-python-cli
```

3. Run the application:

```bash
python main.py
```

## 📝 Usage

### Initial Login Menu

1. Login to Existing Account: Enter username and password.
2. Register (Create a New Account): Create a new user account.
3. Exit Application: Exit the program.

### Administrator Menu

Administrators (e.g., default `admin`/`admin123`) can:

1. Manage books (add, view, update, delete, search).
2. Manage users (create, view, update, delete).
3. Review all purchase records.

### Customer Menu

1. Browse and search the book inventory.
2. Purchase books.
3. View their own purchase history.

## 📂 Project Structure

```
bookstore-python-cli/
│
├── book/
│   ├── add_book.py         # Add a new book to inventory
│   ├── delete_book.py      # Remove a book from inventory
│   ├── update_book.py      # Update book details
│   ├── search_book.py      # Search books by various criteria
│   └── view_all_books.py   # Display all books
│
├── user/
│   ├── create_user.py      # Register a new user
│   ├── read_users.py       # View all users
│   ├── update_user.py      # Modify user details
│   └── delete_user.py      # Delete a user account
│
├── data_handler.py         # Manages CSV file operations
├── buy_book.py             # Handles book purchases
├── view_purchases.py       # Displays purchase history
├── main.py                 # Main application entry point
├── books.csv               # Stores book data
├── users.csv               # Stores user data
└── purchases.csv           # Stores purchase records
```

-   book/: Contains book management modules.
-   user/: Contains user management modules.
-   CSV Files: Store data persistently.

### User Authentication

-   Admin Access: Default credentials are admin/admin123.
-   Customer Registration: Users can sign up and log in.
-   Security Note: Passwords are plain text (not production-ready).

### Book Management

-   Books are identified by ISBN.
-   Admins can add, update, delete, and search books.

### Purchase Management

-   Customers purchase books, updating quantities and logging transactions.
-   Admins view all purchases; customers view their own.

## 🚀 About Me

Tech-savvy designer/programmer pushing boundaries of online tech. Passionate about new tools, seeking challenges to advance skills.

## 🔗 Social Links

Email: [francisrudra@gmail.com](mailto:francisrudra@gmail.com)

![Name](https://img.shields.io/badge/Name-Francis%20Rudra%20D%20Cruze-yellowgreen?style=for-the-badge)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rudradcruze)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/rudradcruze)
[![Facebook](https://img.shields.io/badge/facebook-4267B2?style=for-the-badge&logo=facebook&logoColor=white)](https://facebook.com/rudradcruze)
[![francisrudra@gmail.com](https://img.shields.io/badge/gmail-4267B2?style=for-the-badge&logo=gmail&logoColor=white)](mailto:francisrudra@gmail.com)
