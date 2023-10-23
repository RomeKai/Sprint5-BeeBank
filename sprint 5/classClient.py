import random
import os
from classCard import Tarjeta
from classCuenta import Cuenta


class Client:

  def __init__(self, name, surname, typeclient, dni, limiteTransaccionTotal,
               limiteTransaccionCuota):
    self.name = name
    self.surname = surname
    self.numberclient = random.randint(100000000000000000000,
                                       999999999999999999999)
    self.dni = dni
    self.tipo = typeclient
    self.transacciones = []  #historial transacciones
    self.tarjetasDebito = []  #tarjetas de debito adquiridas
    self.cajasAhorroPesos = []  #cajas de ahorro en pesos adquiridas
    self.cajasAhorroDolares = []  #cajas de ahorro en dolares adquiridas
    self.cuentaCorrientePesos = []  #cuentas corrientes adquiridas
    self.cuentaCorrienteDolar = []  #cuentas corrientes adquiridas
    self.tarjetasCredito = []  #tarjetas de credito adquiridas
    self.cuentaInversion = []  #cuenta inversion adquiridas
    self.chequera = []  #chequeras adquiridas
    self.currentCantTarjetaCredito = 0  #cantidad actual de tarjetas de credito
    self.currentCantTarjetaDebito = 0  #cantidad actual de tarjetas de debito
    self.currentCantCajaAhorro = 0  #cantidad actual de cajas de ahorro
    self.currentCantCuentaCorriente = 0  #cantidad actual de cuentas corrientes
    self.currentCantCuentaInversion = 0  #cantidad actual de cuentas de inversiones
    self.currentCantChequera = 0  #cantidad actual de chequeras
    self.currentLimiteDiario = 0  #Limite diario restante
    self.limiteTransaccionTotal = limiteTransaccionTotal
    self.limiteTransaccionCuota = limiteTransaccionCuota
    self.cargoAdicionalCuentas = 100  #cargo por cuentas adicionales

  def __str__(self):
    return (
        "Nombre:{}\nApellido:{}\nTipo:{}\nNumero de cliente:{}\nDNI:{}".format(
            self.getName(), self.getSurname(), self.getTypeClient(),
            self.getNumberClient(), self.getDni()))

  #extractores de datos////////////////////
  def getCantTCredito(self):
    return self.currentCantTarjetaCredito

  def getCantTDebito(self):
    return self.currentCantTarjetaDebito

  def getCantCajaAhorro(self):
    return self.currentCantCajaAhorro

  def getCantCuentaCorriente(self):
    return self.currentCantCuentaCorriente

  def getCantCuentaInversion(self):
    return self.currentCantCuentaInversion

  def getCantChequera(self):
    return self.currentCantChequera

  def getCargoAdicionalCuentas(self):
    return self.cargoAdicionalCuentas

  def getCurrentLimiteDiario(self):
    return self.currentLimiteDiario

  def getLimiteDiario(self):
    return self.limiteDiario

  def getDni(self):
    return self.dni

  def getName(self):
    return self.name

  def getSurname(self):
    return self.surname

  def getTypeClient(self):
    return self.tipo

  def getNumberClient(self):
    return self.numberclient

  def getLimiteTotal(self):
    return self.limiteTransaccionTotal

  def getLimiteCuota(self):
    return self.limiteTransaccionCuota

  def getLimiteDiarioRestante(self):
    return (self.getLimiteDiario() - self.getCurrentLimiteDiario())

  def getTarjetasDebito(self):
    return self.tarjetasDebito

  def getCajaAhorroPesos(self):
    return self.cajasAhorroPesos

  def getCuentaCorrientePesos(self):
    return self.cuentaCorrientePesos

  def getCuentaCorrienteDolar(self):
    return self.cuentaCorrienteDolar

  def getCajaAhorroDolar(self):
    return self.cajasAhorroDolares

  def getTarjetasCredito(self):
    return self.tarjetasCredito

  def getLimiteTransaccionTotal(self):
    return self.limiteTransaccionTotal

  def getLimiteTransaccionCuota(self):
    return self.limiteTransaccionCuota

  def getCuentaInversion(self):
    return self.cuentaInversion

  def getChequera(self):
    return self.chequera

  def getNumeroCuenta(self):
    return self.numberclient

  def getTransacciones(self):
    return self.transacciones

  #cambio de informacion///////////////////
  def setCantTCredito(self, cant):
    self.currentCantTarjetaCredito = cant

  def setCantTDebito(self, cant):
    self.currentCantTarjetaDebito = cant

  def setCantCajaAhorro(self, cant):
    self.currentCantCajaAhorro = cant

  def setCantCuentaCorriente(self, cant):
    self.currentCantCuentaCorriente = cant

  def setCantCuentaInversion(self, cant):
    self.currentCantCuentaInversion = cant

  def setCantChequera(self, cant):
    self.currentCantChequera = cant

  def setTransacciones(self, elemento):
    lista = self.getTransacciones()
    lista.append(elemento)
    self.transacciones = lista

  def setTarjetasDebito(self, elemento):
    lista = self.getTarjetasDebito()
    lista.append(elemento)
    self.tarjetasDebito = lista

  def setCajaAhorroPesos(self, elemento):
    lista = self.getCajaAhorroPesos()
    lista.append(elemento)
    self.cajasAhorroPesos = lista

  def setCuentaCorrientePesos(self, elemento):
    lista = self.getCuentaCorrientePesos()
    lista.append(elemento)
    self.cuentaCorrientePesos = lista

  def setCuentaCorrienteDolar(self, elemento):
    lista = self.getCuentaCorrienteDolar()
    lista.append(elemento)
    self.cuentaCorrienteDolar = lista

  def setCajaAhorroDolar(self, elemento):
    lista = self.getCajaAhorroDolar()
    lista.append(elemento)
    self.cajasAhorroDolares = lista

  def setTarjetasCredito(self, elemento):
    lista = self.getTarjetasCredito()
    lista.append(elemento)
    self.tarjetasCredito = lista

  def setCuentaInversion(self, elemento):
    lista = self.getCuentaInversion()
    lista.append(elemento)
    self.cuentaInversion = lista

  def setChequera(self, elemento):
    lista = self.getChequera()
    lista.append(elemento)
    self.chequera = lista

  def setCurrentLimiteDiario(self, cant):
    self.currentLimiteDiario = cant

  #creacion de cuentas:
  def crearCuenta(self, tipoCuenta, foundClient):
    newCuenta = Cuenta(tipoCuenta)
    if tipoCuenta == "Caja ahorro pesos":
      if self.getCantCajaAhorro() < foundClient.getLimiteCajaAhorroPeso():
        self.setCajaAhorroPesos(newCuenta)
        self.setCantCajaAhorro(self.getCantCajaAhorro() + 1)
      else:
        if self.getTypeClient == "Classic":
          print("Se alcanzó el maximo de cajas de ahorro en pesos...")
        else:
          saldo = self.getCajaAhorroPesos()
          saldo = saldo[0]
          saldo = saldo.getSaldo()
          if saldo - self.getCargoAdicionalCuentas() < 0:
            print(
                "Saldo en caja de ahorro principal insuficiente para abrir otra cuenta..."
            )
          else:
            self.setCajaAhorroPesos(newCuenta)
            self.setCantCajaAhorro(self.getCantCajaAhorro() + 1)

    elif tipoCuenta == "Caja ahorro dolares":
      if self.getCantCajaAhorro() < foundClient.getLimiteCajaAhorroDolar():
        self.setCajaAhorroDolar(newCuenta)
        self.setCantCajaAhorro(self.getCantCajaAhorro() + 1)
      else:
        if self.getTypeClient() == "Classic":
          print("Se alcanzó el maximo de cajas de ahorro en dolares...")
        else:
          saldo = self.getCajaAhorroPesos()
          saldo = saldo[0]
          saldo = saldo.getSaldo()
          if saldo - self.getCargoAdicionalCuentas() < 0:
            print(
                "Saldo en caja de ahorro principal insuficiente para abrir otra cuenta..."
            )
          else:
            self.setCajaAhorroDolar(newCuenta)
            self.setCantCajaAhorro(self.getCantCajaAhorro() + 1)
    elif tipoCuenta == "Cuenta corriente en pesos" or tipoCuenta == "Cuenta corriente dolar":
      if self.getCantCuentaCorriente() < foundClient.getLimiteCuentaCorriente(
      ):
        self.setCuentaCorrientePesos(newCuenta)
        self.setCantCuentaCorriente(self.getCantCuentaCorriente() + 1)
      else:
        saldo = self.getCajaAhorroPesos()
        saldo = saldo[0]
        saldo = saldo.getSaldo()
        if saldo - self.getCargoAdicionalCuentas() < 0:
          print(
              "Saldo en caja de ahorro principal insuficiente para abrir otra cuenta..."
          )
        else:
          self.setCuentaCorrientePesos(newCuenta)
          self.setCantCuentaCorriente(self.getCantCuentaCorriente() + 1)
    elif tipoCuenta == "Cuenta corriente en dolares" or tipoCuenta == "Cuenta corriente dolar":
      if self.getCantCuentaCorriente() < foundClient.getLimiteCuentaCorriente(
      ):
        self.setCuentaCorrienteDolar(newCuenta)
        self.setCantCuentaCorriente(self.getCantCuentaCorriente() + 1)
      else:
        saldo = self.getCajaAhorroPesos()
        saldo = saldo[0]
        saldo = saldo.getSaldo()
        if saldo - self.getCargoAdicionalCuentas() < 0:
          print(
              "Saldo en caja de ahorro principal insuficiente para abrir otra cuenta..."
          )
        else:
          self.setCuentaCorrienteDolar(newCuenta)
          self.setCantCuentaCorriente(self.getCantCuentaCorriente() + 1)
    elif tipoCuenta == "Cuenta inversion":
      if self.getCantCuentaInversion() < foundClient.getLimiteCuentaInversion(
      ):
        self.setCuentaInversion(newCuenta)
        self.setCantCuentaInversion(self.getCantCuentaInversion() + 1)
      else:
        saldo = self.getCajaAhorroPesos()
        saldo = saldo[0]
        saldo = saldo.getSaldo()
        if saldo - self.getCargoAdicionalCuentas() < 0:
          print(
              "Saldo en caja de ahorro principal insuficiente para abrir otra cuenta..."
          )
        else:
          self.setCuentaInversion(newCuenta)
          self.setCantCuentaInversion(self.getCantCuentaInversion() + 1)
    elif tipoCuenta == "Chequera":
      if self.getCantChequera() < foundClient.getLimiteChequera():
        self.setChequera(newCuenta)
        self.setCantChequera(self.getCantChequera() + 1)
      else:
        saldo = self.getCajaAhorroPesos()
        saldo = saldo[0]
        saldo = saldo.getSaldo()
        if saldo - self.getCargoAdicionalCuentas() < 0:
          print(
              "Saldo en caja de ahorro principal insuficiente para abrir otra cuenta..."
          )
        else:
          self.setChequera(newCuenta)
          self.setCantChequera(self.getCantChequera() + 1)

  #creacion de tarjetas
  #tipo_tarjeta,brand_tarjeta,limiteTotal_tarjeta,limiteCuota_tarjeta
  def crearTarjeta(self, tipoTarjeta, brandTarjeta):
    newTarjeta = Tarjeta(tipoTarjeta, brandTarjeta,
                         self.getLimiteTransaccionTotal(),
                         self.getLimiteTransaccionCuota())
    if tipoTarjeta == "Debito":
      self.setTarjetasDebito(newTarjeta)
      self.setCantTDebito(self.getCantTDebito() + 1)
    else:
      self.setTarjetasCredito(newTarjeta)
      self.setCantTCredito(self.getCantTCredito() + 1)
    os.system("cls")
    print("Tarjeta Creada...")
    print(newTarjeta)

  #retiro de efectivo
  def realizarRetiroEfectivo(self, foundClient, cuenta, monto):
    if cuenta == "Caja de ahorro en pesos":
      if monto <= foundClient.getLimiteDiario(
      ):  # Se verifica el límite diario de retiro
        cajas = foundClient.getCajaAhorroPesos()
        cajaPrincipal = cajas[0]
        if cajaPrincipal.getSaldo() >= monto:
          cajaPrincipal.setSaldo(cajaPrincipal.getSaldo() - monto)
          print("Retiro de efectivo exitoso.")
        else:
          print("Fondos insuficientes en la cuenta seleccionada.")
      else:
        print("El monto excede el límite diario de retiro.")
    elif cuenta == "Caja de ahorro en dolares":
      if monto <= foundClient.getLimiteDiario(
      ):  # Se verifica el límite diario de retiro
        cajas = foundClient.getCajaAhorroDolar()
        cajaPrincipal = cajas[0]
        if cajaPrincipal.getSaldo() >= monto:
          cajaPrincipal.setSaldo(cajaPrincipal.getSaldo() - monto)
          print("Retiro de efectivo exitoso.")
        else:
          print("Fondos insuficientes en la cuenta seleccionada.")
      else:
        print("El monto excede el límite diario de retiro en dólares.")
    else:
      print("Cuenta no válida.")

  def ingresoDinero(self, foundClient, tipo, monto):
    if tipo == "Pesos":
      cajas = foundClient.getCajaAhorroPesos()
      cajaPrincipal = cajas[0]
      cajaPrincipal.setSaldo(cajaPrincipal.getSaldo() + monto)
    elif tipo == "Dolar":
      cajas = foundClient.getCajaAhorroDolar()
      cajaPrincipal = cajas[0]
      cajaPrincipal.setSaldo(cajaPrincipal.getSaldo() + monto)

  #obtener tarjetas edel cliente
  def obtenertarjetasDebito(self):
    return [tarjeta.numeroTarjeta for tarjeta in self.tarjetasDebito]

  #obtener cuentas disponibles
  def obtenerCuentasDisponibles(self):
    cuentas = ["Caja de ahorro en pesos"]
    if self.cajaAhorroDolares.getSaldo() > 0:
      cuentas.append("Caja de ahorro en dólares")
    return cuentas

  #realizar transferencia
  def realizarTransferenciaSaliente(self, foundClient, monto, fecha, cuenta,
                                    permitidoActual, numero, estado):
    comision = monto * 0.05  # Comisión del 1% por transferencias salientes
    totalTransferencia = monto + comision
    cajas = foundClient.getCajaAhorroPesos()
    numero = len(foundClient.getTransacciones()) + 1
    if len(cajas) > 0:
      cajaPrincipal = cajas[0]
      if totalTransferencia <= cajaPrincipal.getSaldo():
        cajaPrincipal.setSaldo(cajaPrincipal.getSaldo() - totalTransferencia)
        nuevaTransaccion = [
            monto, fecha, cuenta, permitidoActual, numero, estado
        ]
        if len(foundClient.getTransacciones()) == 0:
          foundClient.setTransacciones(nuevaTransaccion)
        else:
          foundClient.getTransacciones().append(nuevaTransaccion)
        print("Transferencia saliente exitosa.")
      else:
        print("Fondos insuficientes para realizar la transferencia.")
    else:
      print("No hay cuentas disponibles")

  #realizar transferencia de ingreso
  def realizarTransferenciaEntrante(self, foundClient, monto, fecha, cuenta,
                                    permitidoActual, numero, estado):
    comision = monto * 0.01  # Comisión del 0.5% por transferencias entrantes
    totalTransferencia = monto + comision
    fechaAct = fecha
    cuentaAct = cuenta
    permitido = permitidoActual
    numeroAct = numero
    estadoAct = estado
    numero = len(foundClient.getTransacciones()) + 1
    cajas = foundClient.getCajaAhorroPesos()
    if len(cajas) > 0:
      cajaPrincipal = cajas[0]
      cajaPrincipal.setSaldo(cajaPrincipal.getSaldo() + totalTransferencia)
      nuevaTransaccion = [
          monto, fecha, cuenta, permitidoActual, numero, estado
      ]
      if len(foundClient.getTransacciones()) == 0:
        foundClient.setTransacciones(nuevaTransaccion)
      else:
        foundClient.getTransacciones().append(nuevaTransaccion)
      print("Transferencia entrante exitosa.")
    else:
      print("No hay cajas disponibles..")

  #Verificacion de tenencia de chequera
  def solicitarChequera(self):
    if self.chequera:
      print("Ya tiene una chequera.")
    else:
      self.chequera = True
      print("Chequera solicitada con éxito.")

  def comprarDolar(self, foundClient, monto):
            def comprarDolar(self, foundClient, monto):
              dolar = 1500
              cuentasDolares = self.getCajaAhorroDolar()
              if cuentasDolares:
                  print("Cuentas en dólares disponibles:")
                  for idx, cuenta in enumerate(cuentasDolares):
                      print(f"{idx}. {cuenta}")  

                  opc = input("Ingrese el índice de la cuenta en dólares deseada: ")
                  try:
                      opc = int(opc)
                      if 0 <= opc < len(cuentasDolares):
                          cuentaDolares = cuentasDolares[opc]
                          if monto > 0 and monto <= self.getCurrentLimiteDiario():
                              cajas = foundClient.getCajaAhorroPesos()
                              caja = cajas[opc]
                              if caja.getSaldo() >= monto:
                                  caja.saldo -= monto  
                                  saldoActualDolares = cuentaDolares.getSaldo()
                                  nuevoSaldo = monto / dolar
                                  cuentaDolares.setSaldo(saldoActualDolares + nuevoSaldo)
                                  print(f"Compra de dólares por {monto} realizada con éxito.")
                              else:
                                  print("Fondos insuficientes en la cuenta en dólares.")
                          else:
                              print("Monto inválido o excede el límite diario.")
                      else:
                          print("Índice de cuenta en dólares inválido.")
                  except ValueError:
                      print("Por favor, ingrese un número válido como índice.")
              else:
                  print("No existe una cuenta en dólares asociada a esta cuenta en pesos.")
    
  def venderDolar(self, foundClient, monto):
    dolar = 1500
    cuentasDolares = self.getCajaAhorroDolar()
    if cuentasDolares:
        print("Cuentas en dólares disponibles:")
        for idx, cuenta in enumerate(cuentasDolares):
            print(f"{idx}. {cuenta}")  
  
        opc = input("Ingrese el índice de la cuenta en dólares desde la cual desea vender: ")
        try:
            opc = int(opc)
            if 0 <= opc < len(cuentasDolares):
                cuentaDolares = cuentasDolares[opc]
                saldoActualDolares = cuentaDolares.getSaldo()
                if monto > 0 and monto <= saldoActualDolares:
                    cajas = foundClient.getCajaAhorroPesos()
                    caja = cajas[opc]
                    nuevoSaldoPesos = monto * dolar
                    caja.saldo += nuevoSaldoPesos  
                    cuentaDolares.setSaldo(saldoActualDolares - monto)
                    print(f"Venta de {monto} dólares realizada con éxito.")
                else:
                    print("Monto inválido o excede el saldo en dólares de la cuenta seleccionada.")
            else:
                print("Índice de cuenta en dólares inválido.")
        except ValueError:
            print("Por favor, ingrese un número válido como índice.")
    else:
        print("No existe una cuenta en dólares asociada a esta cuenta en pesos.")





