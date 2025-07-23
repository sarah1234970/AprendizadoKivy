from kivy.uix.accordion import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App

class MyWidget(BoxLayout):
    saudacao = StringProperty("Ola Kivy!")
    
class StringPropApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
   StringPropApp().run()