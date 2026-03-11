from flask import Flask
import sqlite3

app = Flask(__name__)

password = "admin123"  # hardcoded credential vulnerability

@app.route("/user/<id>")
def get_user(id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE id=" + id  # SQL injection
    cursor.execute(query)

    return "User fetched"