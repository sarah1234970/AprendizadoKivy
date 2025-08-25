from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        
        # Criar layout principal
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Adicionar widgets
        title_label = Label(text='Tela Inicial', font_size=24)
        layout.add_widget(title_label)
        
        # Botão de exemplo
        button = Button(text='Ir para Tela 1', size_hint=(1, 0.2))
        layout.add_widget(button)
        
        button.bind(on_press=self.go_to_tela1)
        layout.add_widget(button)
        
        # Adicionar layout à tela
        self.add_widget(layout)
        
    def go_to_tela1(self, instance):
        self.manager.current = 'tela1'
      
        