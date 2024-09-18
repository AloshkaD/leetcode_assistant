import sqlite3

def init_db():
    conn = sqlite3.connect('qa.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS qa (
            id INTEGER PRIMARY KEY,
            question TEXT,
            answer TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_qa_pair(question, answer):
    conn = sqlite3.connect('qa.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO qa (question, answer) VALUES (?, ?)
    ''', (question, answer))
    conn.commit()
    conn.close()
