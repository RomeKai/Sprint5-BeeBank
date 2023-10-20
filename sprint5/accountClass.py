#Clase cuenta//////////////////////////////////////////////////////////
class Cuenta:
    def __init__(self, numero_cuenta, saldo):
        self.numeroCuenta = numero_cuenta
        self.saldo = saldo

    def getSaldo(self):
        return self.saldo
    
    def setSaldo(self,monto):
        self.saldo = monto

#Clase cuenta de ahorro en pesos///////////////////////////////////////
class CuentaAhorroPeso(Cuenta):
    def __init__(self, numero_cuenta, saldo):
        super().__init__(numero_cuenta, saldo)
        self.moneda = "Peso"

#Clase cuenta de ahorro en dolar///////////////////////////////////////
class CuentaAhorroDolar(Cuenta):
    def __init__(self, numero_cuenta, saldo):
        super().__init__(numero_cuenta, saldo)
        self.moneda = "Dólar"

#Clase cuenta corriente en pesos///////////////////////////////////////
class CuentaCorrientePeso(Cuenta):
    def __init__(self, numero_cuenta, saldo):
        super().__init__(numero_cuenta, saldo)
        self.moneda = "Peso"

#Clase cuenta corriente en dolar///////////////////////////////////////
class CuentaCorrienteDolar(Cuenta):
    def __init__(self, numero_cuenta, saldo):
        super().__init__(numero_cuenta, saldo)
        self.moneda = "Dólar"

#Clase cuenta de inversion/////////////////////////////////////////////
class CuentaInversion(Cuenta):
    def __init__(self, numero_cuenta, saldo):
        super().__init__(numero_cuenta, saldo)
        self.moneda = "Peso"  # Se asume que las cuentas de inversión están en pesos