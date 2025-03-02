USER_FIELDNAMES = ['username', 'password', 'full_name', 'email', 'role', 'date_joined']

def read_users(user_handler):
    print("\n=== View All Users ===")

    users = user_handler.load_data()
    if not users:
        print("No users available.")
        return

    print(f"Found {len(users)} user(s):")
    for user in users:
        print(f"Username: {user['username']}, Name: {user['full_name']}, Email: {user['email']}, "
              f"Role: {user['role']}")