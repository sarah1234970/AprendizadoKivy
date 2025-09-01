# language: python
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

# ...existing code...
class BoasVindasScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.name_input = TextInput(hint_text="Digite o seu nome", multiline=False, font_size=18, size_hint=(1, 0.2))
        self.message_label = Label(text="Boas-Vindas!", font_size=20, halign='center', valign='middle')
        self.message_label.bind(size=self.message_label.setter('text_size'))
        btn = Button(text="Continuar", size_hint=(1, 0.2), font_size=18)
        btn.bind(on_press=self.ir_para_sugestao)

        layout.add_widget(self.name_input)
        layout.add_widget(self.message_label)
        layout.add_widget(btn)
        self.add_widget(layout)

    def ir_para_sugestao(self, instance):
        nome = self.name_input.text.strip()
        if not nome:
            self.message_label.text = "Por favor, digite seu nome."
            return
        # passar dado para a tela de sugestao definindo atributo na instância da tela destino
        if self.manager:
            tela_sug = self.manager.get_screen('sugestao_filmes')
            tela_sug.username = nome
            # alternativa: App.get_running_app().username = nome
            self.manager.current = 'sugestao_filmes'