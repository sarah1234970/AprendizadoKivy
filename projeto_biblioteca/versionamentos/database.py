import sqlite3
from datetime import datetime

class Database:
    def __init__(self, db_name='library.db'):
        self.db_name = db_name
        self.connection = None
    
    def connect(self):
        """Establish connection to the database"""
        self.connection = sqlite3.connect(self.db_name)
        return self.connection
    
    def disconnect(self):
        """Close database connection"""
        if self.connection:
            self.connection.close()
    
    def create_tables(self):
        """Create all necessary tables"""
        conn = self.connect()
        cursor = conn.cursor()
        
        # Create users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                senha TEXT NOT NULL
            )
        ''')
        
        # Create books table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS livros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL,
                status TEXT DEFAULT 'disponivel'
            )
        ''')
        
        # Create loans table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS emprestimos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario_id INTEGER,
                livro_id INTEGER,
                data_emprestimo TEXT,
                data_devolucao TEXT,
                FOREIGN KEY (usuario_id) REFERENCES usuarios (id),
                FOREIGN KEY (livro_id) REFERENCES livros (id)
            )
        ''')
        
        conn.commit()
        self.disconnect()
    
    def add_user(self, nome, email, senha):
        """Add a new user to the database"""
        conn = self.connect()
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                INSERT INTO usuarios (nome, email, senha)
                VALUES (?, ?, ?)
            ''', (nome, email, senha))
            
            conn.commit()
            user_id = cursor.lastrowid
            self.disconnect()
            return user_id
        except sqlite3.IntegrityError:
            self.disconnect()
            return None
    
    def get_user_by_email(self, email):
        """Get user by email"""
        conn = self.connect()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM usuarios WHERE email = ?
        ''', (email,))
        
        user = cursor.fetchone()
        self.disconnect()
        return user
    
    def add_book(self, titulo, autor):
        """Add a new book to the database"""
        conn = self.connect()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO livros (titulo, autor)
            VALUES (?, ?)
        ''', (titulo, autor))
        
        conn.commit()
        book_id = cursor.lastrowid
        self.disconnect()
        return book_id
    
    def get_all_books(self):
        """Get all books from the database"""
        conn = self.connect()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM livros
        ''')
        
        books = cursor.fetchall()
        self.disconnect()
        return books
    
    def get_available_books(self):
        """Get all available books from the database"""
        conn = self.connect()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM livros WHERE status = 'disponivel'
        ''')
        
        books = cursor.fetchall()
        self.disconnect()
        return books
    
    def borrow_book(self, usuario_id, livro_id):
        """Create a new loan record"""
        conn = self.connect()
        cursor = conn.cursor()
        
        # Update book status
        cursor.execute('''
            UPDATE livros SET status = 'emprestado' WHERE id = ?
        ''', (livro_id,))
        
        # Create loan record
        cursor.execute('''
            INSERT INTO emprestimos (usuario_id, livro_id, data_emprestimo)
            VALUES (?, ?, ?)
        ''', (usuario_id, livro_id, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        
        conn.commit()
        self.disconnect()
    
    def return_book(self, livro_id):
        """Return a book and update loan record"""
        conn = self.connect()
        cursor = conn.cursor()
        
        # Update book status
        cursor.execute('''
            UPDATE livros SET status = 'disponivel' WHERE id = ?
        ''', (livro_id,))
        
        # Update loan record with return date
        cursor.execute('''
            UPDATE emprestimos 
            SET data_devolucao = ? 
            WHERE livro_id = ? AND data_devolucao IS NULL
        ''', (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), livro_id))
        
        conn.commit()
        self.disconnect()
    
    def get_user_loans(self, usuario_id):
        """Get all loans for a specific user"""
        conn = self.connect()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT e.id, l.titulo, l.autor, e.data_emprestimo, e.data_devolucao
            FROM emprestimos e
            JOIN livros l ON e.livro_id = l.id
            WHERE e.usuario_id = ?
            ORDER BY e.data_emprestimo DESC
        ''', (usuario_id,))
        
        loans = cursor.fetchall()
        self.disconnect()
        return loans
