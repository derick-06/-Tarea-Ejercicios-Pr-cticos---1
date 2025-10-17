class Fecha:
    def __init__(self, dia, mes, año):
        # Constructor: guarda día, mes y año
        self.dia = dia
        self.mes = mes
        self.año = año
    def es_bisiesto(self):
        # Es un año es bisiesto si es divisible por 4 y no es divisible por 100, excepto si es divisible por 400
        return (self.año % 4 == 0 and self.año % 100 != 0) or (self.año % 400 == 0)  
    def es_valida(self):
        # Verifica si la fecha es válida según el calendario ; Primero chequea mes válido (1-12)
        if self.mes < 1 or self.mes > 12:
            return False  
        # Límites de días según mes
        dias_por_mes = [31, 29 if self.es_bisiesto() else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]   
        # Chequea si el día está en el rango válido para ese mes
        if self.dia < 1 or self.dia > dias_por_mes[self.mes - 1]:
            return False      
        return True   
    def es_anterior(self, otra_fecha):
        # Compara si esta fecha es anterior a otra_fecha ; Primero compara años, luego meses, luego días
        if self.año != otra_fecha.año:
            return self.año < otra_fecha.año
        if self.mes != otra_fecha.mes:
            return self.mes < otra_fecha.mes
        return self.dia < otra_fecha.dia
    def dias_entre(self, otra_fecha):
        # Calcula la diferencia en días entre dos fechas ; Convierte ambas fechas a días totales y resta
        dias_self = self._a_dias_totales()
        dias_otra = otra_fecha._a_dias_totales()
        return abs(dias_self - dias_otra)   
    def _a_dias_totales(self):
        # Método privado: convierte fecha a días totales desde año 0 ; Para cálculo simplificado de diferencia
        dias = self.dia
        dias_por_mes = [31, 29 if self.es_bisiesto() else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # Suma días de meses anteriores
        for i in range(self.mes - 1):
            dias += dias_por_mes[i]  
        # Suma días de años anteriores 
        dias += self.año * 365      
        return dias

# EJEMPLOS DE USO
fecha1 = Fecha(15, 3, 2023)
fecha2 = Fecha(20, 3, 2023)
fecha3 = Fecha(29, 2, 2020)  # Año bisiesto
fecha4 = Fecha(29, 2, 2023)  # Fecha inválida
print(f"Fecha 1 válida: {fecha1.es_valida()}")
print(f"Fecha 3 válida: {fecha3.es_valida()}")
print(f"Fecha 4 válida: {fecha4.es_valida()}")
print(f"¿2020 es bisiesto?: {fecha3.es_bisiesto()}")
print(f"¿2023 es bisiesto?: {fecha1.es_bisiesto()}")
print(f"¿Fecha 1 es anterior a Fecha 2?: {fecha1.es_anterior(fecha2)}")
print(f"Días entre Fecha 1 y Fecha 2: {fecha1.dias_entre(fecha2)}")


