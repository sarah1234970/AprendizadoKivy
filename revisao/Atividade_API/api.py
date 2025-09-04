# language: python
# ...existing code...
import requests
import threading
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from googletrans import Translator

class JokeApp(App):
    def build(self):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.translator = Translator()
        self.language = 'pt'
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.lang_button = Button(text="PT/EN", size_hint=(1, 0.1), font_size=14)
        self.lang_button.bind(on_press=self.toggle_language)
        
        self.joke_label = Label(text="Clique no botão para uma piada!",
                        font_size=18,
                        halign='center',
                        valign='middle')
        self.joke_label.bind(size=self.joke_label.setter('text_size'))
        self.button = Button(text="Nova Piada", size_hint=(1, 0.2), font_size=18)
        self.button.bind(on_press=self.fetch_joke)

        self.layout.add_widget(self.joke_label)
        self.layout.add_widget(self.button)
        return self.layout

    def fetch_joke(self, instance):
        # executar requisição em thread separada para não bloquear a UI
        threading.Thread(target=self._fetch_joke_thread, daemon=True).start()

    def _fetch_joke_thread(self):
        try:
            url = "https://official-joke-api.appspot.com/random_joke"
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                joke_data = response.json()
                setup = joke_data.get('setup', '')
                punchline = joke_data.get('punchline', '')
                text = f"{setup}\n\n{punchline}"
            else:
                text = "Erro ao buscar piada. Tente novamente."
        except Exception as e:
            text = f"Erro: {str(e)}"
        # atualizar UI no thread principal
        Clock.schedule_once(lambda dt: self._update_label(text))

    def _update_label(self, text):
        self.joke_label.text = text

if __name__ == '__main__':
    JokeApp().run()
# ...existing code...
