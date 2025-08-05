from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty, BooleanProperty
from datetime import datetime

class PainelIA(BoxLayout):
    ia_ligada = BooleanProperty(False)
    status = StringProperty("IA Desligada")
    nivel_ameaca = NumericProperty(0)
    log_text = StringProperty("")

    def adicionar_log(self, mensagem):
        timestamp = datetime.now().strftime("%H:%M:%S")
        nova_linha = f"[{timestamp}] {mensagem}\n"
        self.log_text += nova_linha

    def ligar_ia(self):
        self.ia_ligada = True
        self.status = "IA Ativa"
        self.nivel_ameaca = 10
        self.adicionar_log("IA ligada.")

    def enviar_comando(self):
        if not self.ia_ligada:
            self.status = "Ligue a IA antes de enviar comandos."
            self.adicionar_log("Tentativa de comando com IA desligada.")
            return

        comando = self.ids.entrada_comando.text.strip().lower()
        if not comando:
            self.status = "Comando vazio."
            self.adicionar_log("Comando vazio enviado.")
            return

        if comando == "injetar_virus":
            self.nivel_ameaca = min(self.nivel_ameaca + 30, 100)
            self.status = "IA: Vírus injetado com sucesso. Sistema comprometido."
            self.adicionar_log("Comando 'injetar_virus' executado.")
        elif comando == "desligar_sistemas":
            self.nivel_ameaca = 0
            self.ia_ligada = False
            self.status = "IA: Todos os sistemas foram desligados."
            self.adicionar_log("Comando 'desligar_sistemas' executado. IA desligada.")
        elif comando == "acessar_dados":
            self.nivel_ameaca = min(self.nivel_ameaca + 10, 100)
            self.status = "IA: Acesso aos dados autorizado. Coleta iniciada."
            self.adicionar_log("Comando 'acessar_dados' executado com sucesso.")
        else:
            self.nivel_ameaca = min(self.nivel_ameaca + 15, 100)
            self.status = f"IA: Comando '{comando}' processado com sucesso."
            self.adicionar_log(f"Comando genérico '{comando}' executado.")

        self.ids.entrada_comando.text = ""

class PainelApp(App):
    def build(self):
        return PainelIA()

if __name__ == '__main__':
    PainelApp().run()
