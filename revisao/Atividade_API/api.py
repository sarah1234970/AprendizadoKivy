import requests
import threading
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.togglebutton import ToggleButton
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.graphics import Color, Rectangle

Window.clearcolor = get_color_from_hex('#2c3e50')

class JokeApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.language = 'pt'
        self.portuguese_jokes = [
            "O que o pato disse para a pata? Vem quá!",
            "Por que o menino estava falando no telefone deitado? Para não cair a ligação.",
            "Qual é o contrário de volátil? Vem cá sofrer!",
            "Por que a plantinha não foi atendida no hospital? Porque só tinha médico de plantão."
        ]
        self.english_jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? He was outstanding in his field!",
            "Why don't eggs tell jokes? They'd crack each other up!",
            "What do you call a fake noodle? An impasta!",
            "Why did the math book look so sad? Because it had too many problems!"
        ]

    def build(self):
        # Layout inicial
        self.layout = BoxLayout(orientation='vertical', 
                               padding=30, 
                               spacing=20)
        
        Window.clearcolor = get_color_from_hex('#000000')
        # fUNDO 
        with self.layout.canvas.before:
            Color(0, 0, 0, 1)  # Cor inicial do gradiente
            self.rect = Rectangle(size=Window.size, pos=self.layout.pos)
        
        # Título
        title_label = Label(
            text="App de Piadas",
            font_size=24,
            bold=True,
            color=get_color_from_hex("#FFFFFF"),
            size_hint=(1, 0.2)
        )
        
        # Botão de idioma
        self.lang_button = ToggleButton(
            text="PT BR / EN US",
            size_hint=(1, 0.1),
            font_size=16,
            background_color=get_color_from_hex('#3498db'),
            color=get_color_from_hex('#ecf0f1'),
            bold=True
        )
        self.lang_button.bind(on_press=self.toggle_language)
        
        # Label da piada
        self.joke_label = Label(
            text="Clique no botão para uma piada engraçada!",
            font_size=20,
            halign='center',
            valign='middle',
            color=get_color_from_hex("#FFFFFF"),
            text_size=(Window.width - 60, None),
            size_hint_y=None,
            height=150
        )
        self.joke_label.bind(size=self.joke_label.setter('text_size'))
        
        # Botão de nova piada
        self.button = Button(
            text="Nova Piada:D",
            size_hint=(1, 0.15),
            font_size=20,
            background_color=get_color_from_hex('#e74c3c'),
            color=get_color_from_hex('#ecf0f1'),
            bold=True
        )
        self.button.bind(on_press=self.fetch_joke)
        
        # Adicionar widgets ao layout
        self.layout.add_widget(title_label)
        self.layout.add_widget(self.lang_button)
        self.layout.add_widget(self.joke_label)
        self.layout.add_widget(self.button)
        
        return self.layout

    def fetch_joke(self, instance):
        # Feedback visual no botão
        instance.text = "Carregando..."
        instance.background_color = get_color_from_hex('#95a5a6')
        
        # Executar em thread separada
        threading.Thread(target=self._fetch_joke_thread, daemon=True).start()

    def _fetch_joke_thread(self):
        try:
            if self.language == 'pt':
                # Usar piadas em português pré-definidas
                import random
                text = random.choice(self.portuguese_jokes)
            else:
                # Buscar piada em inglês da API
                url = "https://official-joke-api.appspot.com/random_joke"
                response = requests.get(url, timeout=5)
                if response.status_code == 200:
                    joke_data = response.json()
                    setup = joke_data.get('setup', '')
                    punchline = joke_data.get('punchline', '')
                    text = f"{setup}\n\n{punchline}"
                else:
                    text = "Error fetching joke. Try again."
        except Exception as e:
            text = "Erro de conexão. Usando piada local." if self.language == 'pt' else "Connection error. Using local joke."
            import random
            if self.language == 'pt':
                text = random.choice(self.portuguese_jokes)
            else:
                text = random.choice(self.english_jokes)
        
        # Atualizar UI no thread principal
        Clock.schedule_once(lambda dt: self._update_label(text))

    def _update_label(self, text):
        self.joke_label.text = text
        # Restaurar botão
        self.button.text = "^^ Nova Piada" if self.language == 'pt' else "^^ New Joke"
        self.button.background_color = get_color_from_hex('#e74c3c')

    def toggle_language(self, instance):
        if instance.state == 'down':
            self.language = 'en'
            instance.text = "EN US / PT BR"
            self.button.text = "^^ New Joke"
            self.joke_label.text = "Click the button for a funny joke!"
        else:
            self.language = 'pt'
            instance.text = "PT BR / EN US"
            self.button.text = "^^ Nova Piada"
            self.joke_label.text = "Clique no botão para uma piada engraçada!"

    def on_start(self):
        # Atualiza o tamanho do retângulo de fundo
        self.layout.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

if __name__ == '__main__':
    JokeApp().run()
