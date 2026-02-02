class User:
    user_count = 0
    def __init__(self, email):
        self.email = email
        User.user_count += 1
    @staticmethod
    def is_valid_email(email):
        return "@" in email and "." in email
    @classmethod
    def total_users(cls):
        return cls.user_count
u1 = User("a@test.com")
u2 = User("b@test.com")
print(User.is_valid_email("x@y.com")) 
print(User.total_users())              