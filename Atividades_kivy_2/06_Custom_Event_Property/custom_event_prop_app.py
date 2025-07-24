from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.event import EventDispatcher

class MyCustomWidget(EventDispatcher):
    message = StringProperty('')
    __events__ = ('on_message_changed',)
    
    def on_message(self, instance, value):
        self.dispatch('on_message_changed', value)

class CustomEventPropApp(App):
    def build(self):
        return MyCustomWidget()

if __name__ == '__main__':
    CustomEventPropApp().run()