#buscador de cliente segun DNI
def buscarDniCliente(fdni):
    columnaDniCliente = 3#columna 4 del csv
    with open("sprint5/clientDB.csv","r") as dataDB:
        dato = []
        posData = 0
        for line in dataDB:
            dato = line.split(",")
            if int(dato[columnaDniCliente])==fdni:
                return [True,posData]
            posData = posData + 1
    return [False,0]