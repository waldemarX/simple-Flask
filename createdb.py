import sqlite3


conn = sqlite3.connect("database.db")


c = conn.cursor()


c.execute(
    """CREATE TABLE IF NOT EXISTS content (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             idblock TEXT,
             short_title TEXT,
             img TEXT,
             altimg TEXT,
             title TEXT,
             contenttext TEXT,
             author TEXT,
             timestampdata DATETIME)"""
)

c.execute(
    """CREATE TABLE IF NOT EXISTS users (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             username TEXT,
             password TEXT)"""
)

conn.close()
