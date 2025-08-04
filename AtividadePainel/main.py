from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty, BooleanProperty
from kivy.lang import Builder

class PainelIA(BoxLayout):
    ia_ligada = BooleanProperty(False)
    status = StringProperty("IA Desligada")
    nivel_ameaca = NumericProperty(0)

    def ligar_ia(self):
        self.ia_ligada = True
        self.status = "IA Ativa"
        self.nivel_ameaca = 10

    def enviar_comando(self):
        if not self.ia_ligada:
            self.status = "Ligue a IA antes de enviar comandos."
            return
        
        comando = self.ids.entrada_comando.text.strip()
        if comando:
            self.status = f"Comando recebido: {comando}"
            self.nivel_ameaca = min(self.nivel_ameaca + 15, 100)
        else:
            self.status = "Comando vazio."

        self.ids.entrada_comando.text = ""

class PainelApp(App):
    def build(self):
        return PainelIA()

if __name__ == '__main__':
    PainelApp().run()
