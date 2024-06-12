from models.database_config import CONN, CURSOR
from models.Deposit import Deposit
from Database.setup import (create_tables, drop_tables)
import pytest
import datetime
class test_Deposit:
    @pytest.fixture(autouse=True)
    def create_table(self):
        create_tables()
        drop_tables()
    def test_create_deposit(self):
        Deposit1 = Deposit.create_deposit(1000,1)
        assert Deposit1.amount == 1000
        assert Deposit1.user_id == 1
        assert Deposit1.date == datetime.datetime.now()
