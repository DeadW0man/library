from flask import Flask, g, request, jsonify
from os import getenv
from sqlite3 import connect
from db.database import prepare_tables

solaris_app = Flask('solaris')

def run_app() -> None:
    # Просто запускаем наше приложение
    solaris_app.run(
        host=getenv('SOLARIS_HOST', '0.0.0.0'),
        port=int(getenv('SOLARIS_PORT', '5000')),
        debug=True
    )

if __name__ == '__main__':
    with solaris_app.app_context():
        prepare_tables()
    run_app()
