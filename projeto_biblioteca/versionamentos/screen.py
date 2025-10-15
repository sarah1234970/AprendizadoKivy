"""
Sistema de Biblioteca – Versão v1.1.0
Tipo de manutenção: Corretiva
Alterações:
- Corrigido erro de login não reconhecido
- Corrigido problema ao cadastrar usuário
- Aprimorado tratamento de erros no processo de autenticação
- Melhorada validação de dados no cadastro
"""

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.app import App
import re

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        # Title
        title = Label(text='Sistema de Biblioteca', font_size=24, size_hint_y=None, height=50)
        self.layout.add_widget(title)
        
        # Email input
        self.email_input = TextInput(hint_text='Email', multiline=False, size_hint_y=None, height=40)
        self.layout.add_widget(self.email_input)
        
        # Password input
        self.password_input = TextInput(hint_text='Senha', password=True, multiline=False, size_hint_y=None, height=40)
        self.layout.add_widget(self.password_input)
        
        # Login button
        login_btn = Button(text='Login', size_hint_y=None, height=50)
        login_btn.bind(on_press=self.login)
        self.layout.add_widget(login_btn)
        
        # Register button
        register_btn = Button(text='Criar Conta', size_hint_y=None, height=50)
        register_btn.bind(on_press=self.go_to_register)
        self.layout.add_widget(register_btn)
        
        # Error message label
        self.error_label = Label(text='', color=(1, 0, 0, 1))
        self.layout.add_widget(self.error_label)
        
        self.add_widget(self.layout)
    
    def validate_email(self, email):
        """Validate email format"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def login(self, instance):
        """Handle login process"""
        email = self.email_input.text.strip()
        password = self.password_input.text.strip()
        
        # Validate inputs
        if not email or not password:
            self.error_label.text = 'Por favor, preencha todos os campos.'
            return
        
        # Validate email format
        if not self.validate_email(email):
            self.error_label.text = 'Por favor, insira um email válido.'
            return
        
        app = App.get_running_app()
        user = app.db.get_user_by_email(email)
        
        if user and user[3] == password:  # user[3] is the password field
            app.current_user = user
            self.manager.current = 'book_list'
            self.error_label.text = ''
            # Clear input fields
            self.email_input.text = ''
            self.password_input.text = ''
        else:
            self.error_label.text = 'Email ou senha incorretos.'
    
    def go_to_register(self, instance):
        """Navigate to register screen"""
        self.manager.current = 'register'
        self.error_label.text = ''

class RegisterScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        # Title
        title = Label(text='Cadastro de Usuário', font_size=24, size_hint_y=None, height=50)
        self.layout.add_widget(title)
        
        # Name input
        self.name_input = TextInput(hint_text='Nome', multiline=False, size_hint_y=None, height=40)
        self.layout.add_widget(self.name_input)
        
        # Email input
        self.email_input = TextInput(hint_text='Email', multiline=False, size_hint_y=None, height=40)
        self.layout.add_widget(self.email_input)
        
        # Password input
        self.password_input = TextInput(hint_text='Senha', password=True, multiline=False, size_hint_y=None, height=40)
        self.layout.add_widget(self.password_input)
        
        # Register button
        register_btn = Button(text='Cadastrar', size_hint_y=None, height=50)
        register_btn.bind(on_press=self.register)
        self.layout.add_widget(register_btn)
        
        # Back to login button
        back_btn = Button(text='Voltar ao Login', size_hint_y=None, height=50)
        back_btn.bind(on_press=self.go_to_login)
        self.layout.add_widget(back_btn)
        
        # Error message label
        self.error_label = Label(text='', color=(1, 0, 0, 1))
        self.layout.add_widget(self.error_label)
        
        self.add_widget(self.layout)
    
    def validate_email(self, email):
        """Validate email format"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def validate_password(self, password):
        """Validate password strength"""
        # At least 6 characters
        return len(password) >= 6
    
    def register(self, instance):
        """Handle user registration"""
        name = self.name_input.text.strip()
        email = self.email_input.text.strip()
        password = self.password_input.text.strip()
        
        # Validate inputs
        if not name or not email or not password:
            self.error_label.text = 'Por favor, preencha todos os campos.'
            return
        
        # Validate email format
        if not self.validate_email(email):
            self.error_label.text = 'Por favor, insira um email válido.'
            return
        
        # Validate password strength
        if not self.validate_password(password):
            self.error_label.text = 'A senha deve ter pelo menos 6 caracteres.'
            return
        
        app = App.get_running_app()
        user_id = app.db.add_user(name, email, password)
        
        if user_id:
            self.error_label.text = 'Usuário cadastrado com sucesso!'
            self.error_label.color = (0, 1, 0, 1)  # Green color for success
            # Clear input fields
            self.name_input.text = ''
            self.email_input.text = ''
            self.password_input.text = ''
        else:
            self.error_label.text = 'Email já cadastrado. Tente outro.'
            self.error_label.color = (1, 0, 0, 1)  # Red color for error
    
    def go_to_login(self, instance):
        """Navigate to login screen"""
        self.manager.current = 'login'
        self.error_label.text = ''
        self.error_label.color = (1, 0, 0, 1)  # Reset to red color

class BookListScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Top bar with title and profile button
        top_bar = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
        title = Label(text='Livros Disponíveis', font_size=20)
        profile_btn = Button(text='Perfil', size_hint_x=None, width=100)
        profile_btn.bind(on_press=self.go_to_profile)
        top_bar.add_widget(title)
        top_bar.add_widget(profile_btn)
        self.layout.add_widget(top_bar)
        
        # Scrollable book list
        self.scroll = ScrollView()
        self.book_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.book_layout.bind(minimum_height=self.book_layout.setter('height'))
        self.scroll.add_widget(self.book_layout)
        self.layout.add_widget(self.scroll)
        
        # Refresh button
        refresh_btn = Button(text='Atualizar', size_hint_y=None, height=50)
        refresh_btn.bind(on_press=self.load_books)
        self.layout.add_widget(refresh_btn)
        
        self.add_widget(self.layout)
        
        # Load books when screen is shown
        self.bind(on_enter=self.load_books)
    
    def load_books(self, instance):
        """Load all available books"""
        # Clear existing widgets
        self.book_layout.clear_widgets()
        
        app = App.get_running_app()
        books = app.db.get_available_books()
        
        if not books:
            no_books_label = Label(text='Nenhum livro disponível no momento.')
            self.book_layout.add_widget(no_books_label)
            return
        
        # Add books to layout
        for book in books:
            book_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=60)
            book_info = Label(text=f'{book[1]} - {book[2]}', halign='left', valign='middle')
            borrow_btn = Button(text='Emprestar', size_hint_x=None, width=100)
            borrow_btn.bind(on_press=lambda x, b=book: self.borrow_book(b))
            
            book_box.add_widget(book_info)
            book_box.add_widget(borrow_btn)
            self.book_layout.add_widget(book_box)
    
    def borrow_book(self, book):
        """Borrow a book"""
        app = App.get_running_app()
        app.db.borrow_book(app.current_user[0], book[0])  # user_id, book_id
        
        # Show confirmation
        popup = Popup(title='Sucesso',
                      content=Label(text=f'Livro "{book[1]}" emprestado com sucesso!'),
                      size_hint=(0.8, 0.4))
        popup.open()
        
        # Reload books
        self.load_books(None)
    
    def go_to_profile(self, instance):
        """Navigate to profile screen"""
        self.manager.current = 'profile'

class ProfileScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Top bar with title and back button
        top_bar = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
        title = Label(text='Meu Perfil', font_size=20)
        back_btn = Button(text='Voltar', size_hint_x=None, width=100)
        back_btn.bind(on_press=self.go_back)
        top_bar.add_widget(title)
        top_bar.add_widget(back_btn)
        self.layout.add_widget(top_bar)
        
        # User info section
        self.user_info = BoxLayout(orientation='vertical', size_hint_y=None, height=150)
        self.user_name = Label(text='', font_size=18)
        self.user_email = Label(text='', font_size=16)
        self.user_info.add_widget(self.user_name)
        self.user_info.add_widget(self.user_email)
        self.layout.add_widget(self.user_info)
        
        # Loans section
        loans_title = Label(text='Meus Empréstimos', font_size=18, size_hint_y=None, height=40)
        self.layout.add_widget(loans_title)
        
        # Scrollable loans list
        self.scroll = ScrollView()
        self.loans_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.loans_layout.bind(minimum_height=self.loans_layout.setter('height'))
        self.scroll.add_widget(self.loans_layout)
        self.layout.add_widget(self.scroll)
        
        # Logout button
        logout_btn = Button(text='Sair', size_hint_y=None, height=50)
        logout_btn.bind(on_press=self.logout)
        self.layout.add_widget(logout_btn)
        
        self.add_widget(self.layout)
        
        # Load profile when screen is shown
        self.bind(on_enter=self.load_profile)
    
    def load_profile(self, instance):
        """Load user profile and loans"""
        app = App.get_running_app()
        user = app.current_user
        
        # Update user info
        self.user_name.text = f'Nome: {user[1]}'
        self.user_email.text = f'Email: {user[2]}'
        
        # Clear existing loans
        self.loans_layout.clear_widgets()
        
        # Load user loans
        loans = app.db.get_user_loans(user[0])
        
        if not loans:
            no_loans_label = Label(text='Você não tem empréstimos ativos.')
            self.loans_layout.add_widget(no_loans_label)
            return
        
        # Add loans to layout
        for loan in loans:
            loan_box = BoxLayout(orientation='vertical', size_hint_y=None, height=80)
            loan_info = Label(text=f'{loan[1]} - {loan[2]}', halign='left')
            loan_dates = Label(text=f'Emprestado em: {loan[3][:10]}', halign='left', font_size=14)
            
            # Return button (only if not returned yet)
            if loan[4] is None:  # Not returned yet
                return_btn = Button(text='Devolver', size_hint_y=None, height=30)
                return_btn.bind(on_press=lambda x, l=loan: self.return_book(l))
                loan_box.add_widget(return_btn)
            
            loan_box.add_widget(loan_info)
            loan_box.add_widget(loan_dates)
            self.loans_layout.add_widget(loan_box)
    
    def return_book(self, loan):
        """Return a borrowed book"""
        app = App.get_running_app()
        app.db.return_book(loan[2])  # loan[2] is livro_id
        
        # Show confirmation
        popup = Popup(title='Sucesso',
                      content=Label(text='Livro devolvido com sucesso!'),
                      size_hint=(0.8, 0.4))
        popup.open()
        
        # Reload profile
        self.load_profile(None)
    
    def go_back(self, instance):
        """Go back to book list"""
        self.manager.current = 'book_list'
    
    def logout(self, instance):
        """Logout and go to login screen"""
        app = App.get_running_app()
        app.current_user = None
        self.manager.current = 'login'
