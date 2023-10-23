import random
#clase Tarjeta//////////////////////////////////////////////////////////
class Tarjeta():
    def __init__(self, tipo_tarjeta,brand_tarjeta,limiteTotal_tarjeta,limiteCuota_tarjeta):
        self.tipo_tarjeta = tipo_tarjeta
        self.brand_tarjeta = brand_tarjeta
        self.limiteTotal_tarjeta = limiteTotal_tarjeta
        self.limiteCuota_tarjeta = limiteCuota_tarjeta
        self.numero_tarjeta = random.randint(100000000000000000000,999999999999999999999)
        if self.tipo_tarjeta == "Debito":
            self.saldo_tarjeta = 0
        else:
            self.saldo_tarjeta = limiteCuota_tarjeta

    def __str__(self):
        if self.getTipoTarjeta() == "Debito":
            return ("Tarjeta de Debito {}\nNumero de tarjeta:{}\nSaldo disponible:${}".format(self.getBrandTarjeta(),self.getNumeroTarjeta(),self.getSaldo()))
        else:
            return ("Tarjeta de Credito {}\nNumero de tarjeta:{}\nLimite en una cuota:${}\nLimite en varias cuotas:{}\nSaldo disponible:{}".format(self.getBrandTarjeta(),self.getNumeroTarjeta(),self.getLimiteTotal(),self.getLimiteCuota(),self.getSaldo()))
        
    #extractores de datos////////
    def getTipoTarjeta(self):
        return self.tipo_tarjeta
    def getBrandTarjeta(self):
        return self.brand_tarjeta
    def getNumeroTarjeta(self):
        return self.numero_tarjeta
    def getLimiteTotal(self):
        if self.getTipoTarjeta()=="Debito":
            return "No aplica"
        else:
            return self.limiteTotal_tarjeta
    def getLimiteCuota(self):
        if self.getTipoTarjeta()=="Debito":
            return "No aplica"
        else:
            return self.limiteCuota_tarjeta
    def getSaldo(self):
        return self.saldo_tarjeta
    #seteadores de datos
    def setSaldo(self):
        return self.saldo_tarjeta