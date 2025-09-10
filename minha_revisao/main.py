from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Teste(App):
    def build(self):
        box = BoxLayout(orientation='vertical', padding=30, spacing=18)
        btn = Button(text="botao 1")
        label = Label(text="text 1")
        box.add_widget(btn)
        box.add_widget(label)
        
        box2 = BoxLayout()
        btn2 = Button(text="botao 2")
        label2 = Label(text="text 2")
        box2.add_widget(btn2)
        box2.add_widget(label2)
        box.add_widget(box2)
        
        return box  
Teste().run()