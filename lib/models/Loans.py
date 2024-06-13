#lib/Loans.py
from datetime import datetime
from .database_config import CONN,CURSOR
from .User import User
class Loan:

    def __init__(self,amount,userid,date_due):
        if not isinstance(amount,int) and not isinstance(userid,int) and not isinstance(date_due,int):
            raise TypeError("Amount,user id,date_due must be integers.")
        self.amount = amount
        self.user_id = userid
        self.date_due = date_due
        self.date = datetime.now()
        self.id = self.add_loan()
        print(self)
        self.add_loan_user()
    @classmethod
    def create_loan(cls,amount,userid,date_due):
        """Create a new loan instance"""
        return cls(amount,userid,date_due)
    def __repr__(self):
        return f"You loaned {self.amount} to user with id: {self.user_id} on {self.date_due} his loan id is {self.id}"
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
        return f"New Bank Total after loan is:{result}"
    
    @classmethod
    def delete_loan(cls, loan_id):
        """Delete loan from bank"""
        sql1 =""" SELECT loan_amount,user_id FROM loans WHERE loan_id = ?"""
        CURSOR.execute(sql1,(loan_id,))
        result = CURSOR.fetchone()
        amount = result[0]
        user_id = result[1]
        amount = 0-amount
        result = User.update_user(user_id,amount)

        sql="""
              DELETE FROM loans WHERE loan_id =?;
           """
        CURSOR.execute(sql,(loan_id,))
        CONN.commit()
        return f"Loan {loan_id} has been deleted.New Bank Total after deleting loan is:{result} For user with id {user_id}"
    @classmethod
    def get_all_loans(cls):
        """Get all loans from the database"""
        sql = """
               SELECT * FROM loans;
           """
        CURSOR.execute(sql)
        result = CURSOR.fetchall()
        return result
    
    @classmethod
    def find_loan_by_id(cls, loan_id):
        """Finds a loan by id"""
        sql=""" SELECT * FROM loans where loan_id =?"""
        CURSOR.execute(sql,(loan_id,))
        result = CURSOR.fetchone()
        return f"Loan id: {result[0]} was made on {result[2]} by user with id: {result[3]} for an amount of {result[1]}."
    @classmethod
    def find_user_loans(cls, user_id):
        """Finds a loan by id"""
        sql=""" SELECT * FROM loans where user_id =?"""
        CURSOR.execute(sql,(user_id,))
        result = CURSOR.fetchall()
        return result
    
    

        
        