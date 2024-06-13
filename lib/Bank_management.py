from models.database_config import CONN,CURSOR
from models.User import User
from models.Deposit import Deposit
from models.Payment import Payment
from models.Loans import Loan
from models.Manager import Manager


def delete_user():
    user_id = int(input("Enter user id: "))
    User.delete_user(user_id)

def deleteDeposit():
    deposit_id = int(input("Enter deposit id: "))
    Deposit.delete_deposit(deposit_id)

def delete_loan():
    loan_id = int(input("Enter loan id: "))
    Loan.delete_loan(loan_id)

def delete_payment():
    payment_id = int(input("Enter payment id: "))
    Payment.delete_payment(payment_id)
def create_manager():
    manager_id = int(input("Enter manager id: "))
    if manager_id == 0:
        Manager.create_manager(manager_id)
    else:
        print("You are not authorized to create a manager")
def delete_manager():
    manager_id = int(input("Enter manager id: "))
    if manager_id == 0:
        Manager.delete_manager(manager_id)
    else:
        print("You are not authorized to delete a manager")
def get_all_managers():
    manager_id =input("Enter manager id:")
    if manager_id == 0:
        managers = Manager.get_all_managers()
        for manager in managers:
            print(f"{manager[1]} is a manager at We Bank Limited")
    else:
        print("You are not authorized to view all managers")
def find_manager_by_id():
    manager_id = int(input("Enter manager id: "))
    if manager_id == 0:
        manager = Manager.find_manager_by_id(manager_id)
        print(manager)
    else:
        print("You are not authorized to find a manager")