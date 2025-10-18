# EJERCICIO 20: Historial de Navegación

class Navegador:
    def __init__(self):
        self.pilaAtras = []
        self.pilaAdelante = []
        self.paginaActual = None

    def visitar(self, url):
        if self.paginaActual is not None:
            self.pilaAtras.append(self.paginaActual)
        self.paginaActual = url
        self.pilaAdelante.clear()
        print(f"Visitando: {self.paginaActual}")

    def atras(self):
        if not self.pilaAtras:
            print("⚠️ No hay páginas anteriores.")
            return
        self.pilaAdelante.append(self.paginaActual)
        self.paginaActual = self.pilaAtras.pop()
        print(f"⬅️ Volviendo a: {self.paginaActual}")

    def adelante(self):
        if not self.pilaAdelante:
            print("⚠️ No hay páginas siguientes.")
            return
        self.pilaAtras.append(self.paginaActual)
        self.paginaActual = self.pilaAdelante.pop()
        print(f"➡️ Avanzando a: {self.paginaActual}")

# --- PRUEBA ---
navegador = Navegador()
navegador.visitar("google.com")
navegador.visitar("youtube.com")
navegador.visitar("chat.openai.com")
navegador.atras()
navegador.atras()
navegador.adelante()
