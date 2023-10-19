from abc import ABC, abstractmethod

#Clases base abstractas no instanciables Cliente,Cuenta y tarjeta


class Client:
    def __init__(self, name, surname, typeclient, numberclient, dni):
        self.name = name
        self.surname = surname
        self.typeclient = typeclient
        self.numberclient = numberclient
        self.dni = dni
        self.transacciones = []  # Lista de movimientos

    def __str__(self):
        print("Nombre:{}\nApellido:{},Tipo:{},Numero de cliente:{},DNI:{}".format(self.name,self.surname,self.typeclient,self.numberclient,self.dni))
    """
    @abstractmethod
    def obtener_tarjetas_disponibles(self):
        pass
    
    @abstractmethod
    def obtener_cuentas_disponibles(self):
        pass
    
    @abstractmethod
    def realizar_transferencia(self, monto, destino):
        pass

    @abstractmethod
    def obtener_limite_retiro_diario(self, cuenta):
        pass
    """

class ClienteClassic(Client):
    def __init__(self, name,surname,numberclient,dni):
        super().__init__(name,surname,"Classic",numberclient,dni)
        self.tarjetasDisponibles = [TarjetaDebito(numberclient, 10000)]  # Se crea una tarjeta de débito con un límite inicial de 10000
        self.cajaAhorroPesos = CuentaAhorroPeso(numberclient, 0)  # Saldo inicial en pesos
        self.cajaAhorroDolares = CuentaAhorroDolar(numberclient, 0)  # Saldo inicial en dólares
        self.cargoMensualCajaDolares = 10  # Cargo mensual por caja de ahorro en dólares

    def __str__(self):
        return ("Nombre:{}\nApellido:{}\nTipo:{}\nNumero de cliente:{}\nDNI:{}".format(self.name,self.surname,self.typeclient,self.numberclient,self.dni))
    
    def obtenerTarjetasDisponibles(self):
        return [tarjeta.numeroTarjeta for tarjeta in self.tarjetasDisponibles]

    def obtenerCuentasDisponibles(self):
        cuentas = ["Caja de ahorro en pesos"]
        if self.cajaAhorroDolares.obtenerSaldo() > 0:
            cuentas.append("Caja de ahorro en dólares")
        return cuentas

    def realizarRetiroEfectivo(self, cuenta, monto):
        if cuenta == "Caja de ahorro en pesos":
            if monto <= 10000:  # Se verifica el límite diario de retiro
                if self.cajaAhorroPesos.obtenerSaldo() >= monto:
                    self.cajaAhorroPesos.saldo -= monto
                    print("Retiro de efectivo exitoso.")
                else:
                    print("Fondos insuficientes en la cuenta seleccionada.")
            else:
                print("El monto excede el límite diario de retiro.")
        elif cuenta == "Caja de ahorro en dólares":
            if monto <= 10000:  # Se verifica el límite diario de retiro
                if self.cajaAhorroDolares.obtenerSaldo() >= monto:
                    self.cajaAhorroDolares.saldo -= monto
                    print("Retiro de dólares exitoso.")
                else:
                    print("Fondos insuficientes en la cuenta seleccionada.")
            else:
                print("El monto excede el límite diario de retiro en dólares.")
        else:
            print("Cuenta no válida.")

    def realizarTransferenciaSaliente(self, monto):
        comision = monto * 0.01  # Comisión del 1% por transferencias salientes
        totalTransferencia = monto + comision
        if totalTransferencia <= self.cajaAhorroPesos.obtenerSaldo():
            self.cajaAhorroPesos.saldo -= totalTransferencia
            print("Transferencia saliente exitosa.")
        else:
            print("Fondos insuficientes para realizar la transferencia.")

    def realizarTransferenciaEntrante(self, monto):
        comision = monto * 0.005  # Comisión del 0.5% por transferencias entrantes
        totalTransferencia = monto - comision
        self.cajaAhorroPesos.saldo += totalTransferencia
        print("Transferencia entrante exitosa.")


