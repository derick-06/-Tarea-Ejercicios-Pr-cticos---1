class Rectangulo:
    def __init__(self, base, altura):
        # Constructor: inicializa los atributos base y altura
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        # Multiplica base por altura para obtener el área
        return self.base * self.altura
    
    def calcular_perimetro(self):
        # Suma base + altura y multiplica por 2
        return 2 * (self.base + self.altura)
    
    def es_cuadrado(self):
        # Compara si base es igual a altura para determinar si es cuadrado
        return self.base == self.altura
    

# EJEMPLOS DE USO
# Crear rectángulos
r1 = Rectangulo(5, 3)
# Cuadrado
r2 = Rectangulo(4, 4)  

# Operaciones
print(f"Área: {r1.calcular_area()}")            # 15
print(f"Perímetro: {r1.calcular_perimetro()}")  # 16  
print(f"¿Es cuadrado?: {r1.es_cuadrado()}")     # False

print(f"¿Es cuadrado r2?: {r2.es_cuadrado()}")  # True


