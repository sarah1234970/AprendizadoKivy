from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import DictProperty

class ThemedApp(App):
    app_theme = DictProperty({
        'primary': [0.2, 0.6, 0.8, 1],
        'secondary': [0.9, 0.9, 0.9, 1]
    })
    
    def change_theme(self):
        self.app_theme = {
            'primary': [0.8, 0.2, 0.2, 1] if self.app_theme['primary'][0] == 0.2 else [0.2, 0.6, 0.8, 1],
            'secondary': [0.1, 0.1, 0.1, 1] if self.app_theme['secondary'][0] == 0.9 else [0.9, 0.9, 0.9, 1]
        }  # Indentação corrigida
    
    def build(self):
        return BoxLayout()

if __name__ == '__main__':
    ThemedApp().run()