import random

#buscador de numero de cliente
def buscarNumeroCliente(fNumeroCliente):
    columnaNumeroCliente = 5#columna 6 del csv
    with open("sprint5/clientDB.csv","r") as dataDB:
        dato = []
        posData = 0
        for line in dataDB:
            dato = line.split(",")
            if int(dato[columnaNumeroCliente])==fNumeroCliente:
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