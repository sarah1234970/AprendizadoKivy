
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line 
from random import random
from kivy.uix.slider import Slider
from kivy.uix.boxlayout import BoxLayout

class MeuPaintWidget(Widget):
    def __init__(self, **kwargs):
        super(MeuPaintWidget, self).__init__(**kwargs)
        self.line_width = 2
        
    def on_touch_down(self, touch):
        color = (random(), 1, 1)
        with self.canvas:
            Color(*color, mode='hsv')
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=self.line_width)
                 
    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]

class MeuPaintApp(App):
    def build(self): 
        main_layout = BoxLayout(orientation='vertical')
        controls_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        
        # Botão para limpar
        clearbtn = Button(text='Limpar')
        clearbtn.bind(on_release=self.clear_canvas)
        
        # Slider para controle da espessura
        self.slider = Slider(min=1, max=20, value=2, step=1)
        self.slider.bind(value=self.on_slider_change)
        
        # Adiciona controles ao layout de controles
        controls_layout.add_widget(clearbtn)
        controls_layout.add_widget(self.slider)
        
        # Área de pintura
        self.painter = MeuPaintWidget()
        
        # Adiciona tudo ao layout principal
        main_layout.add_widget(controls_layout)
        main_layout.add_widget(self.painter)
        
        return main_layout
    
    def on_slider_change(self, instance, value):
        # Atualiza a espessura da linha quando o slider muda
        self.painter.line_width = value
    
    def clear_canvas(self, obj):
        self.painter.canvas.clear()

if __name__ == '__main__':
    MeuPaintApp().run()