from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.lang import Builder

class BoasVindasApp(App):
    def build(self):
        self.title = "Boas Vindas"
        return BoasVindasScreen()
    
Builder.load_string('''
<Boas_vindas>:
    orientation: 'vertical'
    padding: 10
    spacing: 10
    
      Label:
        text: '[b]App de Boas-vindas[/b]'
        markup: True 
        size_hint_y: None
        height: '50dp'
        font_size: '20sp'
        halign: 'center'
        valign: 'middle'
        text_size: self.width, None

    TextInput:
        id: entrada_nome
        hint_text: "Digite o seu nome"
        size_hint_y: None
        height: '50dp'
        font_size: '18sp'
        multiline: False
        on_text_validate: root.on_enviar_nome()
        padding: '10dp'

    Button:
        text: 'Enviar'
        size_hint_y: None
        height: '50dp'
        font_size: "20sp"
        background_normal: ""
        background_color: (0.2, 0.6, 0.8, 1)
        on_release: root.on_enviar_nome()

    Label:
        text: root.mensagem
        halign: 'center'
        valign: 'middle'
        text_size: self.width, None
        size_hint_y: None
        height: '50dp'
        font_size: '18sp'
        color: 0.2, 0.4, 0.6, 1
        bold: True
''')

class BoasVindasScreen(BoxLayout):
    mensagem = StringProperty("Boas-Vindas!")
    
    def on_enviar_nome(self,):
        nome_usuario = self.ids.entrada_nome.text.strip()
        if nome_usuario:
            self.mensagem = f"Olá, {nome_usuario}!"
        else:
            self.mensagem = "Por favor, digite seu nome."



if __name__ == '__main__':
    BoasVindasApp().run()    