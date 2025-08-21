from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class Boas_vindas(BoxLayout):
    mensagem = StringProperty("Boas-Vindas!")
    
    def on_enviar_nome(self, instance):
        nome_usuario = self.ids.entrada_nome.text.strip()
        if nome_usuario:
            self.mensagem = f"Olá, {nome_usuario}!"
        else:
            self.mensagem = "Por favor, digite seu nome."

class BoasVindasApp(App):
    def build(self):
        return Boas_vindas()

if __name__ == '__main__':
    BoasVindasApp().run()


        