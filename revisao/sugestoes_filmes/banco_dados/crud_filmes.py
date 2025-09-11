from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
from kivy.app import App

import sqlite3

# Conexão global com o banco
con = sqlite3.connect('filmes.db')
cur = con.cursor()

def criar_tabela():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS filmes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            genero TEXT,
            ano INTEGER
        )
    """)
    con.commit()

class FilmesItem(BoxLayout):
    def __init__(self, filme, manager, **kwargs):
        super().__init__(**kwargs)
        self.manager = manager  # Recebe a referência do manager
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = 50
        self.filme_id = filme[0]
        
        # Labels com informações do filme
        lbl_id = Label(text=str(filme[0]), size_hint_x=0.1)
        lbl_titulo = Label(text=filme[1], size_hint_x=0.4)
        lbl_genero = Label(text=filme[2], size_hint_x=0.2)
        lbl_ano = Label(text=str(filme[3]), size_hint_x=0.1)
        
        # Botões de ação
        btn_editar = Button(text='Editar', size_hint_x=0.1)
        btn_editar.bind(on_press=self.editar_filme)
        
        btn_deletar = Button(text='Deletar', size_hint_x=0.1)
        btn_deletar.bind(on_press=self.deletar_filme)
        
        self.add_widget(lbl_id)
        self.add_widget(lbl_titulo)
        self.add_widget(lbl_genero)
        self.add_widget(lbl_ano)
        self.add_widget(btn_editar)
        self.add_widget(btn_deletar)
    
    def editar_filme(self, instance):
        # Buscar dados do filme
        cur.execute("SELECT * FROM filmes WHERE id=?", (self.filme_id,))
        filme = cur.fetchone()
        
        if filme:
            tela_editar = self.manager.get_screen('editar')
            tela_editar.carregar_dados(filme[0], filme[1], filme[2], filme[3])
            self.manager.current = 'editar'
    
    def deletar_filme(self, instance):
        cur.execute("DELETE FROM filmes WHERE id=?", (self.filme_id,))
        con.commit()
        # Atualizar lista
        tela_lista = self.manager.get_screen('listagem')
        tela_lista.listar_filmes()

class TelaCadastro(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        self.titulo_input = TextInput(hint_text='Título do Filme', size_hint=(1, 0.1))
        self.genero_input = Spinner(
            text='Escolha o gênero', 
            values=['Comédia', 'Ação', 'Animação', 'Drama', 'Terror'],
            size_hint=(1, 0.1)
        )
        self.ano_input = TextInput(hint_text='Ano de Lançamento', size_hint=(1, 0.1), input_filter='int')
        
        btn_salvar = Button(text="Salvar no Banco", size_hint=(1, 0.1))
        btn_salvar.bind(on_press=self.salvar_no_banco)
        
        btn_listar = Button(text="Listar Filmes", size_hint=(1, 0.1))
        btn_listar.bind(on_press=self.ir_para_lista)
        
        layout.add_widget(Label(text="Cadastro de Filmes", size_hint=(1, 0.1), font_size=20))
        layout.add_widget(self.titulo_input)
        layout.add_widget(self.genero_input)
        layout.add_widget(self.ano_input)
        layout.add_widget(btn_salvar)
        layout.add_widget(btn_listar)
        
        self.add_widget(layout)
        
    def salvar_no_banco(self, instance):
        titulo = self.titulo_input.text.strip()
        genero = self.genero_input.text
        ano = self.ano_input.text.strip()
        
        if titulo and genero != 'Escolha o gênero' and ano:
            try:
                ano_int = int(ano)
                cur.execute("INSERT INTO filmes (titulo, genero, ano) VALUES (?, ?, ?)", 
                           (titulo, genero, ano_int))
                con.commit()
                
                # Limpar campos
                self.titulo_input.text = ''
                self.genero_input.text = 'Escolha o gênero'
                self.ano_input.text = ''
                
                print("Filme salvo com sucesso!")
            except ValueError:
                print("Erro: Ano deve ser um número")
        else:
            print("Preencha todos os campos!")
    
    def ir_para_lista(self, instance):
        self.manager.current = 'listagem'
        # Atualizar lista ao mudar de tela
        tela_lista = self.manager.get_screen('listagem')
        tela_lista.listar_filmes()

class TelaListagem(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # ScrollView para a lista
        scroll = ScrollView()
        
        self.grid = BoxLayout(orientation='vertical', size_hint_y=None, spacing=10)
        self.grid.bind(minimum_height=self.grid.setter('height'))
        scroll.add_widget(self.grid)
        
        btn_novo = Button(text="Novo Filme", size_hint=(1, 0.1))
        btn_novo.bind(on_press=self.ir_para_cadastro)
        
        self.layout.add_widget(Label(text="Lista de Filmes", size_hint=(1, 0.1), font_size=20))
        self.layout.add_widget(scroll)
        self.layout.add_widget(btn_novo)
        
        self.add_widget(self.layout)
        
    def on_pre_enter(self, *args):
        self.listar_filmes()
        
    def listar_filmes(self):
        self.grid.clear_widgets()
        cur.execute("SELECT * FROM filmes ORDER BY titulo")
        filmes = cur.fetchall()
        
        if not filmes:
            self.grid.add_widget(Label(text="Nenhum filme cadastrado"))
        else:
            for filme in filmes:
                # Passa a referência do manager para o FilmesItem
                item = FilmesItem(filme, self.manager)
                self.grid.add_widget(item)
    
    def ir_para_cadastro(self, instance):
        self.manager.current = 'cadastro'

class TelaEditar(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        self.filme_id = None
        
        self.titulo_input = TextInput(hint_text='Título do Filme', size_hint=(1, 0.1))
        self.genero_input = Spinner(
            text='Escolha o gênero', 
            values=['Comédia', 'Ação', 'Animação', 'Drama', 'Terror'],
            size_hint=(1, 0.1)
        )
        self.ano_input = TextInput(hint_text='Ano de Lançamento', size_hint=(1, 0.1), input_filter='int')
        
        btn_salvar = Button(text="Salvar Alterações", size_hint=(1, 0.1))
        btn_salvar.bind(on_press=self.salvar_alteracoes)
        
        btn_voltar = Button(text="Voltar para Lista", size_hint=(1, 0.1))
        btn_voltar.bind(on_press=self.voltar_para_lista)
        
        layout.add_widget(Label(text="Editar Filme", size_hint=(1, 0.1), font_size=20))
        layout.add_widget(self.titulo_input)
        layout.add_widget(self.genero_input)
        layout.add_widget(self.ano_input)
        layout.add_widget(btn_salvar)
        layout.add_widget(btn_voltar)
        
        self.add_widget(layout)
        
    def carregar_dados(self, filme_id, titulo, genero, ano):
        self.filme_id = filme_id
        self.titulo_input.text = titulo
        self.genero_input.text = genero
        self.ano_input.text = str(ano)
        
    def salvar_alteracoes(self, instance):
        titulo = self.titulo_input.text.strip()
        genero = self.genero_input.text
        ano = self.ano_input.text.strip()
        
        if titulo and genero != 'Escolha o gênero' and ano and self.filme_id:
            try:
                ano_int = int(ano)
                cur.execute("UPDATE filmes SET titulo=?, genero=?, ano=? WHERE id=?", 
                           (titulo, genero, ano_int, self.filme_id))
                con.commit()
                self.voltar_para_lista(None)
            except ValueError:
                print("Erro: Ano deve ser um número")
        else:
            print("Preencha todos os campos!")
            
    def voltar_para_lista(self, instance):
        self.manager.current = 'listagem'
        # Atualizar lista
        tela_lista = self.manager.get_screen('listagem')
        tela_lista.listar_filmes()

class GerenciadorTelas(ScreenManager):
    pass

class CrudFilmesApp(App):
    def build(self):
        # criar tabela se não existir
        criar_tabela()
        
        gerenciador = GerenciadorTelas()
        
        # Adicionar telas
        gerenciador.add_widget(TelaCadastro(name='cadastro'))
        gerenciador.add_widget(TelaListagem(name='listagem'))
        gerenciador.add_widget(TelaEditar(name='editar'))
        
        return gerenciador

if __name__ == "__main__":
    CrudFilmesApp().run()
