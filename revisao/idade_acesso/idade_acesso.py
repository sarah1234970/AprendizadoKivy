from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.label import Label


class IdadeApp(App):
    def build(self):
        self.idade = 0
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.label_idade = TextInput(hint_text=f'idade: {self.idade}', font_size=30)
        self.layout.add_widget(self.label_idade)
        
        btn_adicionar = Button( text='Adicionar Idade', on_press=self.adicionar_idade, font_size=20)
        self.layout.add_widget(btn_adicionar)
        
        btn_remover = Button (text='Remover Idade', on_press=self.remover_idade, font_size=20)
        self.layout.add_widget(btn_remover) # type: ignore
        
        btn_verificar = Button(text='Verificar Acesso', on_press=self.verificar_acesso, font_size=20)#type: ignore
        self.layout.add_widget(btn_verificar)
        
        self.label_acesso = Label(text='')
        self.layout.add_widget(self.label_acesso)
        
        return self.layout
    
    def adicionar_idade(self, instance):
        self.idade += 1
        self.label_idade.text = f'idade: {self.idade}'
        self.label_acesso.text = '' # ele da uma resposta de acesso?
        
    def remover_idade(self, instance):
        if self.idade > 0:
            self.idade -= 1
            self.label_idade.text = f'Idade: {self.idade}'
            self.label_acesso.text = '' # ele da uma resposta de acesso?

    def verificar_acesso(self, instance):
        if self.idade >= 18:
            self.label_acesso.text = 'Acesso Permitido'
        else:
            self.label_acesso.text = 'Acesso Negado'
            
if __name__ == '__main__':
    IdadeApp().run()
        
        