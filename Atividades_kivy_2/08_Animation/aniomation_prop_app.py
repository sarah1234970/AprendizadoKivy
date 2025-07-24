from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from kivy.animation import Animation

class AnimatedBox(BoxLayout):
    box_size = NumericProperty(100)
    
    def animate_box(self):
        anim = Animation(box_size=200 if self.box_size == 100 else 100, duration=0.5)
        anim.start(self)

class AnimationPropApp(App):
    def build(self):
        return AnimatedBox()

if __name__ == '__main__':
    AnimationPropApp().run()