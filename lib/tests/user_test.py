from models.database_config import CONN, CURSOR
from models.User import User
import pytest
import datetime

class TestUser:
    @pytest.fixture(autouse=True)
    def drop_table(self):
        CURSOR.execute("DROP TABLE IF EXISTS users")
        CONN.commit()
        CURSOR.execute("""CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT NOT NULL,
            Amount DECIMAL(19,4) NOT NULL,
            date_created DATE NOT NULL
        );""")
        CONN.commit()
    def test_user_initialization(self):
        user = User("John Doe")
        assert user.name == "John Doe"
        assert user.amount == 0.00
        assert isinstance(user.date, datetime.datetime)
        assert isinstance(user.id, int)

    def test_user_name_setter_getter(self):
        user = User("John Doe")
        user.name = "Jane Doe"
        assert user.name == "Jane Doe"

        with pytest.raises(TypeError):
            user.name = 123  # Non-string name should raise a TypeError

    def test_add_user(self):
        user = User("John Doe")
        CURSOR.execute("SELECT user_name FROM users WHERE user_id =?", (user.id,))
        result = CURSOR.fetchone()
        assert result is not None
        assert result[0] == "John Doe"

    def test_update_user(self):
        user = User("John Doe")
        new_amount = User.update_user(user.id, 50.00)
        assert new_amount == 50.00

        CURSOR.execute("SELECT Amount FROM users WHERE user_id =?", (user.id,))
        result = CURSOR.fetchone()
        assert result[0] == 50.00

    def test_delete_user(self):
        user = User("John Doe")
        User.delete_user(user.id)

        CURSOR.execute("SELECT * FROM users WHERE user_id =?", (user.id,))
        result = CURSOR.fetchone()
        assert result is None

    def test_get_all_users(self):
        user1 = User("John Doe")
        user2 = User("Jane Doe")
        all_users = User.get_all_users()
        assert "John Doe" in all_users
        assert "Jane Doe" in all_users

    def test_find_user_by_id(self):
        user = User("John Doe")
        user_name = User.find_user_by_id(user.id)
        assert user_name == "User's name is: John Doe"

    def test_create_user(self):
        user = User.create_user("John Doe")
        assert user.name == "John Doe"

    def test_repr_method(self):
        user = User("John Doe")
        expected_repr = f"Your username is: John Doe while your password/id is: {user.id}."
        assert repr(user) == expected_repr