class CuentaBancaria:
    def __init__(self, numero_cuenta, titular, saldo_inicial=0):
        # Constructor: inicializa los datos de la cuenta
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.saldo = saldo_inicial  # Saldo inicial de la cuenta
    def depositar(self, monto):
        # Suma el monto al saldo actual 
        self.saldo += monto
    def retirar(self, monto):
        # Verifica si hay suficiente saldo antes de retirar
        # Si monto <= saldo: resta y retorna True (éxito)
        # Si monto > saldo: no resta y retorna False (fallo)
        if monto <= self.saldo:
            self.saldo -= monto
            return True
        return False
    def consultar_saldo(self):
        # Devuelve el saldo actual de la cuenta
        return self.saldo
    def obtener_titular(self):
        # Devuelve el nombre del titular de la cuenta
        return self.titular

# EJEMPLOS DE USO
# Crear cuenta bancaria
cuenta = CuentaBancaria("123456", "Derick Pazmiño", 100)
print(f"Titular: {cuenta.obtener_titular()}")
print(f"Saldo inicial: {cuenta.consultar_saldo()}")
# Depositar 50
cuenta.depositar(50)
print(f"Saldo después de depositar 50: {cuenta.consultar_saldo()}")
# Intentar retirar 200 (no hay suficiente saldo)
resultado = cuenta.retirar(200)
print(f"¿Retiro exitoso de 200?: {resultado}")
print(f"Saldo actual: {cuenta.consultar_saldo()}")
# Retirar 80 (sí hay suficiente saldo)
resultado = cuenta.retirar(80)
print(f"¿Retiro exitoso de 80?: {resultado}")
print(f"Saldo final: {cuenta.consultar_saldo()}")


