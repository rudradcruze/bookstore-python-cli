from user.user import User
from datetime import datetime

def update_user(user_handler):
    print("\n=== Update a User ===")

    users = user_handler.load_data()
    if not users:
        print("No users available to update.")
        return

    username_to_update = None
    while username_to_update is None:
        username_input = input("Enter the username of the user to update: ").strip()
        if not username_input:
            print("Error: Username cannot be empty.")
        else:
            username_to_update = username_input

    user_to_update = None
    for user in users:
        if user['username'] == username_to_update:
            user_to_update = user
            break

    if not user_to_update:
        print(f"Error: No user found with username '{username_to_update}'.")
        return

    print(f"\nFound user: {user_to_update['full_name']} ({user_to_update['username']})")
    print("Enter new values (or press Enter to keep the current value).")

    password = None
    while password is None:
        password_input = input(f"Enter new password [{user_to_update['password']}]: ").strip()
        if not password_input:
            password = user_to_update['password']
        elif len(password_input) < 4:
            print("Error: Password must be at least 4 characters long.")
        else:
            password = password_input

    full_name = None
    while full_name is None:
        full_name_input = input(f"Enter new full name [{user_to_update['full_name']}]: ").strip()
        if not full_name_input:
            full_name = user_to_update['full_name']
        elif not all(c.isalpha() or c.isspace() or c in "'-" for c in full_name_input):
            print("Error: Full name must contain only letters, spaces, apostrophes, or hyphens.")
        else:
            full_name = full_name_input

    email = None
    while email is None:
        email_input = input(f"Enter new email [{user_to_update['email']}]: ").strip()
        if not email_input:
            email = user_to_update['email']
        elif '@' not in email_input or '.' not in email_input:
            print("Error: Email must contain '@' and a domain (e.g., user@domain.com).")
        else:
            email = email_input

    role = None
    while role is None:
        role_input = input(f"Enter new role (user/admin) [{user_to_update['role']}]: ").strip().lower()
        if not role_input:
            role = user_to_update['role']
        elif role_input not in ["user", "admin"]:
            print("Error: Role must be 'user' or 'admin'.")
        else:
            role = role_input

    # Preserve the original date_joined
    date_joined = user_to_update.get('date_joined', '')
    if not date_joined:
        # If there was no date_joined, add the current date
        date_joined = datetime.now().strftime("%Y-%m-%d")

    updated_user = User(username_to_update, password, full_name, email, role, date_joined)

    updated_users = []
    for user in users:
        if user['username'] == username_to_update:
            updated_users.append({
                'username': updated_user.username,
                'password': updated_user.password,
                'full_name': updated_user.full_name,
                'email': updated_user.email,
                'role': updated_user.role,
                'date_joined': updated_user.date_joined
            })
        else:
            updated_users.append(user)

    user_handler.save_data(updated_users)
    print(f"User '{username_to_update}' updated successfully!")
