import sqlite3

DB_NAME = "tasks.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_task(title: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title) VALUES(?)", (title,))
    conn.commit()
    conn.close()

def get_tasks():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def del_tasks(id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks where id = ?", (id,))
    conn.commit()
    conn.close()