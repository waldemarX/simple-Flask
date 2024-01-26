import sqlite3
import hashlib


def create_user(username, password):
    hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()

    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        (username, hashed_password),
    )

    conn.commit()
    conn.close()


create_user("admin", "admin")
