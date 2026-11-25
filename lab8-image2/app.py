#!/usr/bin/python
"""
Lab 8 - Image 2
Flask API that runs on port 3000 and exposes GET /get_users, which returns a
list of all the user names stored in the SQLite database (database.db).
"""
import sqlite3

from flask import Flask, jsonify
from flask_cors import CORS


def connect_to_db():
    """Open the SQLite file, creating database.db if it does not exist yet."""
    conn = sqlite3.connect("database.db")
    return conn


def create_db_table():
    """Create the users table on first run (ignored if it already exists)."""
    conn = None
    try:
        conn = connect_to_db()
        conn.execute(
            """
            CREATE TABLE users (
                user_id INTEGER PRIMARY KEY NOT NULL,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL,
                address TEXT NOT NULL,
                country TEXT NOT NULL
            );
            """
        )
        conn.commit()
        print("User table created successfully")
    except sqlite3.Error as error:
        print(f"User table creation failed - Maybe table already exists ({error})")
    finally:
        if conn:
            conn.close()


def get_user_names():
    """Return a list containing only the names of all users in the database."""
    names = []
    conn = None
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("SELECT name FROM users")
        rows = cur.fetchall()
        names = [row[0] for row in rows]
    except sqlite3.Error:
        names = []
    finally:
        if conn:
            conn.close()
    return names


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/get_users", methods=["GET"])
def api_get_users():
    """GET /get_users -> JSON list of all user names, e.g. ["John Doe"]"""
    return jsonify(get_user_names())


if __name__ == "__main__":
    create_db_table()
    # host="0.0.0.0" is REQUIRED inside Docker so the -p 3000:3000 mapping
    # can reach the app from outside the container.
    app.run(host="0.0.0.0", port=3000)
