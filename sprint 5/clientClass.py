from scriptDB import agregarCliente
from scriptDB import generarNumeroCliente

class Client:
    def __init__(self,name,surname,typeclient,dni,transacciones,clientNumber,tCredito,tDebito,cAhorroPesos,cAhorroDolares,cuentaCorriente,cantTCredito,cantTDebito,cantCAhorro,cantCCorriente,cantCInversion,cantChequera,cantLimiteDiario,state):
        if state=="creating":
            self.name = name
            self.surname = surname
            self.numberclient = generarNumeroCliente()
            self.dni = dni
            self.tipo = typeclient
            self.transacciones = [] #historial transacciones
            self.tarjetasDebito = [] #tarjetas de debito adquiridas
            self.cajasAhorroPesos = [] #cajas de ahorro en pesos adquiridas
            self.cuentaCorriente = [] #cuentas corrientes adquiridas
            self.cajasAhorroDolares = [] #cajas de ahorro en dolares adquiridas
            self.tarjetasCredito = [] #tarjetas de credito adquiridas
            self.currentCantTarjetaCredito = 0 #cantidad actual de tarjetas de credito
            self.currentCantTarjetaDebito = 0 #cantidad actual de tarjetas de debito
            self.currentCantCajaAhorro = 0 #cantidad actual de cajas de ahorro
            self.currentCantCuentaCorriente = 0 #cantidad actual de cuentas corrientes
            self.currentCantCuentaInversion = 0 #cantidad actual de cuentas de inversiones
            self.currentCantChequera = 0 #cantidad actual de chequeras
            self.currentLimiteDiario = 0 #Limite diario restante
            self.crearCliente() #creacion del perfil
        else:
            self.name = name
            self.surname = surname
            self.numberclient = clientNumber
            self.dni = dni
            self.tipo = typeclient
            self.transacciones = transacciones
            self.tarjetasDebito = tDebito
            self.cajasAhorroPesos = cAhorroPesos
            self.cuentaCorriente = cuentaCorriente
            self.cajasAhorroDolares = cAhorroDolares
            self.tarjetasCredito = tCredito
            self.currentCantTarjetaCredito = cantTCredito
            self.currentCantTarjetaDebito = cantTDebito
            self.currentCantCajaAhorro = cantCAhorro
            self.currentCantCuentaCorriente = cantCCorriente
            self.currentCantCuentaInversion = cantCInversion
            self.currentCantChequera = cantChequera
            self.currentLimiteDiario = cantLimiteDiario

    #crear cliente en base de datos
    def crearCliente(self):
        agregarCliente(self.getName(),self.getSurname(),self.getTypeClient(),self.getDni(),self.getNumberClient(),self.getTarjetasCredito(),self.getTarjetasDebito(),self.getCajaAhorroPesos(),self.getCajaAhorroDolar(),self.getCuentaCorriente(),self.getCantTCredito(),self.getCantTDebito(),self.getCantCajaAhorro(),self.getCantCuentaCorriente(),self.getCantCuentaInversion(),self.getCantChequera(),self.getCurrentLimiteDiario())
    
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
        return (self.getLimiteDiario()-self.getCurrentLimiteDiario())
    
    def getTransacciones(self):
        return self.transacciones[1:]
    def getTarjetasDebito(self):
        return self.tarjetasDebito
    def getCajaAhorroPesos(self):
        return self.cajasAhorroPesos
    def getCuentaCorriente(self):
        return self.cuentaCorriente
    def getCajaAhorroDolar(self):
        return self.cajasAhorroDolares
    def getTarjetasCredito(self):
        return self.tarjetasCredito
    #cambio de informacion///////////////////
    def setCantTCredito(self,cant):
        self.currentCantTarjetaCredito = cant
    def setCantTDebito(self,cant):
        self.currentCantTarjetaDebito = cant
    def setCantCajaAhorro(self,cant):
        self.currentCantCajaAhorro = cant
    def setCantCuentaCorriente(self,cant):
        self.currentCantCuentaCorriente = cant
    def setCantCuentaInversion(self,cant):
        self.currentCantCuentaInversion = cant
    def setCantChequera(self,cant):
        self.currentCantChequera = cant

    def setCurrentLimiteDiario(self,cant):
        self.currentLimiteDiario = cant
    
    def __str__(self):
        return ("Nombre:{}\nApellido:{}\nTipo:{}\nNumero de cliente:{}\nDNI:{}".format(self.getName(),self.getSurname(),self.getTypeClient(),self.getNumberClient(),self.getDni()))

    #retiro de efectivo
    def realizarRetiroEfectivo(self, cuenta, monto):
        if cuenta == "Caja de ahorro en pesos":
            if monto <= 10000:  # Se verifica el límite diario de retiro
                if self.cajaAhorroPesos.getSaldo() >= monto:
                    self.cajaAhorroPesos.saldo -= monto
                    print("Retiro de efectivo exitoso.")
                else:
                    print("Fondos insuficientes en la cuenta seleccionada.")
            else:
                print("El monto excede el límite diario de retiro.")
        elif cuenta == "Caja de ahorro en dólares":
            if monto <= 10000:  # Se verifica el límite diario de retiro
                if self.cajaAhorroDolares.getSaldo() >= monto:
                    self.cajaAhorroDolares.saldo -= monto
                    print("Retiro de dólares exitoso.")
                else:
                    print("Fondos insuficientes en la cuenta seleccionada.")
            else:
                print("El monto excede el límite diario de retiro en dólares.")
        else:
            print("Cuenta no válida.")

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
    def realizarTransferenciaSaliente(self, monto):
        comision = monto * 0.01  # Comisión del 1% por transferencias salientes
        totalTransferencia = monto + comision
        if totalTransferencia <= self.cajaAhorroPesos.getSaldo():
            self.cajaAhorroPesos.saldo -= totalTransferencia
            print("Transferencia saliente exitosa.")
        else:
            print("Fondos insuficientes para realizar la transferencia.")

    #realizar transferencia de ingreso
    def realizarTransferenciaEntrante(self, monto):
        comision = monto * 0.005  # Comisión del 0.5% por transferencias entrantes
        totalTransferencia = monto - comision
        self.cajaAhorroPesos.saldo += totalTransferencia
        print("Transferencia entrante exitosa.")

    #Verificacion de tenencia de chequera
    def solicitarChequera(self):
        if self.chequera:
            print("Ya tiene una chequera.")
        else:
            self.chequera = True
            print("Chequera solicitada con éxito.")



