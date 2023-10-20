#agregar cliente a la base de datos
def agregarCliente(name,surname,typeclient,dni,clientNumber,tCredito,tDebito,cAhorroPesos,cAhorroDolares,cuentaCorriente,cantTCredito,cantTDebito,cantCAhorro,cantCCorriente,cantCInversion,cantChequera,cantLimiteDiario):
    with open("sprint5/clientDB.csv","a") as dataDB:
        dataDB.write("{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(name,surname,typeclient,dni,["transacciones"],clientNumber,tCredito,tDebito,cAhorroPesos,cAhorroDolares,cuentaCorriente,cantTCredito,cantTDebito,cantCAhorro,cantCCorriente,cantCInversion,cantChequera,cantLimiteDiario))
