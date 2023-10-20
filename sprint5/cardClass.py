#clase Tarjeta//////////////////////////////////////////////////////////
class Tarjeta():
    def __init__(self, numero_tarjeta, limiteTotal ,limiteCuota):
        self.numeroTarjeta = numero_tarjeta
        self.limiteTotal = limiteTotal
        self.limitecuota = limiteCuota

    def obtenerLimiteTotal(self):
        return self.limiteTotal
    def obtenerLimiteCuota(self):
        return self.limiteCuota

#clase Tarjeta de debito////////////////////////////////////////////////
class TarjetaDebito(Tarjeta):
    def __init__(self, numero_tarjeta, limiteTotal, tipo):
        super().__init__(numero_tarjeta, limiteTotal, "No aplica")
        self.tipo = tipo

    def __str__(self):
        return ("Tarjeta de {}, limite en un pago ${}".format(self.tipo,self.limiteTotal))

    def getTipo(self):
        return self.tipo

#clase tarjeta de credito///////////////////////////////////////////////
class TarjetaCredito(Tarjeta):
    def __init__(self, numero_tarjeta, limiteTotal ,limiteCuota ,tipo):
        super().__init__(numero_tarjeta, limiteTotal ,limiteCuota)
        self.tipo = tipo

    def __str__(self):
        return ("Tarjeta de {}, limite en un pago ${}, limite total por pago en cuotas ${}".format(self.tipo,self.limiteTotal,self.limiteCuota))
    
    def getTipo(self):
        return self.tipo