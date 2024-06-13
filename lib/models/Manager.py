import datetime
from .database_config import CONN,CURSOR
class Manager:
    def __init__(self,name):
        self._name = name
        self.date = datetime.datetime.now()
        self.id = self.add_manager()
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
    def create_manager(cls,name):
        """Create a new manager instance"""
        return cls(name)
    def add_manager(self):
        """Add a new manager instance"""
        sql="""
            INSERT INTO managers (manager_name,manager_date) 
            VALUES(?,?)
            """
        CURSOR.execute(sql,(self._name,self.date))
        CONN.commit()
        manager_id = CURSOR.lastrowid
        return manager_id
    def delete_manager(self, manager_id):
        """Delete manager from the bank"""
        sql = """
               DELETE FROM managers
               WHERE manager_id = ?;
           """
        CURSOR.execute(sql,(manager_id,))
        CONN.commit()
        print(f"Manager with id: {manager_id} has been deleted.")
    @classmethod
    def get_all_managers(cls):
        """Get all managers from the database"""
        sql = """
               SELECT * FROM managers;
           """
        CURSOR.execute(sql)
        results = CURSOR.fetchall()
        return results
    @classmethod
    def find_manager_by_id(cls, manager_id):
        """Find a manager by id"""
        sql=""" SELECT * FROM managers where manager_id =?"""
        CURSOR.execute(sql,(manager_id,))
        result = CURSOR.fetchone()
        return f"Manager id: {result[0]} was created on {result[1]} by user with id: {result[2]}."