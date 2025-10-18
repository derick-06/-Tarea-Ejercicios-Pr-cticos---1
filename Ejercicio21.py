# EJERCICIO 21: Verificar Palíndromos

def es_palindromo(texto):
    texto_limpio = "".join(texto.lower().split())  # sin espacios ni mayúsculas
    pila = []

    mitad = len(texto_limpio) // 2
    for i in range(mitad):
        pila.append(texto_limpio[i])

    inicio = mitad + 1 if len(texto_limpio) % 2 != 0 else mitad

    for i in range(inicio, len(texto_limpio)):
        if not pila or texto_limpio[i] != pila.pop():
            return False
    return True

# --- PRUEBA ---
palabras = ["anilina", "radar", "reconocer", "python", "neuquen"]
for palabra in palabras:
    print(f"{palabra}: {'✅ Palíndromo' if es_palindromo(palabra) else '❌ No lo es'}")
