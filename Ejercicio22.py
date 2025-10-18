# EJERCICIO 22: Sistema Deshacer/Rehacer

class EditorTexto:
    def __init__(self):
        self.contenido = ""
        self.pilaDeshacer = []
        self.pilaRehacer = []

    def escribir(self, texto):
        self.pilaDeshacer.append(self.contenido)
        self.contenido += texto
        self.pilaRehacer.clear()
        print(f"✍️ Escribiendo: '{texto}' → Contenido actual: {self.contenido}")

    def deshacer(self):
        if not self.pilaDeshacer:
            print("⚠️ Nada que deshacer.")
            return
        self.pilaRehacer.append(self.contenido)
        self.contenido = self.pilaDeshacer.pop()
        print(f"↩️ Deshacer → Contenido actual: {self.contenido}")

    def rehacer(self):
        if not self.pilaRehacer:
            print("⚠️ Nada que rehacer.")
            return
        self.pilaDeshacer.append(self.contenido)
        self.contenido = self.pilaRehacer.pop()
        print(f"↪️ Rehacer → Contenido actual: {self.contenido}")

# --- PRUEBA ---
editor = EditorTexto()
editor.escribir("Hola")
editor.escribir(" Mundo")
editor.deshacer()
editor.rehacer()
editor.escribir("!")
