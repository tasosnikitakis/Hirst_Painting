class User:

    def __init__(self, user_id, username):
        print("New user being created...")
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1





user_1 = User("001", "tasos")
user_2 = User("002", "Dina")

user_1.follow(user_2)
print(user_1.following)
print(user_2.followers)
