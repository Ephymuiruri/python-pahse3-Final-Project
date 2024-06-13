from models.database_config import CONN,CURSOR
from models.Deposit import Deposit
from models.Payment import Payment

def make_payment():
    user_id = int(input("Enter user id: "))
    recipient_id = int(input("Enter recipient id: "))
    amount = int(input("Enter amount: "))
    Payment.create_payment(user_id,recipient_id,amount)
def find_payment():
    user_name =input("Enter user name: ")
    user_id = int(input("Enter user id: "))
    sql = """SELECT user_id FROM users WHERE user_id = ? and user_name = ?"""
    CURSOR.execute(sql,(user_id,user_name))
    result = CURSOR.fetchone()
    if result[0] == True:
        input(f"your presence has been verified\nplease enter your payment_id: ")
        payment = Payment.find_payment_by_id(user_name,user_id)
        print(payment)
    else:
        print("sorry we could  not find a user with the id {user_id}")

def find_payments_user():
    user_id = int(input("Enter user id: "))
    payments = Payment.find_payments_user(user_id)
    for payment in payments:
        print(f"A payment of {payment[1]} was sent to customer with id {payment[4]} on {payment[2]}")


def get_all_payments():
    payments = Payment.get_all_payments()
    for instance in payments:
        print(f"payment of {instance[1]} made out to user with id: {instance[4]} by user with id: {instance[3]}")




def make_deposit():
    user_id = int(input("Enter user id: "))
    amount = int(input("Enter amount: "))
    Deposit.create_deposit(user_id,amount)
def get_all_deposits():
    deposits = Deposit.get_all_deposits()
    for deposit in deposits:
        print(deposit)
def find_deposit_by_id():
    deposit_id = int(input("Enter deposit id: "))
    deposit = Deposit.find_deposit_by_id(deposit_id)
    print(deposit)
def find_deposit_user():
    user_id = int(input("Enter user id: "))
    deposits = Deposit.find_user_deposits(user_id)
    for deposit in deposits:
        print(f"Deposit of {deposit[1]} made on {deposit[2]} by user with id: {deposit[3]}")

