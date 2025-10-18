

#Listas
lista = [1, 2, 3, 4, 5]

print("=== OPERACIONES CON LISTAS ===")
# Buscar un elemento
print("¿Está el 3 en la lista?", 3 in lista)  # O(n)

# Insertar un elemento
lista.append(6)  # O(1) amortizado
print("Lista después de insertar:", lista)

# Eliminar un elemento
lista.remove(2)  # O(n)
print("Lista después de eliminar:", lista)

#Diccionarios
diccionario = {1: "uno", 2: "dos", 3: "tres"}

print("\n=== OPERACIONES CON DICCIONARIOS ===")
# Buscar una clave
print("¿Existe la clave 3?", 3 in diccionario)  # O(1) promedio

# Insertar una clave-valor
diccionario[4] = "cuatro"  # O(1) promedio
print("Diccionario después de insertar:", diccionario)

# Eliminar una clave
del diccionario[2]  # O(1) promedio
print("Diccionario después de eliminar:", diccionario)

"""
LISTAS:
Buscar: O(n) (LENTO)
Insertar: O(1) al final (amortizado), O(n) en posición específica (Medio)
Eliminar O(n) (LENTO)

DICCIONARIOS:
Buscar: O(1) (RAPIDO)
Insertar: O(1) (RAPIDO)
Eliminar: O(1) (RAPIDO)

¿Por que?

En listas se revisa elemento por elemento; en diccionarios se usa tabla hash.
Los diccionarios asignan una posición con hash automáticamente.
En listas hay que desplazar elementos; en diccionarios solo se borra la clave.

¿Cuando usar cada estructura?

listas(list) Cuando necesitas mantener un orden específico o recorrer los elementos en secuencia.
Diccionario(dict) Cuando necesitas acceso rápido por clave, sin importar el orden. Ideal para búsquedas y actualizaciones frecuentes.

"""