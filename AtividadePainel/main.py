from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, BooleanProperty, NumericProperty

# Carrega manualmente o arquivo KV
Builder.load_file("painel.kv")

class PainelControle(BoxLayout):
    status = StringProperty("IA Desligada")
    ia_ativa = BooleanProperty(False)
    nivel_ameaca = NumericProperty(0)

    def alternar_ia(self):
        self.ia_ativa = not self.ia_ativa
        if self.ia_ativa:
            self.status = "IA Ativa"
            self.nivel_ameaca = 25
        else:
            self.status = "IA Desligada"
            self.nivel_ameaca = 0

    def enviar_comando(self):
        comando = self.ids.campo_comando.text.strip()
        if not comando:
            self.status = "Comando vazio."
            return

        if self.ia_ativa:
            self.status = f"Executando: {comando}"
            self.nivel_ameaca = min(self.nivel_ameaca + 10, 100)
        else:
            self.status = "Não é possível enviar comandos. IA está desligada."

        self.ids.campo_comando.text = ""

class PainelApp(App):
    def build(self):
        return PainelControle()

if __name__ == '__main__':
    PainelApp().run()
 