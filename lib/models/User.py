#lib/User.py

import datetime
from .database_config import CONN,CURSOR
class User:
    def __init__(self,name):
        self._name = name
        self.date =datetime.datetime.now()
        self.amount = 0.00
        self.id = self.add_user()
        print(self)
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if not isinstance(name,str):
            raise TypeError("Name must be a string.")
        self._name = name
    def __repr__(self):
        return f"Your username is: {self._name} while your password/id is: {self.id}."
    @classmethod
    def create_user(cls,name):
        """Create a new user instance"""
        return cls(name)

    def add_user(self):
        """Create a new user in database"""
        sql = """
               INSERT INTO  users (user_name,Amount,date_created)
               VALUES(?,?,?);
           """
        CURSOR.execute(sql,(self._name,self.amount,self.date))
        CONN.commit()
        user_id = CURSOR.lastrowid
        return user_id
    @classmethod
    def update_user(cls,user_id,amount):
        """Update a user in the database"""
        sql1 ="""SELECT amount FROM users WHERE user_id = ?"""
        CURSOR.execute(sql1,(user_id,))
        result = CURSOR.fetchone()
        amount = result[0] + amount
        amount = round(amount,4)
        sql = """
               UPDATE users
               SET Amount = ?
               WHERE user_id =?;
           """
        CURSOR.execute(sql,(amount,user_id))
        CONN.commit()
        return amount
    @classmethod
    def delete_user(self, user_id):
        """Delete a user from the database"""
        sql = """
               DELETE FROM users
               WHERE user_id =?;
           """
        CURSOR.execute(sql,(user_id,))
        CONN.commit()
        print(f"User {user_id} has been deleted.")
    @classmethod
    def get_all_users(self):
        """Get all users from the database"""
        sql = """
               SELECT user_name FROM users;
           """
        CURSOR.execute(sql)
        result = CURSOR.fetchall()
        return ([user[0] for user in result])
    @classmethod
    def find_user_by_id(cls, user_id):
        """Find a user by id"""
        sql = """
               SELECT user_name FROM users
               WHERE user_id =?;
           """
        CURSOR.execute(sql,(user_id,))
        result = CURSOR.fetchone()
        return f"User's name is: {result[0]}"

    
