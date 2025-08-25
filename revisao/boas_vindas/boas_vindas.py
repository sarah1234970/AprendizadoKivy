from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class BoasVindasApp(App):
     
    def build(self):
            self.title = "Boas Vindas"
            
            self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
            
            self.name_input = TextInput(hint_text="Digite o seu nome", multiline=False, font_size=18)
            
            self.message_label = Label(text="Boas-Vindas!", font_size=20,
                                    halign='center', valign='middle')
            
            self.message_label.bind(size=self.message_label.setter('text_size'))

            self.button = Button(
                text="Enviar",
                font_size=18,
                size_hint=(1,0.3))
            
            self.button.bind(on_press=self.show_message)

            self.layout.add_widget(self.name_input)
            self.layout.add_widget(self.message_label)
            self.layout.add_widget(self.button)
            
            return self.layout
        
    def show_message(self, instance):
            
        name = self.name_input.text.strip()
        
        if name:
            self.message_label.text = f"Olá, {name}!"
            
        else:
            self.message_label.text = "Por favor, digite seu nome."
            

if __name__ == '__main__':
    BoasVindasApp().run()    