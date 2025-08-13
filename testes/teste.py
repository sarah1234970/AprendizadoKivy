from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class Test(App):
    def build(self):
        box = BoxLayout(orientation='vertical')
        button = Button(text='Botao 1')
        label = Label(text='Texto 1')
        box.add_widget(button)
        box.add_widget(label)

    
        return box
Test().run()