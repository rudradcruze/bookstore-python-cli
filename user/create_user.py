from user.user import User
from data_handler import DataHandler

USER_FIELDNAMES = ['username', 'password', 'full_name', 'email', 'role', 'date_joined']

def create_user(user_handler):
    print("\n=== Create a New User ===")

    existing_users = user_handler.load_data()
    existing_usernames = {user['username'] for user in existing_users}

    username = None
    while username is None:
        username_input = input("Enter username: ").strip()
        if not username_input:
            print("Error: Username cannot be empty.")
        elif username_input in existing_usernames:
            print("Error: This username is already taken.")
        elif not username_input.isalnum():
            print("Error: Username must contain only letters and numbers.")
        else:
            username = username_input

    password = None
    while password is None:
        password_input = input("Enter password: ").strip()
        if not password_input:
            print("Error: Password cannot be empty.")
        elif len(password_input) < 4:
            print("Error: Password must be at least 4 characters long.")
        else:
            password = password_input

    full_name = None
    while full_name is None:
        full_name_input = input("Enter full name: ").strip()
        if not full_name_input:
            print("Error: Full name cannot be empty.")
        elif not all(c.isalpha() or c.isspace() or c in "'-" for c in full_name_input):
            print("Error: Full name must contain only letters, spaces, apostrophes, or hyphens.")
        else:
            full_name = full_name_input

    email = None
    while email is None:
        email_input = input("Enter email: ").strip()
        if not email_input:
            print("Error: Email cannot be empty.")
        elif '@' not in email_input or '.' not in email_input:
            print("Error: Email must contain '@' and a domain (e.g., user@domain.com).")
        else:
            email = email_input

    role = None
    while role is None:
        role_input = input("Enter role (user/admin) [default: user]: ").strip().lower()
        if not role_input:
            role = "user"
        elif role_input not in ["user", "admin"]:
            print("Error: Role must be 'user' or 'admin'.")
        else:
            role = role_input


    new_user = User(username, password, full_name, email, role)

    user_dict = {
        'username': new_user.username,
        'password': new_user.password,
        'full_name': new_user.full_name,
        'email': new_user.email,
        'role': new_user.role,
    }
    user_handler.append_data(user_dict)
    print(f"User '{username}' created successfully!")