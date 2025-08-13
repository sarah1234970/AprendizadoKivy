from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

class HomeScreen(Screen):
    title = StringProperty('Tela Principal')

    def go_to_screen(self, screen_name):
        # Você pode adicionar lógica aqui antes de mudar de tela
        print(f"Indo para {screen_name}")
        self.manager.current = screen_name