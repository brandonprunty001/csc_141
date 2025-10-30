class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}\n")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back.\n")

user1 = User("Brandon", "Smith", 25, "Baltimore")
user2 = User("Ava", "Johnson", 30, "New York")
user3 = User("Liam", "Davis", 22, "Chicago")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
