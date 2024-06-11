from datetime import datetime,date
from lib.models.__init__ import CONN,CURSOR
from lib.models.User import User
class Loan:

    def __init__(self,amount,userid,date_due):
        if not isinstance(amount,int) and not isinstance(userid,int) and not isinstance(date_due,int):
            raise TypeError("Amount,user id,date_due must be integers.")
        self.amount = amount
        self.user_id = userid
        self.date_due = date_due
        self.date = datetime.now()
        self.id = self.add_loan()
        self.add_loan_user()
    @classmethod
    def create_loan(cls,amount,userid,date_due):
        """Create a new loan instance"""
        return cls(amount,userid,date_due)
    def add_loan(self):
        """add a loan to the account in the database"""
        sql ="""INSERT INTO loans (loan_amount,loan_date,user_id,date_due)
                VALUES (?,?,?,?)
            """
        CURSOR.execute(sql,(self.amount,self.date,self.user_id,self.date_due))
        CONN.commit()
        loan_id = CURSOR.lastrowid
        return loan_id
    def add_loan_user(self):
        id = self.user_id
        amount = self.amount
        result = User.update_user(id,amount)
        print (f"New Bank Total after loan is:{result}")
    

        
        