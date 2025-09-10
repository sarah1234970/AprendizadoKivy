from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner

import sqlite3  
import random

def conexao_banco():
    conn = sqlite3.connect('filmes.db')  
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS filmes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            genero TEXT,
            ano INTEGER
        )
    """)
    conn.commit()
    return conn 

        
class TelaCadastro(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        self.titulo_input = TextInput(hint_text='Título do Filme', size_hint=(1, 0.1))
        self.genero_input = Spinner(text='Escolha o gênero', values=['Comédia', 'Ação', 'Animação'], size_hint=(1, 0.1))
        self.ano_input = TextInput(hint_text='Seu Nome', size_hint=(1, 0.1))
        self.cadastrar_btn = Button(text='Cadastrar Filme', size_hint=(1, 0.1))
        
        btn_salvar = Button(text="Salvar no Banco", size_hint=(1, 0.1))
        btn_salvar.bind(on_press=self.salvar_no_banco)
        
        btn_listar = Button(text="Listar Filmes", size_hint=(1, 0.1))
        btn_listar.bind(on_press=self.listar_filmes)
        
        layout.add_widget(self.titulo_input)
        layout.add_widget(self.genero_input)
        layout.add_widget(self.ano_input)   
        layout.add_widget(self.cadastrar_btn)
        layout.add_widget(btn_salvar)
        layout.add_widget(btn_listar)
        self.layout.add_widget(layout)
        
    def adicionar_fime(self, instance):
        titulo = self.titulo_input.text
        genero = self.genero_input.text
        ano = self.ano_input.text
        
        if titulo and genero and ano:
            con = conexao_banco()
            cur = con.cursor()
            cur.execute("INSERT INTO filmes (titulo, genero, ano) VALUES (?, ?, ?)", (titulo, genero, ano))
            self.manager.get_screen('sugestao').adicionar_filme(titulo, genero, ano)
            self.titulo_input.text = ''
            self.genero_input.text = 'Escolha o gênero'
            self.ano_input.text = ''
            
class TelaListagem(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        self.grid = BoxLayout(orientation='vertical', size_hint_y=None)
        self.grid.bind(minimum_height=self.grid.setter('height'))
        self.layout.add_widget(self.grid)
        
        btn_new = Button(text="Novo Filme", size_hint=(1, 0.1))
        btn_new.bind(on_press=self.novo_filme)
        self.layout.add_widget(btn_new)
        
        self.label = Label(text='Lista de Filmes', font_size=20)
        self.layout.add_widget(self.label)
        self.add_widget(self.layout)
        
    def on_pre_enter(self, *args):
        self.listar_filmes()
        
    def listar_filmes(self):
        self.grid.clear_widgets()
        cur.execute("SELECT * FROM filmes")
        filmes = cur.fetchall()
        for filmes in filmes:
            item = FilmesItem(filmes)
            self.grid.add_widget(item)
    
    def delet_fime(self, filme_id):
        cur.execute("DELETE FROM filmes WHERE id=?", (filme_id,))
        con.commit()
        self.listar_filmes()

    def editar_fime(self, filme_id, titulo, genero, ano):
        tela_editar = self.manager.get_screen('editar')
        tela_editar.carregar_dados(filme_id, titulo, genero, ano)
        self.manager.current = 'editar'        

class TelaEditar(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.filme_id_input = TextInput(hint_text='ID do Filme', size_hint=(1, 0.1))
        
        self.id_label = Label(text='ID do Filme', size_hint=(1, 0.1))
        self.titulo_input = TextInput(hint_text='Título do Filme', size_hint=(1, 0.1))
        self.genero_input = Spinner(text='Escolha o gênero', values=['Comédia', 'Ação', 'Animação'], size_hint=(1, 0.1))
        self.ano_input = TextInput(hint_text='Seu Nome', size_hint=(1, 0.1))
        
        btn_salvar = Button(text="Salvar Alterações", size_hint=(1, 0.1))
        btn_salvar.bind(on_press=self.salvar_alteracoes)
        
        btn_retornar = Button(text="Voltar para Lista", size_hint=(1, 0.1))
        btn_retornar.bind(on_press=self.voltar_para_lista)
        
        layout.add_widget(self.id_label)
        layout.add_widget(self.filme_id_input)
        layout.add_widget(self.titulo_input)
        layout.add_widget(self.genero_input)
        layout.add_widget(self.ano_input)
        layout.add_widget(btn_salvar)
        layout.add_widget(btn_retornar)
        self.add_widget(layout)
        
    def carregar_dados(self, filme_id, titulo, genero, ano):
        self.filme_id_input.text = str(filme_id)
        self.titulo_input.text = titulo
        self.genero_input.text = genero
        self.ano_input.text = str (ano)
        
    def salvar_alteracoes(self, instance):
        filmes_id = self.filme_id_input.text
        titulo = self.titulo_input.text
        genero = self.genero_input.text
        ano = self.ano_input.text
        
        if filmes_id and titulo and genero and ano:
            cur.execute("UPDATE filmes SET titulo=?, genero=?, ano=? WHERE id=?", (titulo, genero, ano, filmes_id))
            con.commit()
            self.manager.get_screen('listagem').listar_filmes()
            self.manager.current = 'listagem'
            
    def voltar_para_lista(self, instance):
        self.manager.current = 'listagem'
class FilmesItem(BoxLayout):
    def __init__(self, filmes, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = 40

        ibl = Label(text=str(filmes[0]), size_hint_x=0.1)
        btn_editar = Button(text='Editar', size_hint_x=0.2)
        btn_deletar = Button(text='Deletar', size_hint_x=0.2)
        btn_excluir = Button(text='Excluir', size_hint_x=0.2)

        lbl_titulo = Label(text=filmes[1], size_hint_x=0.3)
        
        