class ClienteClassic(Client):
    def __init__(self,name,surname,dni,transacciones,clientNumber,tCredito,tDebito,cAhorroPesos,cAhorroDolares,cuentaCorriente,cantTCredito,cantTDebito,cantCAhorro,cantCCorriente,cantCInversion,cantChequera,cantLimiteDiario,state):
        super().__init__(name,surname,"Classic",dni,transacciones,clientNumber,tCredito,tDebito,cAhorroPesos,cAhorroDolares,cuentaCorriente,cantTCredito,cantTDebito,cantCAhorro,cantCCorriente,cantCInversion,cantChequera,cantLimiteDiario,state)
        self.cargoMensualCajaDolares = 10  # Cargo mensual por caja de ahorro en dólares
        self.limiteTransaccionTotal = 10000
        self.limiteTransaccionCuota = 10000
        self.limiteDiario = 10000
        self.retiroSinComision = 5
        self.comisionSaliente = 1
        self.comisionEntrante = 0.5
        self.limiteTarjetaDebito = 1
        self.limiteTarjetaCredito = 0
        self.limiteCajaAhorroPeso = 1
        self.limiteCajaAhorroDolar = 1
        self.limiteCuentaCorrientePeso = 0
        self.limiteCuentaCorrienteDolar = 0
        self.limiteCuentaInversion = 0
        self.limiteChequera = 0



class ClienteGold(Client):
    def __init__(self,name,surname,dni,transacciones,clientNumber,tCredito,tDebito,cAhorroPesos,cAhorroDolares,cuentaCorriente,cantTCredito,cantTDebito,cantCAhorro,cantCCorriente,cantCInversion,cantChequera,cantLimiteDiario,state):
        super().__init__(name,surname,"Gold",dni,transacciones,clientNumber,tCredito,tDebito,cAhorroPesos,cAhorroDolares,cuentaCorriente,cantTCredito,cantTDebito,cantCAhorro,cantCCorriente,cantCInversion,cantChequera,cantLimiteDiario,state)
        self.cargoMensualCajaDolares = 0  # Cargo mensual por caja de ahorro en dólares
        self.limiteTransaccionTotal = 150000
        self.limiteTransaccionCuota = 100000
        self.limiteDiario = 20000
        self.comisionSaliente = 1
        self.comisionEntrante = 0.5
        self.limiteTarjetaDebito = 1
        self.limiteTarjetaCredito = 2
        self.limiteExtensiones = 5
        self.limiteCajaAhorroPeso = 2
        self.limiteCajaAhorroDolar = 2
        self.limiteCuentaCorrientePeso = 1
        self.limiteCuentaCorrienteDolar = 1
        self.limiteCuentaInversion = 1 
        self.limiteChequera = 1


    
class ClienteBlack(Client):
    def __init__(self,name,surname,dni,transacciones,clientNumber,tCredito,tDebito,cAhorroPesos,cAhorroDolares,cuentaCorriente,cantTCredito,cantTDebito,cantCAhorro,cantCCorriente,cantCInversion,cantChequera,cantLimiteDiario,state):
        super().__init__(name,surname,"Black",dni,transacciones,clientNumber,tCredito,tDebito,cAhorroPesos,cAhorroDolares,cuentaCorriente,cantTCredito,cantTDebito,cantCAhorro,cantCCorriente,cantCInversion,cantChequera,cantLimiteDiario,state)
        self.cargoMensualCajaDolares = 0  # Cargo mensual por caja de ahorro en dólares
        self.limiteTransaccionTotal = 500000
        self.limiteTransaccionCuota = 600000
        self.limiteDiario = 100000
        self.comisionSaliente = 0
        self.comisionEntrante = 0
        self.limiteTarjetaDebito = 5
        self.limiteTarjetaCredito = 0
        self.limiteExtensiones = 5
        self.limiteCajaAhorroPeso = 5
        self.limiteCajaAhorroDolar = 5
        self.limiteCantCuentaCorriente = 3
        self.limiteCuentaInversion = 1
        self.limiteChequera = 2