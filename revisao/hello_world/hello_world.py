from kivy.properties import StringProperty
from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class MinhaWidget(BoxLayout):
    text = StringProperty("Hello World!")
    
    def __init__(self, **kwargs):
         super().__init__(**kwargs)
         self.add_widget(Label(text=self.text))
    
class Teste(App):
    def build(self):
        return MinhaWidget()
    
if __name__ == '__main__':
        Teste().run()