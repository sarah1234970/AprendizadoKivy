from kivy.app import App
from kivy.properties import  NumericProperty, AliasProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

class CalculatorWidget(BoxLayout):
    num1 = NumericProperty (10)
    num2 = NumericProperty (5)
        
    def get_sum_result(self, *args): #Vai retornar para sum result "GET"
       return self.num1 + self.num2
   
    def set_sum_result(self, value, *args):
       each = value / 2
       self.num1 = each
       self.num2 = each
       
    sum_result = AliasProperty(
        get_sum_result,
        set_sum_result,
        bind=['num1', 'num2'])

class AliasPropertyApp(App):
    def build(self):
        return CalculatorWidget()

if __name__ == '__main__':
    AliasPropertyApp().run()
         