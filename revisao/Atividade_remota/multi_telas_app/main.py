from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from screens.boas_vindas import BoasVindasScreen
from screens.sugestao_filmes import SugestaoFilmesScreen

class MultiTelasApp(App):
    def build(self):
        self.title = "Multi Telas App"
        sm = ScreenManager()
        sm.add_widget(BoasVindasScreen(name='boas_vindas'))
        sm.add_widget(SugestaoFilmesScreen(name='sugestao_filmes'))
        return sm

if __name__ == '__main__':
    MultiTelasApp().run()