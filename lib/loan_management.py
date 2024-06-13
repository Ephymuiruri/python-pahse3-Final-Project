from models.database_config import CONN,CURSOR
from models.Deposit import Deposit
from models.Payment import Payment
from models.Loans import Loan
def make_loan():
    user_id = int(input("Enter user id: "))
    amount = int(input("Enter amount: "))
    date_due = int(input("Enter date due: "))
    loan=Loan.create_loan(amount,user_id,date_due)
    return [loan]
def get_all_loans():
    result =Loan.get_all_loans()
    return [f"Loan of {loan[1]} made on {loan[2]} by user with id: {loan[3]}" for loan in result]
def find_loan_by_id():
    loan_id = int(input("Enter loan id: "))
    loan = Loan.find_loan_by_id(loan_id)
    return [loan]
def find_user_loans():
    user_id=input("please enter your user_id: ")
    result=Loan.find_user_loans(user_id)
    return [f" You received a loan of {loan[1]} made on {loan[2]} and is due on {loan[4]}" for loan in result]

