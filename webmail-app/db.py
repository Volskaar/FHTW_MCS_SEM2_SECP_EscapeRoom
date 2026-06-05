import os
import sqlite3
from pathlib import Path

DB_PATH = Path(os.environ.get("WEBMAIL_DB_PATH", "/opt/webmail/data/webmail.sqlite")).resolve()

def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection