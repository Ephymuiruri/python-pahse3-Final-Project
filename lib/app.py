
from Database.setup import (create_tables, drop_tables)
from models.User import User
from models.Deposit import Deposit
from models.Payment import Payment
from models.Loans import Loan
def main():
    drop_tables()
    create_tables()
    User1= User.create_user("Ephy")
    User2= User.create_user("Peter")
    Deposit1 = Deposit.create_deposit(1000,1)
    Deposit3 = Deposit.create_deposit(15000,2)
    payment1 = Payment.create_payment(500,1,2)
    payment2 = Payment.create_payment(500,2,1)
    loan1=Loan.create_loan(10000,1,12-6-2024)
    values=User1.get_all_users()


if __name__ == '__main__':
    main()