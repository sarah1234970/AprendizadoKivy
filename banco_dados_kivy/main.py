import sqlite3

con = sqlite3.connect('banco_dados.db')
cur = con.cursor()
cur.execute("""
        CREATE TABLE IF NOT EXISTS usuarios 
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        senha TEXT,
        idade INTEGER NOT NULL
            ) 
        """)
con.commit()
