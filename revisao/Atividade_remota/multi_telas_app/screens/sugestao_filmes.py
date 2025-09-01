# language: python
import random
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen

# ...existing code...
filmes = {
    "Comédia": [
        {"titulo": "As Branquelas", "ano": 2004, "duração": "1h 49min"},
        {"titulo": "Meninas Malvadas", "ano": 2004, "duração": "1h 37min"},
    ],
    "Ação": [
        {"titulo": "Velozes e Furiosos", "ano": 2001, "duração": "1h 46min"},
        {"titulo": "Vingadores: Ultimato", "ano": 2019, "duração": "3h 02min"},
    ],
    "Animação": [
        {"titulo": "Procurando Nemo", "ano": 2003, "duração": "1h 40min"},
        {"titulo": "Shrek", "ano": 2001, "duração": "1h 30min"},
    ]
}

class SugestaoFilmesScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.username = None
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.welcome_label = Label(text="Olá!", font_size=20, size_hint=(1, 0.15))
        self.spinner = Spinner(text='Escolha o gênero', values=list(filmes.keys()), size_hint=(1, 0.15))
        self.suggest_btn = Button(text='Sugerir Filme', size_hint=(1, 0.15))
        self.result_label = Label(text='', font_size=18)

        self.suggest_btn.bind(on_press=self.sugerir_filme)

        self.layout.add_widget(self.welcome_label)
        self.layout.add_widget(self.spinner)
        self.layout.add_widget(self.suggest_btn)
        self.layout.add_widget(self.result_label)
        self.add_widget(self.layout)

    def on_pre_enter(self, *args):
        # atualiza o texto de boas-vindas com o nome recebido da outra tela
        if getattr(self, 'username', None):
            self.welcome_label.text = f"Olá, {self.username}!"
        else:
            self.welcome_label.text = "Olá!"

    def sugerir_filme(self, instance):
        genero = self.spinner.text
        if genero not in filmes:
            self.result_label.text = "Selecione um gênero válido."
            return
        escolha = random.choice(filmes[genero])
        self.result_label.text = f"{escolha['titulo']} ({escolha['ano']}) - {escolha['duração']}"