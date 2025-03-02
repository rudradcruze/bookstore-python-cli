USER_FIELDNAMES = ['username', 'password', 'full_name', 'email', 'role', 'date_joined']

def delete_user(user_handler):
    print("\n=== Delete a User ===")

    users = user_handler.load_data()
    if not users:
        print("No users available to delete.")
        return

    username_to_delete = None
    while username_to_delete is None:
        username_input = input("Enter the username of the user to delete: ").strip()
        if not username_input:
            print("Error: Username cannot be empty.")
        else:
            username_to_delete = username_input

    user_found = False
    updated_users = []
    for user in users:
        if user['username'] == username_to_delete:
            user_found = True
            print(f"Deleting user: {user['full_name']} ({user['username']})")
        else:
            updated_users.append(user)

    if user_found:
        user_handler.save_data(updated_users)
        print(f"User '{username_to_delete}' has been successfully removed.")
    else:
        print(f"Error: No user found with username '{username_to_delete}'.")