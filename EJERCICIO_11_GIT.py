
def busquedaBinaria(listaOrdenada, elemento):
    izq = 0
    der = len(listaOrdenada) - 1

    while izq <= der:
        medio = (izq + der) // 2
        if listaOrdenada[medio] == elemento:
            return medio
        elif listaOrdenada[medio] < elemento:
            izq = medio + 1
        else:
            der = medio - 1

    return -1 


# Ejemplo de uso
lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
buscado = int(input("Ingresa el número a buscar: "))

posicion = busquedaBinaria(lista, buscado)

if posicion != -1:
    print(f"Elemento encontrado en la posición {posicion}.")
else:
    print("Elemento no encontrado en la lista.")

"""
Análisis de Complejidad:
 Mejor caso es O(1), Si el elemento se encuentra justo en el centro al primer intento.
 Peor caso es O(log n), En cada iteración, se descarta la mitad de la lista restante
 Caso promedio es O(log n), El número de pasos crece logarítmicamente con el tamaño de la lista.
¿Por qué es O(log n)?
Porque este divide el espacio de búsqueda en dos mitades.
Si hay n elementos al inicio, después del primer paso quedan n/2, luego n/4, luego n/8, y así sucesivamente.
El número de veces que puede dividirse n entre 2 hasta llegar a 1 es:
k=log2(n)
Por eso, la complejidad temporal es O(log n).
y aveces es mas eficiente que la búsqueda lineal porque:
Lineal (O(n))	Recorre cada elemento hasta encontrar el buscado.	
Binaria (O(log n))	Divide el rango de búsqueda a la mitad en cada paso.
"""
