#lib/Deposit.py
import datetime
from .database_config import CONN,CURSOR
from .User import User
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

    @classmethod
    def delete_deposit(cls, deposit_id):
        """Delete deposit from bank"""
        sql1 =""" SELECT deposit_amount,user_id FROM deposits WHERE deposit_id = ?"""
        CURSOR.execute(sql1,(deposit_id,))
        result = CURSOR.fetchone()
        amount = result[0]
        user_id = result[1]
        amount = 0-amount
        result = User.update_user(user_id,amount)

        sql="""
              DELETE FROM deposits WHERE deposit_id =?;
           """
        CURSOR.execute(sql,(deposit_id,))
        CONN.commit()
        print(f"Deposit {deposit_id} has been deleted.New Bank Total after deleting deposit is:{result}")
    @classmethod
    def get_all_deposits(cls):
        """Get all deposits from the database"""
        sql = """
               SELECT * FROM deposits;
           """
        CURSOR.execute(sql)
        result = CURSOR.fetchall()
        for deposit in result:
            print(f"Deposit of {deposit[1]} made on {deposit[2]} by user with id: {deposit[3]}")

    @classmethod
    def find_deposit_by_id(cls, deposit_id):
        """Finds a deposit by id"""
        sql=""" SELECT * FROM deposits where deposit_id =?"""
        CURSOR.execute(sql,(deposit_id,))
        result = CURSOR.fetchone()
        return f"Deposit id: {result[0]} was made on {result[2]} by user with id: {result[3]} for an amount of {result[1]}."
        
    

        

