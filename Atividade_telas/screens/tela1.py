from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

class BaseScreen(Screen):
    title = StringProperty('')

class HomeScreen(BaseScreen):
    pass

class Tela1(BaseScreen):
    pass

# (Repetir padrão similar para Screen2, Screen3, etc.)