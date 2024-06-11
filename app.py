from lib.Database.setup import (create_tables, drop_tables)
from lib.models.User import User
def main():
    drop_tables()
    create_tables()
    User1= User.create_user("Ephy")

if __name__ == '__main__':
    main()