class ClienteClassic(Client):

  def __init__(self, name, surname, dni):
    self.cargoMensualCajaDolares = 10  # Cargo mensual por caja de ahorro en dólares
    self.limiteTransaccionTotal = 10000
    self.limiteTransaccionCuota = 10000
    self.limiteDiario = 10000
    self.retiroSinComision = 5
    self.comisionSaliente = 1
    self.comisionEntrante = 0.5
    self.limiteTarjetaDebito = 1
    self.limiteCajaAhorroPeso = 1
    self.limiteCajaAhorroDolar = 1
    super().__init__(name, surname, "Classic", dni,
                     self.limiteTransaccionTotal, self.limiteTransaccionCuota)

  def getLimiteTarjetaDebito(self):
    return self.limiteTarjetaDebito

  def getLimiteCajaAhorroPeso(self):
    return self.limiteCajaAhorroPeso

  def getLimiteCajaAhorroDolar(self):
    return self.limiteCajaAhorroDolar


class ClienteGold(Client):

  def __init__(self, name, surname, dni):
    self.cargoMensualCajaDolares = 0  # Cargo mensual por caja de ahorro en dólares
    self.limiteTransaccionTotal = 150000
    self.limiteTransaccionCuota = 100000
    self.limiteDiario = 20000
    self.comisionSaliente = 1
    self.comisionEntrante = 0.5
    self.limiteTarjetaDebito = 1
    self.limiteCajaAhorroPeso = 2
    self.limiteCajaAhorroDolar = 2
    self.limiteCuentaCorriente = 1
    self.limiteCuentaInversion = 1
    self.limiteChequera = 1
    super().__init__(name, surname, "Gold", dni, self.limiteTransaccionTotal,
                     self.limiteTransaccionCuota)

  def getLimiteTarjetaDebito(self):
    return self.limiteTarjetaDebito

  def getLimiteCajaAhorroPeso(self):
    return self.limiteCajaAhorroPeso

  def getLimiteCajaAhorroDolar(self):
    return self.limiteCajaAhorroDolar

  def getLimiteCuentaCorriente(self):
    return self.limiteCuentaCorriente

  def getLimiteCuentaInversion(self):
    return self.limiteCuentaInversion

  def getLimiteChequera(self):
    return self.limiteChequera


