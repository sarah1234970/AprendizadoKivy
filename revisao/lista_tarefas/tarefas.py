from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.lang import Builder 
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView

Builder.load_string('''
<TarefasScreen>:
    orientation: 'vertical'
    spacing: 15
    padding: 20
    
    Label:
        text: '[b]Tarefas[/b]'
        markup: True
        font_size: 25
        halign: 'center'
        size_hint_y: None
        height: 50
        
    TextInput:
        id: inicio_tarefa
        hint_text: "Anote suas tarefas"
        size_hint_y: None
        height: 50
        multiline: False
        font_size: 20
        
    Button:
        text: 'Nova tarefa'
        size_hint_y: None
        height: 50
        font_size: 20
        on_press: root.adicionar_tarefa(inicio_tarefa.text)
        background_color: (0.2, 0.7, 0.3, 1) 
        
    ScrollView:
        Label:
            id: local_tarefas
            text: 'Suas tarefas estao aqui!!'
            size_hint_y: None
            height: self.texture_size[1]
            font_size: 20
            text_size: self.width, None
''')

class TarefasScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.lista_tarefas = []
        
    def adicionar_tarefa(self, tarefa):
        if tarefa.strip():  # Verifica se não está vazio
            self.lista_tarefas.append(tarefa)
            self.mostrar_tarefas()
            self.ids.inicio_tarefa.text = ""  # Limpa o campo 
        else:
            self.ids.local_tarefas.text = "Insira uma tarefa!"
    
    def mostrar_tarefas(self):
        if self.lista_tarefas:
            texto = ""
            for i, tarefa in enumerate(self.lista_tarefas, start=1):
                texto += f"{i}. {tarefa}\n"
            self.ids.local_tarefas.text = texto
        else: 
            self.ids.local_tarefas.text = "Nenhuma tarefa encontrada!"

class TarefasApp(App):
    def build(self):
        self.title = "Minhas Tarefas" 
        return TarefasScreen() 

if __name__ == '__main__':
    TarefasApp().run()