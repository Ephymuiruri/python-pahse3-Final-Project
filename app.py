from lib.Database.setup import (create_tables, drop_tables)
from lib.models.User import User
from lib.models.Deposit import Deposit
from lib.models.Payment import Payment
from lib.models.Loans import Loan
def main():
    drop_tables()
    create_tables()
    User1= User.create_user("Ephy")
    User2= User.create_user("Peter")
    Deposit1 = Deposit.create_deposit(1000,1)
    Deposit3 = Deposit.create_deposit(15000,2)
    payment1 = Payment.create_payment(500,1,2)
    loan1=Loan.create_loan(10000,1,12-6-2024)
if __name__ == '__main__':
    main()