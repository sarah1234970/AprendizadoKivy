from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Teste(App):
    def build(self):
        box = BoxLayout(orientation='vertical')
        btn = Button(text= 'studing kivy', font_size=30, on_release=self.incrementar)
        self.label = Label(text='1', font_size=30)
        box.add_widget(btn)
        box.add_widget(self.label)

        return box
    def incrementar(self, button):
        button.text = 'AI SIMMM'
        self.label.text =  str (int(self.label.text)+1)
Teste().run()