class ClienteGold(Client):
    def __init__(self, nombre, dni, numeroCliente):
        super().__init__(nombre, dni, "Gold", numeroCliente)
        self.tarjetasDisponibles = [TarjetaDebito(numeroCliente, 20000)]  # Se crea una tarjeta de débito con un límite inicial de 20000
        self.cajasAhorroPesos = [CuentaAhorroPeso(numeroCliente, 0) for _ in range(2)]  # Hasta 2 cajas de ahorro en pesos sin cargo adicional
        self.cuentaCorriente = CuentaCorrientePeso(numeroCliente, 0)  # Una cuenta corriente sin cargo adicional
        self.cajasAhorroDolares = CuentaAhorroDolar(numeroCliente, 0)  # Saldo inicial en dólares
        self.cargoMensualCajaDolares = 10  # Cargo mensual por caja de ahorro en dólares adicionales
        self.tarjetasCredito = {"VISA": TarjetaCredito("VISA", 150000, 100000),
                                "Mastercard": TarjetaCredito("Mastercard", 150000, 100000)}  # Tarjetas VISA y Mastercard con límites
        self.accesoCuentasInversion = True  # Acceso a cuentas de inversión
        self.chequera = True  # Posibilidad de tener una chequera

    def __str__(self):
        return ("Nombre:{}\nApellido:{}\nTipo:{}\nNumero de cliente:{}\nDNI:{}".format(self.name,self.surname,self.typeclient,self.numberclient,self.dni))

    def obtenerTarjetasDisponibles(self):
        return [tarjeta.numeroTarjeta for tarjeta in self.tarjetasDisponibles]

    def obtenerCuentasDisponibles(self):
        cuentas = ["Caja de ahorro en pesos", "Cuenta corriente"]
        if self.cajasAhorroDolares.obtenerSaldo() > 0:
            cuentas.append("Caja de ahorro en dólares")
        return cuentas

    def realizarRetiroEfectivo(self, cuenta, monto):
        if cuenta == "Caja de ahorro en pesos":
            for caja in self.cajasAhorroPesos:
                if monto <= 10000 and caja.obtenerSaldo() >= monto:
                    caja.saldo -= monto
                    print("Retiro de efectivo exitoso.")
                    return
            print("Fondos insuficientes en la cuenta seleccionada o se excede el límite diario de retiro.")
        elif cuenta == "Caja de ahorro en dólares" and monto <= 10000 and self.cajasAhorroDolares.obtenerSaldo() >= monto:
            self.cajasAhorroDolares.saldo -= monto
            print("Retiro de dólares exitoso.")
        elif cuenta == "Cuenta corriente" and monto <= 10000 and self.cuentaCorriente.obtenerSaldo() >= monto:
            self.cuentaCorriente.saldo -= monto
            print("Retiro de cuenta corriente exitoso.")
        else:
            print("Fondos insuficientes en la cuenta seleccionada o se excede el límite diario de retiro.")

    def realizarTransferenciaSaliente(self, monto):
        comision = monto * 0.005  # Comisión del 0.5% por transferencias salientes
        totalTransferencia = monto + comision
        if totalTransferencia <= sum([caja.obtenerSaldo() for caja in self.cajasAhorroPesos]) + self.cuentaCorriente.obtenerSaldo():
            for caja in self.cajasAhorroPesos:
                if totalTransferencia > caja.obtenerSaldo():
                    totalTransferencia -= caja.obtenerSaldo()
                    caja.saldo = 0
                else:
                    caja.saldo -= totalTransferencia
                    print("Transferencia saliente exitosa.")
                    return
            self.cuentaCorriente.saldo -= totalTransferencia
            print("Transferencia saliente exitosa.")
        else:
            print("Fondos insuficientes para realizar la transferencia.")

    def realizarTransferenciaEntrante(self, monto):
        comision = monto * 0.001  # Comisión del 0.1% por transferencias entrantes
        totalTransferencia = monto - comision
        for caja in self.cajasAhorroPesos:
            caja.saldo += totalTransferencia
        print("Transferencia entrante exitosa.")

    def solicitarChequera(self):
        if self.chequera:
            print("Ya tiene una chequera.")
        else:
            self.chequera = True
            print("Chequera solicitada con éxito.")



    

