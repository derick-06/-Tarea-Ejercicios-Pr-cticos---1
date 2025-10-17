class Conjunto:
    def __init__(self):
        # Constructor: crea un conjunto vacío usando set() ; set() automáticamente elimina duplicados
        self.elementos = set()
    def agregar(self, elemento):
        # Agrega un elemento al conjunto ; Si el elemento ya existe, no lo duplica
        self.elementos.add(elemento)   
    def eliminar(self, elemento):
        # Elimina un elemento si existe ; Retorna True si lo eliminó, False si no existía
        if elemento in self.elementos:
            self.elementos.remove(elemento)
            return True
        return False 
    def contiene(self, elemento):
        # Verifica si el elemento está en el conjunto ; Retorna True o False
        return elemento in self.elementos  
    def tamaño(self):
        # Retorna la cantidad de elementos en el conjunto
        return len(self.elementos)  
    def union(self, otro_conjunto):
        # Crea un nuevo conjunto con todos los elementos de ambos ; Unión: elementos que están en A o en B
        nuevo = Conjunto()
        nuevo.elementos = self.elementos.union(otro_conjunto.elementos)
        return nuevo
    def interseccion(self, otro_conjunto):
        # Crea un nuevo conjunto con elementos comunes ; Intersección: elementos que están en A y en B
        nuevo = Conjunto()
        nuevo.elementos = self.elementos.intersection(otro_conjunto.elementos)
        return nuevo
    def diferencia(self, otro_conjunto):
        # Crea un nuevo conjunto con elementos de A que no están en B ; Diferencia: A - B = elementos en A pero no en B
        nuevo = Conjunto()
        nuevo.elementos = self.elementos.difference(otro_conjunto.elementos)
        return nuevo
# EJEMPLOS DE USO
conjuntoA = Conjunto()
conjuntoB = Conjunto()
# Agregar elementos
conjuntoA.agregar(1)
conjuntoA.agregar(2)
conjuntoA.agregar(3)
conjuntoB.agregar(2)
conjuntoB.agregar(3)
conjuntoB.agregar(4)
print(f"Conjunto A: {conjuntoA.elementos}")
print(f"Conjunto B: {conjuntoB.elementos}")
# Operaciones entre conjuntos
union = conjuntoA.union(conjuntoB)
print(f"Unión A U B: {union.elementos}")
interseccion = conjuntoA.interseccion(conjuntoB)
print(f"Intersección A n B: {interseccion.elementos}")
diferencia = conjuntoA.diferencia(conjuntoB)
print(f"Diferencia A-B: {diferencia.elementos}")
# Operaciones
print(f"¿A contiene 2?: {conjuntoA.contiene(2)}")
print(f"Tamaño de A: {conjuntoA.tamaño()}")


