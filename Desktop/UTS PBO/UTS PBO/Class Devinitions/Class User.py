class User:
    def __init__(self, user_id, username, password):
        self.user_id = user_id
        self.username = username
        self.password = password

    def get_user_id(self):
        return self.user_id
    
    def get_username(self):
        return self.username
    
    def set_password(self, password):
        self.password = password


user1 = User("23025", "olivia", "smngt")


print("User Information:")
print("User ID:", user1.get_user_id())
print("Username:", user1.get_username())
print("Password:", user1.password)