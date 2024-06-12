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
    
    @classmethod
    def delete_payment(cls, payment_id):
        """Delete payment from the bank"""
        sql1 ="""SELECT recipient_id,user_id,payment_amount FROM payments WHERE payment_id = ?"""
        CURSOR.execute(sql1,(payment_id,))
        data = CURSOR.fetchone()
        recipient_id = data[0]
        user_id = data[1]
        amount = data[2]
        CURSOR.execute(sql1,(recipient_id,))
        CONN.commit()
        sql = """
               DELETE FROM payments
               WHERE payment_id = ?;
           """
        CURSOR.execute(sql,(payment_id,))
        CONN.commit()
        result2 = User.update_user(user_id,amount)
        result3 = User.update_user(recipient_id,0-amount)
        print(f"Payment of id: {payment_id} has been deleted restoring Kshs.{amount} to your account")
    @classmethod
    def get_all_payments(cls):
        """Returns all payments payments made"""
        sql = """
               SELECT * FROM payments;
           """
        CURSOR.execute(sql)
        results = CURSOR.fetchall()
        for instance in results:
            print(f"payment of {instance[1]} made out to user with id: {instance[4]} by user with id: {instance[3]}")

    @classmethod
    def find_payment_by_id(cls, payment_id):
        """Finds a payment by id"""
        sql=""" SELECT * FROM payments where payment_id =?"""
        CURSOR.execute(sql,(payment_id,))
        result = CURSOR.fetchone()
        return f"Payment id: {result[0]} was made on {result[1]} by user with id: {result[2]} to user with id: {result[3]} for an amount of {result[4]}."
    