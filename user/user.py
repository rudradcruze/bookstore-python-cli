class User:
    def __init__(self, username, password, full_name, email, role="user", date_joined=None):
        self.username = username
        self.password = password
        self.full_name = full_name
        self.email = email
        self.role = role

    def __str__(self):
        return f"User: {self.username}, Name: {self.full_name}, Email: {self.email}, Role: {self.role}"

    def check_password(self, password):
        return self.password == password

    def is_admin(self):
        return self.role.lower() == "admin"