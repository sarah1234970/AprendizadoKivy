from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.image import Image
from kivy.core.window import Window

import random

filmes = {
    "Comédia": [
        {"titulo": "As Branquelas", "ano": 2004, "duração": "1h 49min", "img": "imagens/branquelas.jpg"},
        {"titulo": "Todo Mundo em Pânico", "ano": 2000, "duração": "1h 28min", "img": "imagens/panico.jpg"},
        {"titulo": "Meninas Malvadas", "ano": 2004, "duração": "1h 37min", "img": "imagens/meninas.jpg"},
    ],
    "Terror": [
        {"titulo": "Invocação do Mal", "ano": 2013, "duração": "1h 52min", "img": "imagens/invocacao.png"},
        {"titulo": "It: A Coisa", "ano": 2017, "duração": "2h 15min", "img": "imagens/it.jpg"},
        {"titulo": "A Hora do Pesadelo", "ano": 1984, "duração": "1h 31min", "img": "imagens/pesadelo.png"},
    ],
    "Ação": [
        {"titulo": "Velozes e Furiosos", "ano": 2001, "duração": "1h 46min", "img": "imagens/velozes.webp"},
        {"titulo": "Missão Impossível", "ano": 1996, "duração": "1h 50min", "img": "imagens/missao.jpg"},
        {"titulo": "Vingadores: Ultimato", "ano": 2019, "duração": "3h 02min", "img": "imagens/vingadores.jpg"},
    ],
    "Drama": [
        {"titulo": "A Procura da Felicidade", "ano": 2006, "duração": "1h 57min", "img": "imagens/felicidade.jpg"},
        {"titulo": "O Menino do Pijama Listrado", "ano": 2008, "duração": "1h 34min", "img": "imagens/pijama.jpg"},
        {"titulo": "Clube da Luta", "ano": 1999, "duração": "2h 19min", "img": "imagens/luta.jpg"},
    ],
    "Animação": [
        {"titulo": "Procurando Nemo", "ano": 2003, "duração": "1h 40min", "img": "imagens/nemo.jpg"},
        {"titulo": "Divertidamente", "ano": 2015, "duração": "1h 35min", "img": "imagens/divertidamente.webp"},
        {"titulo": "Shrek", "ano": 2001, "duração": "1h 30min", "img": "imagens/shrek.webp"},
    ]
}

class FilmesApp(App):
    def build(self):
        Window.clearcolor = (0.08, 0.08, 0.08, 1)
        layout = BoxLayout(orientation='vertical', padding=30, spacing=18)

        self.nome_input = TextInput(
            hint_text='Digite seu nome',
            multiline=False,
            size_hint=(1, 0.09),
            font_size=22,
            foreground_color=(1, 1, 1, 1),
            background_color=(0.18, 0.18, 0.18, 1),
            cursor_color=(1, 1, 1, 1)
        )

        self.spinner = Spinner(
            text="Selecione o gênero do filme",
            values=["Drama", "Comédia", "Terror", "Ação", "Animação"],
            size_hint=(1, 0.09),
            font_size=20,
            background_color=(0.22, 0.22, 0.22, 1),
            color=(1, 1, 1, 1)
        )

        # BOTÃO SUGERIR - MUDE A COR AQUI ↓
        botao_sugerir = Button(
            text="Sugerir Filme",
            size_hint=(1, 0.09),
            font_size=20,
            background_normal='',
            background_color=(0.3, 0.7, 0.3, 1),  # VERDE MAIS CLARO
            color=(1, 1, 1, 1)
        )
        botao_sugerir.bind(on_press=self.sugerir_filme)

        botao_limpar = Button(
            text="Limpar",
            size_hint=(1, 0.09),
            font_size=20,
            background_normal='',
            background_color=(0.7, 0.2, 0.2, 1),
            color=(1, 1, 1, 1)
        )
        botao_limpar.bind(on_press=self.limpar_campos)

        self.mensagem_label = Label(
            text="Coloque seu nome e selecione um gênero para uma nova sugestão de filme",
            size_hint=(1, 0.13),
            font_size=20,
            halign="center",
            valign="middle",
            color=(1, 1, 1, 1)
        )
        self.mensagem_label.bind(size=self.mensagem_label.setter("text_size"))

        self.imagem_filme = Image(
            source="",
            size_hint=(1, 0.51),
            allow_stretch=True,
            keep_ratio=True
        )

        layout.add_widget(self.nome_input)
        layout.add_widget(self.spinner)
        layout.add_widget(botao_sugerir)
        layout.add_widget(botao_limpar)
        layout.add_widget(self.mensagem_label)
        layout.add_widget(self.imagem_filme)

        return layout

    def sugerir_filme(self, instance):
        nome = self.nome_input.text.strip()
        genero = self.spinner.text

        if not nome:
            self.mensagem_label.text = "Por gentileza, digite seu nome."
            self.imagem_filme.source = ""
        elif genero not in filmes:
            self.mensagem_label.text = "Por gentileza, selecione um genero."
            self.imagem_filme.source = ""
        else:
            filme_sugerido = random.choice(filmes[genero])
            self.mensagem_label.text = (
                f"Olá, {nome}! Sua sugestão de filme de {genero} é: "
                f"{filme_sugerido['titulo']} ({filme_sugerido['ano']})."
            )
            self.imagem_filme.source = filme_sugerido["img"]

    def limpar_campos(self, instance):
        self.nome_input.text = ""
        self.spinner.text = "Selecione o genero do filme"
        self.mensagem_label.text = "Coloque seu nome e selecione um genero para uma nova sugestão de filme"
        self.imagem_filme.source = ""

if __name__ == "__main__":
    FilmesApp().run()