from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty

class ValidatedInputWidget(Widget):
    _validated_text = StringProperty('')
    
    def get_validated_text(self):
        return self._validated_text
    
    def set_validated_text(self, value):
        if len(value) >= 5 and not any(char.isdigit() for char in value):
            self._validated_text = value
        else:
            # Mantém o valor anterior
            pass
    
    validated_text = property(get_validated_text, set_validated_text)

class ValidationPropApp(App):
    def build(self):
        return ValidatedInputWidget()

if __name__ == '__main__':
    ValidationPropApp().run()