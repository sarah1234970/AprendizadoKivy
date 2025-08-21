from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class HomeScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10
        self.padding = 10

        self.add_widget(Label(text='Bem-vindo! Qual é o seu nome?'))

        self.name_input = TextInput(multiline=False)
        self.add_widget(self.name_input)

        self.greet_button = Button(text='Dizer Olá')
        self.greet_button.bind(on_press=self.greet_user)
        self.add_widget(self.greet_button)

        self.greeting_label = Label(text='')
        self.add_widget(self.greeting_label)

    def greet_user(self, instance):
        user_name = self.name_input.text
        if user_name:
            self.greeting_label.text = f'Olá, {user_name}!'
        else:
            self.greeting_label.text = 'Por favor, digite seu nome.'

class BoasVindasApp(App):
    def build(self):
        return HomeScreen()

if __name__ == '__main__':
    BoasVindasApp().run()