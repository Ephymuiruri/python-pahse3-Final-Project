from models.__init__ import CONN,CURSOR
from models.User import User

class TestUser:
    '''Test user class'''    
    def test_create_user(self):
        user = User.create_user("test")
        assert user.name == "test"