from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.lang import Builder 
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
import random


class FilmesApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        self.nome_input = TextInput(
            hint_text='Digite seu nome',
            multiline=False,
            size_hint=(1, 0.1)
            )
        #genero do filme 
        self.spinner = Spinner(
            text="Selecione o genero do filme",
            values=["Drama", "Comédia", "Terror", "Ação", "Animação"],
            size_hint=(1, 0.1))
        
        botao = Button(
            text="Sugerir Filme", #nome do botao
            size_hint=(1, 0.1),
            on_press=self.sugerir_filme
        )
        botao.bind(on_press=self.sugerir_filme)
        
        self.mensagem_label = Label(
            text="Coloque seu nome e selecione um genero para uma nova sugestão de filme",
            size_hint=(1, 0.1), 
            halign="center",
            valign="middle")
        self.mensagem_label.bind(size=self.mensagem_label.setter("text_size"))
        
        #Widgets do layout
        layout.add_widget(self.nome_input)
        layout.add_widget(self.spinner)
        layout.add_widget(botao)
        layout.add_widget(self.mensagem_label)
        return layout
    
    #Quando o botao for iniciado
    def sugerir_filme(self, instance):
        filmes = {
        "Comédia":["As Branquelas","Todo Mundo em Pânico","Garotas Malvadas" ],
        "Terror":["Invocação do Mal","It A Coisa","A Hora do Pesadelo" ],
        "Ação":["Velozes e Furiosos","Missão Impossível","Vingadores: Ultimato" ],
        "Drama":["A Procura da Felicidade","O Menino do Pijama Listrado","Clube da Luta" ],
        "Animação":["Procurando Nemo","Divertidamente","Shrek", ]
        }
        
        nome = self.nome_input.text.strip() 
        genero = self.spinner.text
        
        if not nome:
            self.mensagem_label.text = "Por gentileza, digite seu nome."
        elif genero not in filmes:
            self.mensagem_label.text = "Por gentileza, selecione um genero."
        else:
            filme_sugerido = random.choice(filmes[genero])
            self.mensagem_label.text =f"Olá, {nome}! Sua sugestão de filme é:{filme_sugerido}."
            
if __name__ == "__main__":
    FilmesApp().run()