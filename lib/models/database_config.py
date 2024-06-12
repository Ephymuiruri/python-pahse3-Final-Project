# lib/__init__.py
import sqlite3

CONN = sqlite3.connect('lib/Database/company.db')
CURSOR = CONN.cursor()
