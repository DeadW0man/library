from flask import Flask, g, request, jsonify
from os import getenv
from sqlite3 import connect

db_path = getenv('SOLARIS_SQLITE_PATH', 'dev.db')

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect(db_path)
    return db

def prepare_tables() -> None:
    # Все запросы к базе делаются через курсор
    cursor = get_db().cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(128) NOT NULL,
            email VARCHAR(128) NOT NULL,
            password VARCHAR(128) NOT NULL
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sessions (
            user_id INTEGER NOT NULL,
            session_id INTEGER PRIMARY KEY AUTOINCREMENT,
            FOREIGN KEY (user_id) REFERENCES users (id)
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS shares (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER NOT NULL,
            giver_id INTEGER NOT NULL,
            taker_id INTEGER NOT NULL,
            final_date VARCHAR(32),
            FOREIGN KEY (book_id) REFERENCES books (id),
            FOREIGN KEY (giver_id) REFERENCES users (id),
            FOREIGN KEY (taker_id) REFERENCES users (id)
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(128) NOT NULL,
            author VARCHAR(128) NOT NULL,
            release_year INTEGER NOT NULL,
            owner_id INTEGER NOT NULL,
            FOREIGN KEY (owner_id) REFERENCES users (id)
        );
    """)
