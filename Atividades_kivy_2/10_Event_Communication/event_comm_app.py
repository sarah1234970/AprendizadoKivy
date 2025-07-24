from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ObjectProperty
from kivy.event import EventDispatcher

class GlobalState(EventDispatcher):
    current_status = StringProperty('Initial Status')

class StatusDisplayWidget(BoxLayout):
    global_state_obj = ObjectProperty()

class StatusChangerWidget(BoxLayout):
    global_state_obj = ObjectProperty()

class EventCommApp(App):
    def build(self):
        gs = GlobalState()
        root = BoxLayout(orientation='vertical')
        root.add_widget(StatusDisplayWidget(global_state_obj=gs))
        root.add_widget(StatusChangerWidget(global_state_obj=gs))
        return root

if __name__ == '__main__':
    EventCommApp().run()