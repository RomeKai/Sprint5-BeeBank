import random
import os

#buscador de numero de cliente
def buscarNumeroCliente(fNumeroCliente):
    columnaNumeroCliente = 5#columna 6 del csv
    with open("sprint 5/clientDB.csv","r") as dataDB:
        dato = []
        posData = 0
        for line in dataDB:
            dato = line.split(",")
            if int(dato[columnaNumeroCliente])==fNumeroCliente:
                return [True,posData]
            posData = posData + 1 
    return [False,0]

#buscador de cliente segun DNI
def buscarDniCliente(fdni):
    columnaDniCliente = 3#columna 4 del csv
    with open("sprint 5/clientDB.csv","r") as dataDB:
        dato = []
        posData = 0
        for line in dataDB:
            dato = line.split(",")
            if int(dato[columnaDniCliente])==fdni:
                return [True,posData]
            posData = posData + 1
    return [False,0]

#generar numero de cliente unico de 21 cifras
def generarNumeroCliente():
    first = 0
    while True:
        numero = random.randint(100000000000000000000,999999999999999999999)
        numberExists = buscarNumeroCliente(numero)
        if numberExists[first]==False:
            break
    return numero

#agregar cliente a la base de datos
def agregarCliente(name,surname,typeclient,dni,clientNumber,tCredito,tDebito,cAhorroPesos,cAhorroDolares,cuentaCorriente,cantTCredito,cantTDebito,cantCAhorro,cantCCorriente,cantCInversion,cantChequera,cantLimiteDiario):
    with open("sprint 5/clientDB.csv","a") as dataDB:
        dataDB.write("{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(name,surname,typeclient,dni,["transacciones"],clientNumber,tCredito,tDebito,cAhorroPesos,cAhorroDolares,cuentaCorriente,cantTCredito,cantTDebito,cantCAhorro,cantCCorriente,cantCInversion,cantChequera,cantLimiteDiario))

#reconstruir cliente
def reconstruirCliente(fdni):
    state = 0
    position = 1

    clientNameIndex=0
    clientSurnameIndex = 1
    clientTypeIndex = 2
    clientDni = fdni
    clientTransfersIndex = 4
    clientNumberIndex = 5
    clientTCreditoIndex = 6
    clientTDebitoIndex = 7
    clientCAhorroPesosIndex = 8
    clientCAhorroDolaresIndex = 9
    clientCuentaCorrienteIndex = 10
    clientCantTCreditoIndex = 11
    clientCantTDebitoIndex = 12
    clientCantCAhorroIndex = 13
    clientCantCCorrienteIndex = 14
    clientCantCInversionIndex = 15
    clientCantChequeraIndex = 16
    clientCantLimiteDiarioIndex = 17

    statePointer = buscarDniCliente(clientDni)
    if statePointer[state]==True:
        with open("sprint 5/clientDB.csv","r") as dataDB:
            dato=[]
            dataDB.seek(statePointer[position])
            dato = dataDB.readline().split(",")

            clientName = dato[clientNameIndex]
            clientSurname = dato[clientSurnameIndex]
            clientType = dato[clientTypeIndex]
            clientTransfers = dato[clientTransfersIndex]
            clientNumber = dato[clientNumberIndex]
            clientTCredito = dato[clientTCreditoIndex]
            clientTDebito = dato[clientTDebitoIndex]
            clientCAhorroPesos = dato[clientCAhorroPesosIndex]
            clientCAhorroDolares = dato[clientCAhorroDolaresIndex]
            clientCuentaCorriente = dato[clientCuentaCorrienteIndex]
            clientCantTCredito = dato[clientCantTCreditoIndex]
            clientCantTDebito = dato[clientCantTDebitoIndex]
            clientCantCAhorro = dato[clientCantCAhorroIndex]
            clientCantCCorriente = dato[clientCantCCorrienteIndex]
            clientCantCInversion = dato[clientCantCInversionIndex]
            clientCantChequera = dato[clientCantChequeraIndex]
            clientCantLimiteDiario = dato[clientCantLimiteDiarioIndex]
            
        if clientType == "Classic":
            clienteV = ClienteClassic(clientName,clientSurname,clientDni,clientTransfers,clientNumber,clientTCredito,clientTDebito,clientCAhorroPesos,clientCAhorroDolares,clientCuentaCorriente,clientCantTCredito,clientCantTDebito,clientCantCAhorro,clientCantCCorriente,clientCantCInversion,clientCantChequera,clientCantLimiteDiario,"recreating")
        elif clientType == "Gold":
            clienteV = ClienteGold(clientName,clientSurname,clientDni,clientTransfers,clientNumber,clientTCredito,clientTDebito,clientCAhorroPesos,clientCAhorroDolares,clientCuentaCorriente,clientCantTCredito,clientCantTDebito,clientCantCAhorro,clientCantCCorriente,clientCantCInversion,clientCantChequera,clientCantLimiteDiario,"recreating")
        elif clientType == "Black":
            clienteV = ClienteBlack(clientName,clientSurname,clientDni,clientTransfers,clientNumber,clientTCredito,clientTDebito,clientCAhorroPesos,clientCAhorroDolares,clientCuentaCorriente,clientCantTCredito,clientCantTDebito,clientCantCAhorro,clientCantCCorriente,clientCantCInversion,clientCantChequera,clientCantLimiteDiario,"recreating")
        print(clienteV)
        os.system("cls")
    else:
        print("Cliente no encontrado...")
        input("Presione ENTER para continuar...")
        os.system("cls")