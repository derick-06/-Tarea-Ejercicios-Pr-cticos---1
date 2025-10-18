def sumaElementos(lista):
        suma = 0
        for elemento in lista:
            suma = suma + elemento
        return suma
    #Ejemplo de Uso
numeros = [2, 4, 6, 8, 10]
resultado = sumaElementos(numeros)
print("La suma de los elementos es:", resultado)
    
    #Analisis de complejidad
"""Operación principal: la instrucción suma = suma + elemento
    se ejecuta una vez por cada elemento de la lista.
    Si la lista tiene N elementos:   
    El bucle for elemento in lista: se ejecuta N veces.
    Por tanto, el tiempo de ejecución crece linealmente con n.
    La Complejidad temporal O(n), La complejidad espacial O(1)"""
