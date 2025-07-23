from kivy.uix.accordion import BooleanProperty
from kivy.uix.accordion import NumericProperty
from kivy.uix.actionbar import BoxLayout
from kivy.app import App
from kivy.properties import StringProperty, NumericProperty, BooleanProperty

class PlayerInfo(BoxLayout):
    player_name = StringProperty("Jogador 1")
    player_score = NumericProperty(0)
    is_online = BooleanProperty(False)

    def aumentar_score(self):
        self.player_score += 1

class CustomPropApp(App):
    def build(self):
        return PlayerInfo()

if __name__ == '__main__':
    CustomPropApp().run()
