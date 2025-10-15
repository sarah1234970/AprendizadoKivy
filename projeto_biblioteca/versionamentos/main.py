"""
Sistema de Biblioteca – Versão v1.1.0
Tipo de manutenção: Corretiva
Alterações:
- Corrigido erro de login não reconhecido
- Corrigido problema ao cadastrar usuário
- Aprimorado tratamento de erros no processo de autenticação
- Melhorada validação de dados no cadastro
"""

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from database import Database
from screens import *

class LibraryApp(App):
    def build(self):
        # Initialize database
        self.db = Database()
        self.db.create_tables()
        self.add_sample_data()
        
        # Create screen manager
        sm = ScreenManager()
        
        # Add screens
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(BookListScreen(name='book_list'))
        sm.add_widget(ProfileScreen(name='profile'))
        
        return sm
    
    def add_sample_data(self):
        """Add sample books to the database for testing"""
        # Check if we already have books to avoid duplicates
        books = self.db.get_all_books()
        if len(books) == 0:
            # Add sample books
            self.db.add_book("Dom Quixote", "Miguel de Cervantes")
            self.db.add_book("1984", "George Orwell")
            self.db.add_book("O Senhor dos Anéis", "J.R.R. Tolkien")
            self.db.add_book("O Pequeno Príncipe", "Antoine de Saint-Exupéry")
            self.db.add_book("Harry Potter e a Pedra Filosofal", "J.K. Rowling")
            self.db.add_book("O Código Da Vinci", "Dan Brown")
            self.db.add_book("Cem Anos de Solidão", "Gabriel García Márquez")
            self.db.add_book("Orgulho e Preconceito", "Jane Austen")

if __name__ == '__main__':
    LibraryApp().run()