class ClienteBlack(Client):

  def __init__(self, name, surname, dni):
    self.cargoMensualCajaDolares = 0  # Cargo mensual por caja de ahorro en dólares
    self.limiteTransaccionTotal = 500000
    self.limiteTransaccionCuota = 600000
    self.limiteDiario = 100000
    self.comisionSaliente = 0
    self.comisionEntrante = 0
    self.limiteTarjetaDebito = 5
    self.limiteCajaAhorroPeso = 5
    self.limiteCajaAhorroDolar = 5
    self.limiteCantCuentaCorriente = 3
    self.limiteCuentaInversion = 1
    self.limiteChequera = 2
    super().__init__(name, surname, "Black", dni, self.limiteTransaccionTotal,
                     self.limiteTransaccionCuota)

  def getLimiteTarjetaDebito(self):
    return self.limiteTarjetaDebito

  def getLimiteCajaAhorroPeso(self):
    return self.limiteCajaAhorroPeso

  def getLimiteCajaAhorroDolar(self):
    return self.limiteCajaAhorroDolar

  def getLimiteCantCuentaCorriente(self):
    return self.limiteCantCuentaCorriente

  def getLimiteCuentaInversion(self):
    return self.limiteCuentaInversion

  def getLimiteChequera(self):
    return self.limiteChequera
