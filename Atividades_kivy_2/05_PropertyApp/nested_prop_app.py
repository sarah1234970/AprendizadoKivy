from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import BooleanProperty, ObjectProperty

class StatusIndicator(Widget):
    is_active = BooleanProperty(False)

class MainControlWidget(Widget):
    status_obj = ObjectProperty(StatusIndicator())
    
    def toggle_status(self):
        self.status_obj.is_active = not self.status_obj.is_active

class NestedPropApp(App):
    def build(self):
        return MainControlWidget()

if __name__ == '__main__':
    NestedPropApp().run()