class ClienteBlack(Client):
    def __init__(self, nombre, dni, numeroCliente):
        super().__init__(nombre, dni, "Black", numeroCliente)
        self.nombre = nombre
        self.dni = dni
        self.numeroCliente = numeroCliente
        self.tarjetasDebito = []  # Lista para almacenar tarjetas de débito
        self.cajasAhorroPesos = 0  # Contador para cajas de ahorro en pesos
        self.cajasAhorroDolares = 0  # Contador para cajas de ahorro en dólares
        self.cuentasCorrientes = 0  # Contador para cuentas corrientes
        self.tarjetasCredito = []  # Lista para almacenar tarjetas de crédito
        self.limiteRetiroDiario = 100000  # Límite de retiro diario sin comisiones
        self.transaccionesMensuales = 0  # Contador de transacciones realizadas en el mes

    def __str__(self):
        return ("Nombre:{}\nApellido:{}\nTipo:{}\nNumero de cliente:{}\nDNI:{}".format(self.name,self.surname,self.typeclient,self.numberclient,self.dni))

    def obtenerTarjetasDisponibles(self):
        return len(self.tarjetasDebito) + len(self.tarjetasCredito)

    def obtenerCajasAhorroDisponibles(self):
        return 5 - self.cajasAhorroPesos - self.cajasAhorroDolares

    def obtenerCuentasCorrientesDisponibles(self):
        return 3 - self.cuentasCorrientes

    def obtenerLimiteRetiroDiario(self):
        return self.limiteRetiroDiario

    def realizarRetiro(self, cuenta, monto):
        if cuenta == "CajaAhorroPesos" and self.cajasAhorroPesos > 0:
            self.cajasAhorroPesos -= 1
            return monto
        elif cuenta == "CajaAhorroDolares" and self.cajasAhorroDolares > 0:
            self.cajasAhorroDolares -= 1
            return monto
        elif cuenta == "CuentaCorriente" and self.cuentasCorrientes > 0:
            self.cuentasCorrientes -= 1
            return monto
        else:
            print("Cuenta seleccionada no disponible para retiro.")
            return 0

    def realizarDeposito(self, cuenta, monto):
        if cuenta == "CajaAhorroPesos" and self.cajasAhorroPesos < 5:
            self.cajasAhorroPesos += 1
            return monto
        elif cuenta == "CajaAhorroDolares" and self.cajasAhorroDolares < 5:
            self.cajasAhorroDolares += 1
            return monto
        elif cuenta == "CuentaCorriente" and self.cuentasCorrientes < 3:
            self.cuentasCorrientes += 1
            return monto
        else:
            print("No se pueden agregar más cuentas a la cuenta seleccionada.")
            return 0

    def realizarTransferencia(self, origen, destino, monto):
        if self.transaccionesMensuales < 5:
            if origen == "CajaAhorroPesos" and self.cajasAhorroPesos > 0:
                self.cajasAhorroPesos -= 1
                self.transaccionesMensuales += 1
                return monto
            elif origen == "CajaAhorroDolares" and self.cajasAhorroDolares > 0:
                self.cajasAhorroDolares -= 1
                self.transaccionesMensuales += 1
                return monto
            elif origen == "CuentaCorriente" and self.cuentasCorrientes > 0:
                self.cuentasCorrientes -= 1
                self.transaccionesMensuales += 1
                return monto
            else:
                print("Cuenta de origen no disponible para transferencia.")
                return 0
        else:
            print("Ha alcanzado el límite mensual de transacciones.")
            return 0

    def solicitarChequera(self):
        if self.transaccionesMensuales < 5:
            if self.transaccionesMensuales < 2:
                self.transaccionesMensuales += 1
                return True
            else:
                print("Ha alcanzado el límite mensual de solicitudes de chequera.")
                return False
        else:
            print("Ha alcanzado el límite mensual de transacciones.")
            return False


#----------------------------------------------


class Cuenta(ABC):
    def __init__(self, numero_cuenta, saldo):
        self.numeroCuenta = numero_cuenta
        self.saldo = saldo

    @abstractmethod
    def obtenerSaldo(self):
        pass

class CuentaAhorroPeso(Cuenta):
    def __init__(self, numero_cuenta, saldo):
        super().__init__(numero_cuenta, saldo)
        self.moneda = "Peso"

    def obtenerSaldo(self):
        return self.saldo

class CuentaAhorroDolar(Cuenta):
    def __init__(self, numero_cuenta, saldo):
        super().__init__(numero_cuenta, saldo)
        self.moneda = "Dólar"

    def obtenerSaldo(self):
        return self.saldo

class CuentaCorrientePeso(Cuenta):
    def __init__(self, numero_cuenta, saldo):
        super().__init__(numero_cuenta, saldo)
        self.moneda = "Peso"

    def obtenerSaldo(self):
        return self.saldo

class CuentaCorrienteDolar(Cuenta):
    def __init__(self, numero_cuenta, saldo):
        super().__init__(numero_cuenta, saldo)
        self.moneda = "Dólar"

    def obtenerSaldo(self):
        return self.saldo

class CuentaInversion(Cuenta):
    def __init__(self, numero_cuenta, saldo):
        super().__init__(numero_cuenta, saldo)
        self.moneda = "Peso"  # Se asume que las cuentas de inversión están en pesos

    def obtenerSaldo(self):
        return self.saldo
#-----------------------------------------------------------------------




class Tarjeta(ABC):
    def __init__(self, numero_tarjeta, limite):
        self.numeroTarjeta = numero_tarjeta
        self.limite = limite

    @abstractmethod
    def obtenerLimite(self):
        pass

class TarjetaDebito(Tarjeta):
    def __init__(self, numero_tarjeta, limite):
        super().__init__(numero_tarjeta, limite)

    def obtenerLimite(self):
        return self.limite

class TarjetaCredito(Tarjeta):
    def __init__(self, numero_tarjeta, limite):
        super().__init__(numero_tarjeta, limite)

    def obtenerLimite(self):
        return self.limite
