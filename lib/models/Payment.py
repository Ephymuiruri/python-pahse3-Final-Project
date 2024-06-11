import datetime
from lib.models.__init__ import CONN,CURSOR
from lib.models.User import User
class Payment:
    def __init__(self,amount,user_id,recipient_id):
        if(user_id == recipient_id):
            raise ValueError("You cannot pay yourself.")
        if not isinstance(user_id,int):
            raise TypeError("User id must be an integer.")
        if not isinstance(recipient_id,int):
            raise TypeError("Recipient id must be an integer.")
        self._amount = amount
        self.user_id = user_id
        self.recipient_id = recipient_id
        self.date = datetime.datetime.now()
        self.id = self.add_payment()
        self.add_payment_user()
    @property
    def amount(self):
        return self._amount
    @amount.setter
    def amount(self,amount):
        if not isinstance(amount,int):
            raise TypeError("Amount must be an integer.")
        self._amount = amount
    @classmethod
    def create_payment(cls,amount,user_id,recipient_id):
        """Create a new payment instance"""
        return cls(amount,user_id,recipient_id)
    def add_payment(self):
        """add a new payment to the database"""
        sql="""
            INSERT INTO payments (payment_amount,payment_date,user_id,recipient_id) 
            VALUES(?,?,?,?)
            """
        CURSOR.execute(sql,(self._amount,self.date,self.user_id,self.recipient_id))
        CONN.commit()
        payment_id = CURSOR.lastrowid
        return payment_id
    def add_payment_user(self):
        id = self.user_id
        amount1 = 0-self.amount
        result = User.update_user(id,amount1)
        result2 = User.update_user(self.recipient_id,self.amount)
        print (f"New Bank Total is:{result} after making a payment of {self.amount} to user with id:{self.recipient_id}")
    