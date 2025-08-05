from kivy.app import App
from kivy.properties import StringProperty, NumericProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from datetime import datetime

class PainelControle(BoxLayout):
    status_text= StringProperty("IA desligada")
    nivel_ameaca= NumericProperty(0)#valor de barra do projeto (0 a 100)
    ia_ligada= BooleanProperty(False)# Estado: ligado ou desligada
    log_text= StringProperty("")
    
    #alternar se esta ligada ou desligada
    def alternar_ia(self):
        self.ia_ligada = not self.ia_ligada
        
        if self.ia_ligada:
            self.status_text = "IA ligada"
            self.nivel_ameaca = 30
            self.adicionar_log("IA ativada - Sistema Ativo")
            
        else:
            self.status_text = "IA desligada"
            self.nivel_ameaca = 0
            self.adicionar_log(" IA ativada - Todos os sistemas desativados")
            
    def enviar_comando(self, comando):
        self.adicionar_log(f"Comando recebido: {comando}")
        print(f"Comando recebido:{comando}")
        if not self.ia_ligada:
            self.status_text = "IA desligada"
            self.adicionar_log("Tentativa de comando desligada")
            return
        
        comando = comando
        #alteracao do nivel de ameaca
        print(f"processando comando: {comando}")
        if comando == "alerta":
            self.nivel_ameaca = min(self.nivel_ameaca + 20, 100)     # e o valor da barra do progresso
            self.status_text = "Alerta emitido"
            self.adicionar_log("Nivel de ameaca aumentando")
            
        elif comando == "normalizar":
            self.nivel_ameaca = max(self.nivel_ameaca - 20, 0)
            self.status_text = "Sistema normalizado"
            self.adicionar_log("Nivel de ameaca reduzido")
            
        elif comando == "injetar_virus":
            self.nivel_ameaca = min(self.nivel_ameaca + 30, 100)
            self.status_text = "IA: Invasao detectada! Medidas ativadas!" 
            self.adicionar_log("Tentativa de virus foi encontrada")
        
        elif comando == "desligar_sistemas":
            self.nivel_ameaca = 100
            self.status_text = "IA: ALERTA! Tente novamente"
            self.adicionar_log("Tentativa de desligamento nao foi acessa.")
            
        elif comando == "acessar_dados":
            self.nivel_ameaca = min(self.nivel_ameaca + 15, 100)
            self.status_text = "IA: Acesso confirmado"
            self.adicionar_log("Acesso a banco de dados foi vizualizado")            
            
        else:
            self.status_text = f"IA: Acesso nao recebido - '{comando}'"
            self.adicionar_log(f"Comando não reconhecido: {comando}")
        print(f"Comando Valido recebido {comando}")
        
    def adicionar_log(self, mensagem):
        timestamp = datetime.now().strftime("%H:%M:%S") # responsalvel por criar uma string que tem o formato de horas"H", minutos"M" e segundos"S"
        log_entry = f"[{timestamp}] {mensagem}\n"
        self.log_text = log_entry + self.log_text
        
    
class PainelControleApp(App):
    def build(self):
        return PainelControle()
    
if __name__ == '__main__':
    PainelControleApp().run()