import sqlite3
from datetime import datetime

DB_PATH = "database/logs.db"

def init_db():
    """Crea la tabla de logs si no existe."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS security_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            level TEXT,
            message TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_log(level, message):
    """Guarda un nuevo evento en la base de datos."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('''
        INSERT INTO security_logs (timestamp, level, message)
        VALUES (?, ?, ?)
    ''', (now, level, message))
    conn.commit()
    conn.close()