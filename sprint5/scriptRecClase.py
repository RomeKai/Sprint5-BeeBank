import os
from clientClass import ClienteClassic
from clientClass import ClienteBlack
from clientClass import ClienteGold
from scriptSearchDNI import buscarDniCliente
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
        with open("sprint5/clientDB.csv","r") as dataDB:
            dato=[]
            dataDB.seek(statePointer[position])
            dato = dataDB.readline().split(",")

            clientName = dato[clientNameIndex]
            clientSurname = dato[clientSurnameIndex]
            clientType = dato[clientTypeIndex]
            clientTransfers = eval(dato[clientTransfersIndex])
            clientNumber = dato[clientNumberIndex]
            clientTCredito = eval(dato[clientTCreditoIndex])
            clientTDebito = eval(dato[clientTDebitoIndex])
            clientCAhorroPesos = eval(dato[clientCAhorroPesosIndex])
            clientCAhorroDolares = eval(dato[clientCAhorroDolaresIndex])
            clientCuentaCorriente = eval(dato[clientCuentaCorrienteIndex])
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
        input()
        os.system("cls")
    else:
        print("Cliente no encontrado...")
        input("Presione ENTER para continuar...")
        os.system("cls")