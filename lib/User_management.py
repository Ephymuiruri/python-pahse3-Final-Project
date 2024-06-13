# lib/helpers.py
from models.User import User

def create_user():
    name = input("Enter your name: ")
    user = User.create_user(name)
def get_all_users():
    users = User.get_all_users()
    for user in users:
        print(user)
def find_user_by_id():
    user_id = int(input("Enter user id: "))
    user_name = User.find_user_by_id(user_id)
    print(user_name)

def exit_program():
    print("Goodbye!")
    exit()
