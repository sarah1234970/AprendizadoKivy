"""
Sistema de Biblioteca – Versão v1.0.0
Tipo de manutenção: Versão inicial
Alterações:
- Implementação básica do sistema de biblioteca
- Tela de login e cadastro de usuário
- Tela de lista de livros disponíveis
- Função simples de empréstimo e devolução (CRUD)
- Banco de dados SQLite com tabelas de usuarios, livros e emprestimos
"""

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from database import Database
from screens import LoginScreen, RegisterScreen, BookListScreen, ProfileScreen

class LibraryApp(App):
    def build(self):
        # Initialize database
        self.db = Database()
        self.db.create_tables()
        
        # Create screen manager
        sm = ScreenManager()
        
        # Add screens
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(BookListScreen(name='book_list'))
        sm.add_widget(ProfileScreen(name='profile'))
        
        return sm

if __name__ == '__main__':
    LibraryApp().run()
