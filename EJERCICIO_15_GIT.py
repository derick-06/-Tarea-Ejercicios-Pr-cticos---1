def invertir_cadena(texto):
    pila = []  # Usamos una lista como pila
    
    # Apilamos cada carácter
    for caracter in texto:
        pila.append(caracter)
    
    resultado = ""
    
    # Desapilamos para invertir el orden
    while pila:
        resultado += pila.pop()
    
    return resultado

# Ejemplo de uso:
cadena = "HOLA"
print("Cadena original:", cadena)
print("Cadena invertida:", invertir_cadena(cadena))
