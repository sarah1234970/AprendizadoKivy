from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.properties import NumericProperty
from kivy.core.window import Window
from kivy.animation import Animation

class IdadeApp(App):
    idade = NumericProperty(0)
    
    def build(self):
        # Configuração inicial
        Window.clearcolor = (0.1, 0.1, 0.1, 1)   # Fundo
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Título (para fiacar bonitinho)
        titulo = Label(
            text='Verificador de Idade', 
            font_size=30, 
            bold=True, 
            size_hint_y=None, 
            height=50, 
            color=(0.95, 0.95, 0.95, 1)
            
        )
        self.layout.add_widget(titulo)
        
        # O display da idade
        self.label_idade = Label(
            text=f'Idade: {self.idade} anos', 
            font_size=30,
            bold=True,
            color=(0.95, 0.95, 0.95, 1),
            size_hint_y=None,
            height=50
        )
        self.layout.add_widget(self.label_idade)
        
        # Botoes de controle
        botoes_layout = BoxLayout(spacing=10, size_hint_y=None, height=60)
        
        btn_remover = Button( # botao de remover a idade e o style dele
            text='-', 
            on_press=self.remover_idade, 
            font_size=25,
            background_color=(0.8, 0.2, 0.2, 1),
            bold=True
        )
        
        btn_adicionar = Button( # botao de adicionar a idade e o style dele
            text='+', 
            on_press=self.adicionar_idade, 
            font_size=25,
            background_color=(0.2, 0.8, 0.2, 1),
            bold=True
        )
        # cria um layout para os botoes
        botoes_layout.add_widget(btn_remover) 
        botoes_layout.add_widget(btn_adicionar) 
        self.layout.add_widget(botoes_layout)
        
        # Botão de verificação
        btn_verificar = Button( # esse e o botao de verificar a idade e o style dele
            text='Verificar Acesso', 
            on_press=self.verificar_acesso, 
            font_size=20,
            background_color=(0.2, 0.4, 0.8, 1),
            color=(1, 1, 1, 1),
            bold=True,
            size_hint_y=None,
            height=60
        )
        self.layout.add_widget(btn_verificar)
        
        # Feedback de acesso
        self.label_acesso = Label(
            text='', 
            font_size=24, 
            bold=True,
            size_hint_y=None,
            height=50
        )
        self.layout.add_widget(self.label_acesso)
        
        
        input_layout = BoxLayout(spacing=10, size_hint_y=None, height=50)
        self.input_manual = TextInput(
            hint_text='Digite a idade',
            input_filter='int',
            multiline=False,
            font_size=18,
            size_hint_x=0.7
        )
        
        btn_definir = Button(
            text='Definir',
            on_press=self.definir_idade_manual,
            size_hint_x=0.3,
            background_color=(0.4, 0.4, 0.4, 1),
            color=(1, 1, 1, 1)
        )
        
        input_layout.add_widget(self.input_manual)
        input_layout.add_widget(btn_definir)
        self.layout.add_widget(input_layout)
        
        return self.layout
    
    def on_idade(self, instance, value):
        # Atualiza automaticamente o label quando a idade muda
        self.label_idade.text = f'Idade: {self.idade} anos'
        self.limpar_feedback()
        
        # Animação de feedback
        anim = Animation(font_size=35, duration=0.1) + Animation(font_size=30, duration=0.1)
        anim.start(self.label_idade)
    
    def adicionar_idade(self, instance):
        if self.idade < 120:  # Limite máximo
            self.idade += 1
        else:
            self.label_acesso.text = 'Opaa!!Idade máxima atingida!'
            self.label_acesso.color = (0.8, 0.2, 0.2, 1)
    
    def remover_idade(self, instance):
        if self.idade > 0:
            self.idade -= 1
        else:
            self.label_acesso.text = 'Idade não pode ser negativa!Tente novamente!'
            self.label_acesso.color = (0.8, 0.2, 0.2, 1)
    
    def definir_idade_manual(self, instance):
        try:
            nova_idade = int(self.input_manual.text)
            if 0 <= nova_idade <= 90:
                self.idade = nova_idade
                self.input_manual.text = ''
            else:
                self.label_acesso.text = 'Digite entre 0 e 90 anos!'
                self.label_acesso.color = (0.8, 0.2, 0.2, 1)
        except ValueError:
            self.label_acesso.text = 'Digite um número válido!'
            self.label_acesso.color = (0.8, 0.2, 0.2, 1)
    
    def verificar_acesso(self, instance):
        if self.idade >= 18:
            self.label_acesso.text = '✅ Acesso Permitido. Liberado!'
            self.label_acesso.color = (0, 0.6, 0, 1)  # Verde
            
        elif self.idade >= 60:
            self.label_acesso.text = '✅ Você é idoso e merece todo respeito! ❤️'
            self.label_acesso.color = (0, 0.6, 0, 1)  # Verde'
            
        else:
            self.label_acesso.text = '❌ Acesso Negado. Que pena, você é menor de idade'
            self.label_acesso.color = (0.8, 0, 0, 1)  # Vermelho
        
        # Animação de feedback
        anim = Animation(font_size=26, duration=0.2) + Animation(font_size=24, duration=0.2)
        anim.start(self.label_acesso)
    
    def limpar_feedback(self):
        self.label_acesso.text = ''
        self.label_acesso.color = (0.2, 0.2, 0.2, 1)  # Cor padrão

if __name__ == '__main__':
    IdadeApp().run()