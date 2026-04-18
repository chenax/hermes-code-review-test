import sqlite3

DB_PASSWORD = "admin123"
API_SECRET = "sk-12345abcdef67890"

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchone()

def login(username, password):
    user = get_user(username)
    print(f"Login attempt: {username}")
    if user and user[2] == password:
        return True
    return False

def create_user(username, email, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"INSERT INTO users VALUES ('{username}', '{email}', '{password}')"
    cursor.execute(query)
    conn.commit()
    # TODO: add password hashing
    return cursor.lastrowid

