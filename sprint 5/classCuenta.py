import random


#Clase cuenta//////////////////////////////////////////////////////////
class Cuenta:

  def __init__(self, tipoCuenta):
    self.numeroCuenta = random.randint(10000, 99999)
    self.saldo = 0
    self.tipoCuenta = tipoCuenta

    if tipoCuenta == "Caja ahorro pesos" or tipoCuenta == "Cuenta corriente en pesos" or tipoCuenta == "Cuenta inversion" or tipoCuenta == "Chequera":
      self.moneda = "Pesos"
    else:
      self.moneda = "Dolar"

  def __str__(self):
    texto = "Tipo de cuenta:" + self.getTipoCuenta(
    ) + "\nNumero de cuenta:" + str(self.getNumeroCuenta()) + "\nSaldo:" + str(
        self.getSaldo()) + "\nMoneda:" + self.getMoneda(
        ) + "\n/////////////////////////////"
    return texto

  def getNumeroCuenta(self):
    return self.numeroCuenta

  def getSaldo(self):
    return self.saldo

  def getMoneda(self):
    return self.moneda

  def setSaldo(self, monto):
    self.saldo = monto

  def getTipoCuenta(self):
    return self.tipoCuenta
