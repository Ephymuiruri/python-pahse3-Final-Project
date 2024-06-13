from models.database_config import CONN,CURSOR
def create_tables():
    CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT NOT NULL,
            Amount DECIMAL(19,4) NOT NULL,
            date_created DATE NOT NULL
        );
    """)
    CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS deposits (
            deposit_id INTEGER PRIMARY KEY AUTOINCREMENT,
            deposit_amount INTEGER NOT NULL,
            deposit_date DATE NOT NULL,
            user_id INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        );
    """)
    CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS payments (
            payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            payment_amount INTEGER NOT NULL,
            payment_date DATE NOT NULL,
            user_id INTEGER NOT NULL,
            recipient_id INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(user_id),
            FOREIGN KEY (recipient_id) REFERENCES users(user_id)
        );
    """)
    CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS loans (
            loan_id INTEGER PRIMARY KEY AUTOINCREMENT,
            loan_amount DECIMAL(19,4) NOT NULL,
            loan_date DATE NOT NULL,
            user_id INTEGER NOT NULL,
            date_due DATE NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        );
    """)
    CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS managers (
            manager_id INTEGER PRIMARY KEY AUTOINCREMENT,
            manager_name TEXT NOT NULL,
            date_created DATE NOT NULL
        );
    """)
    CONN.commit()

def drop_tables():
    CURSOR.execute("""
        DROP TABLE IF EXISTS payments;
    """)
    CURSOR.execute("""
        DROP TABLE IF EXISTS deposits;
    """)
    CURSOR.execute("""
        DROP TABLE IF EXISTS users;
    """)
    CURSOR.execute("""
        DROP TABLE IF EXISTS loans;
    """)
    CURSOR.execute("""
        DROP TABLE IF EXISTS managers;
    """)
    CONN.commit()
