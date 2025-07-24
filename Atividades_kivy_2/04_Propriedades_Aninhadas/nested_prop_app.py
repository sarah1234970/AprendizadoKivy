from kivy.uix.accordion import BooleanProperty
from kivy.properties import ObjectProperty
from kivy.app import App
from kivy.properties import ObjectProperty, BooleanProperty
from kivy.uix.widget import Widget

class Statusindicator(Widget):
    is_active = BooleanProperty(False)
    
class MainControlWidget(Widget):
    status_obj = ObjectProperty(Statusindicator())
    
    def toggle_status(self):
        self.status_obj.is_active = not self.status_obj.is_active

class ObjectPropertyApp(App):
    def build(self):
        return Statusindicator()
    
if __name__ == '__main__':
    ObjectPropertyApp().run()
         