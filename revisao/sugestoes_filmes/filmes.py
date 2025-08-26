from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.lang import Builder 
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView

class FilmesApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.scroll_view = ScrollView()