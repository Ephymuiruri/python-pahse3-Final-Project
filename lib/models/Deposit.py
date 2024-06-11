import datetime
from lib.models.__init__ import CONN,CURSOR
from lib.models.User import User
class Deposit:
    all=[]
    def __init__(self,amount,user_id):
        if not isinstance(user_id,int):
            raise TypeError("User id must be an integer.")
        self._amount = amount
        self.user_id = user_id
        self.date = datetime.datetime.now()
        self.id = self.add_deposit()
        self.all.append(self)
        print(self)
        self.add_deposit_user()
    @property
    def amount(self):
        return self._amount
    @amount.setter
    def amount(self,amount):
        if not isinstance(amount,int):
            raise TypeError("Amount must be an integer.")
        self._amount = amount
    def __repr__(self):
        return f"You deposited {self._amount} on {self.date}."
    @classmethod
    def create_deposit(cls,amount,user_id):
        """Create a new deposit instance"""
        return cls(amount,user_id)
    def add_deposit(self):
        """add a new deposit to the database"""
        sql="""
            INSERT INTO deposits (deposit_amount,deposit_date,user_id) 
            VALUES(?,?,?)
            """
        CURSOR.execute(sql,(self._amount,self.date,self.user_id))
        CONN.commit()
        deposit_id = CURSOR.lastrowid
        return deposit_id
    def add_deposit_user(self):
        id = self.user_id
        amount = self.amount
        result = User.update_user(id,amount)
        print (f"New Bank Total after deposit is:{result}")
    

        

