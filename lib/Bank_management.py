from models.database_config import CONN,CURSOR
from models.User import User
from models.Deposit import Deposit
from models.Payment import Payment
from models.Loans import Loan
from models.Manager import Manager


def delete_user():
    manager_id = input("Enter your manager id: ")
    sql =""" SELECT manager_id FROM managers WHERE manager_id = ?"""
    CURSOR.execute(sql,(manager_id,))
    result = CURSOR.fetchone()
    if result[0] == True:
        user_id = int(input("Enter user id: "))
        delete =User.delete_user(user_id)
        return [delete]
    else:
        return ["You are not authorized to delete a user"]
def deleteDeposit():
    manager_id = input("Enter your manager id: ")
    sql =""" SELECT manager_id FROM managers WHERE manager_id = ?"""
    CURSOR.execute(sql,(manager_id,))
    result = CURSOR.fetchone()
    if result[0] == True:
        deposit_id = int(input("Enter deposit id: "))
        delete =Deposit.delete_deposit(deposit_id)
        return [delete]
    else:
        return ["You are not authorized to delete a deposit"]
def delete_loan():
    manager_id = input("Enter your manager id: ")
    sql =""" SELECT manager_id FROM managers WHERE manager_id = ?"""
    CURSOR.execute(sql,(manager_id,))
    result = CURSOR.fetchone()
    if result[0] == True:
        loan_id = int(input("Enter loan id: "))
        delete =Loan.delete_loan(loan_id)
        return [delete]
    else:
        return ["You are not authorized to delete a loan"]

def delete_payment():
    manager_id = input("Enter your manager id: ")
    sql =""" SELECT manager_id FROM managers WHERE manager_id = ?"""
    CURSOR.execute(sql,(manager_id,))
    result = CURSOR.fetchone()
    if result[0] == True:
        payment_id = int(input("Enter payment id: "))
        delete =Payment.delete_payment(payment_id)
        return [delete]
def create_manager():
    manager_id = int(input("Enter manager id: "))
    if manager_id == 0:
        name = input("Enter manager name: ")
        manager =Manager.create_manager(name)
        return [manager]
    else:
        return ["You are not authorized to create a manager"]
def delete_manager():
    manager_id = int(input("Enter manager id: "))
    if manager_id == 0:
        id=int(input("Enter manager whose id is to be deleted: "))
        manager = Manager.delete_manager(id)
        return [manager]
    else:
        return ["You are not authorized to delete a manager"]
def get_all_managers():
    manager_id =int(input("Enter manager id: "))
    if manager_id == 0:
        managers = Manager.get_all_managers()
        return [f"{manager[1]} is a manager at We Bank Limited"for manager in managers]
    else:
        return ["You are not authorized to view all managers"]
def find_manager_by_id():
    manager_id = int(input("Enter manager id: "))
    if manager_id == 0:
        id =int(input("Enter the id of maneager to find: "))
        manager = Manager.find_manager_by_id(id)
        return [manager]
    else:
        return ["You are not authorized to find a manager"]