# lib/helpers.py
from models.User import User
from rich.console import Console
from rich.text import Text
#from cli import main

console = Console()
def create_user():
    name = input("Enter your name: ")
    user = User.create_user(name)
    return [user]
def get_all_users():
    users = User.get_all_users()
    return users
def find_user_by_id():
    user_id = int(input("Enter user id: "))
    user_name = User.find_user_by_id(user_id)
    return [user_name]

def exit_program():
    print("Goodbye!")
    exit()
