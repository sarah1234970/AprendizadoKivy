from kivy.uix.accordion import StringProperty
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import DictProperty
from kivy.properties import StringProperty

class UserProfileWidget(BoxLayout):
   user_data  = DictProperty({'name': 'João', 'age': 30, 'city': 'São Paulo'})
   def update_age(self):
    self.user_data['age'] += 1
    
class DictPropertyApp(App):
    def build(self):
        return UserProfileWidget()
    
if __name__ == '__main__':
        DictPropertyApp().run()