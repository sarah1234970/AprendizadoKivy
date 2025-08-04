from kivy.app import App
from kivy.properties import StringProperty, NumericProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout

class PainelControle(BoxLayout):
    status_text= StringProperty("IA desligada")
    nivel_ameaca= NumericProperty(0)#valor de barra do projeto (0 a 100)
    ia_ligada= BooleanProperty(False)# Estado: ligado ou desligada
    
    #alternar se esta ligada ou desligada
    def alternar_ia(self):
        self.ia_ligada = not self.ia_ligada
        
        if self.ia_ligada:
            self.status_text = "IA ligada"
            self.nivel_ameaca = (30)
            
        else:
            self.status_text = "IA desligada"
            self.nivel_ameaca = (0)
            
    def enviar_comando(self, comando):
        print(f"Comando recebido:{comando}")
        if not self.ia_ligada:
            self.status_text = "IA desligada"
            return
        #alteracao do nivel de ameaca
        print(f"processando comando: {comando}")
        if comando.lower() == "alerta":
            self.nivel_ameaca = min(self.nivel_ameaca + 20, 100)     # e o valor da barra do progresso
            #min = garante que o valor nao utrapasse 100 e tipo o minimo
            self.status_text = "Alerta emitido"
        elif comando.lower() == "normalizar":
            self.nivel_ameaca = max(self.nivel_ameaca - 20, 0)
            self.status_text = "Sistema normalizado"
            #max = garante que o valor nao fique negativo
        else:
            self.status_text = f"Comando Valido: {comando}"
        print(f"Comando Valido recebidoP {comando}")
class PainelControleApp(App):
    def build(self):
        return PainelControle()
    
if __name__ == '__main__':
    PainelControleApp().run()