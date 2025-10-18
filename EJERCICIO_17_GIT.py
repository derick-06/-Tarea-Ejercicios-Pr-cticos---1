def validar_parentesis(expresion: str) -> bool:
    """
    Verifica si los paréntesis (), corchetes [] y llaves {} están balanceados
    y correctamente anidados.

    Ejemplos:
    >>> validar_parentesis("{[()]}")
    True
    >>> validar_parentesis("{[(])}")
    False
    >>> validar_parentesis("{[}")
    False
    """
    pila = []

    # Se agregó este diccionario para manejar todos los tipos de delimitadores
    pares = {')': '(', ']': '[', '}': '{'}

    for caracter in expresion:
        #Antes: solo verificaba si era '('
        # Ahora: verificamos si es cualquiera de los símbolos de apertura
        if caracter in pares.values():  # (, [, {
            pila.append(caracter)

        #Antes: solo verificaba si era ')'
        # Ahora: verificamos si es un símbolo de cierre
        elif caracter in pares.keys():  # ), ], }
            if not pila:  # Si la pila está vacía, no hay con qué cerrar
                return False
            if pila.pop() != pares[caracter]:  # Orden incorrecto
                return False

    #Si la pila queda vacía, todo está correctamente balanceado
    return len(pila) == 0


#Casos de prueba:
casos = [
    ("{[()]}", True),
    ("{[(])}", False),
    ("{[}", False),
    ("()", True),
    ("([]{})", True),
    ("([)]", False),
    ("", True),
]

for expresion, esperado in casos:
    resultado = validar_parentesis(expresion)
    estado = "✓" if resultado == esperado else "✗"
    print(f"{estado} '{expresion}' → {resultado} (esperado: {esperado})")
