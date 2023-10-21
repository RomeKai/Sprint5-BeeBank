import os
from scriptRecClase import reconstruirCliente
from scriptSearchDNI import buscarDniCliente
from clientClass import ClienteClassic
from clientClass import ClienteBlack
from clientClass import ClienteGold

#validacion de la seleccion realizada por el cliente
def validacionSeleccion(texto,overflow):
    while True:
        entrada = input(texto)
        try:
            entrada = int(entrada)
            if entrada>0 and entrada<=overflow:
                break
            else:
                raise ValueError
        except ValueError:
            print("Ingrese una opcion correcta!!")
            input("Presione ENTER para continuar...")
            os.system("cls")
    return str(entrada)

#validacion de la informacion ingresada por el cliente
def validacionInformacionCliente(texto):
    entrada = ""
    while True:
        entrada = input(texto+": ")
        if entrada!="" and entrada!=" ":
            if texto!="Ingrese el DNI del cliente" and texto!="Ingrese el tipo de cliente, Classic, Gold o Black":
                break
            elif texto=="Ingrese el tipo de cliente, Classic, Gold o Black":
                entrada = entrada.lower()
                if entrada=="classic" or entrada=="gold" or entrada=="black":
                    break
                else:
                    print("Error,",texto,"nuevamente!!")
            else:
                try:
                    int(entrada)
                    break
                except ValueError:
                    print("Error,",texto,"nuevamente!!")
        else:
            print("Error,",texto,"nuevamente!!")
    return entrada

#validacion del numero ingresado por el cliente
def enterPositiveNumber(texto):
    while True:
        entrada = input(texto+": ")
        try:
            entrada = int(entrada)
            if entrada>0:
                break
            else:
                raise ValueError
        except ValueError:
            print("Error",texto,"nuevamente...")
            input("Presione ENTER para continuar...")
            os.system("cls")
    return entrada

#creacion del cliente
def menuCrearCliente():
    name = validacionInformacionCliente("Ingrese el nombre del cliente")
    surname = validacionInformacionCliente("Ingrese el apellido del cliente")
    typeclient = validacionInformacionCliente("Ingrese el tipo de cliente, Classic, Gold o Black")
    dni = validacionInformacionCliente("Ingrese el DNI del cliente")

    statePointer = buscarDniCliente(int(dni))#busca en la base de datos si ya hay algun cliente con ese dni
    stateIndex=0

    if statePointer[stateIndex]==False:
        # Crear un nuevo objeto cliente y añadirlo a la base de datos
        if typeclient=="classic":
            nuevoCliente = ClienteClassic(name,surname,dni,None,None,None,None,None,None,None,None,None,None,None,None,None,None,"creating")
        elif typeclient=="gold":
            nuevoCliente = ClienteGold(name,surname,dni,None,None,None,None,None,None,None,None,None,None,None,None,None,None,"creating")
        elif typeclient=="black":
            nuevoCliente = ClienteBlack(name,surname,dni,None,None,None,None,None,None,None,None,None,None,None,None,None,None,"creating")
        os.system("cls")
        print("Cliente creado...")
        print(nuevoCliente)
    else:
        print("Cliente con DNI ya existente...")
    input("Presiona ENTER para continuar...")

def menuUsarCliente():
    dni = enterPositiveNumber("ingrese su DNI")
    statePointer1 = buscarDniCliente(dni)
    stateIndex = 0
    if statePointer1[stateIndex]==True:
        foundClient = reconstruirCliente(dni)
        while True:
            print(f"BIENVENIDO\A : {foundClient.name} {foundClient.surname}")
            #no magic numbers
            opcion1 = 1
            opcion2 = 2
            opcion3 = 3
            opcion4 = 4
            opcion5 = 5
            opcion6 = 6
            opcion7 = 7
            opcion8 = 8
            opcion9 = 9
            opcion10 = 10
            opcion11 = 11
            if foundClient.getTypeClient() == "Classic":
                while True:
                    print("Servicios:")
                    print("1. Retiro de Efectivo por Cajero Automático  2. Alta Tarjeta de Débito")
                    print("3. Alta Caja de Ahorro Pesos                 4. Alta Caja de Ahorro Dolar")
                    print("5. Compra Dólares                            6. Venta Dólares ")
                    print("7. Transferencias                            8. Ingresar dinero ")
                    print("9. Visualizar balances                       10. Resumen de cuenta")
                    print("11. Login off")
                    seleccion = validacionSeleccion("seleccione una opcion",11)
                    break
                if seleccion==opcion1:
                    os.system("cls")
                    print("RETIRO POR CAJERO AUTOMATICO:")
                    input("Pulse ENTER para continuar...")
                elif seleccion==opcion2:
                    os.system("cls")
                    print("SISTEMA DE ALTA DE TARJETA DE DEBITO:")
                    input("Pulse ENTER para continuar...")
                elif seleccion==opcion3:
                    os.system("cls")
                    print("SISTEMA DE ALTA DE CAJA DE AHORRO EN PESOS:")
                    input("Pulse ENTER para continuar...")
                elif seleccion==opcion4:
                    os.system("cls")
                    print("SISTEMA DE ALTA DE CAJA DE AHORRO EN DOLARES:")
                    input("Pulse ENTER para continuar...")
                elif seleccion==opcion5:
                    os.system("cls")
                    print("COMPRA DE DOLARES:")
                    input("Pulse ENTER para continuar...")
                elif seleccion==opcion6:
                    os.system("cls")
                    print("VENTA DE DOLARES:")
                    input("Pulse ENTER para continuar...")
                elif seleccion==opcion7:
                    os.system("cls")
                    print("HISTORIAL DE TRANSFERENCIAS:")
                    input("Pulse ENTER para continuar...")
                elif seleccion==opcion8:
                    pass
                elif seleccion==opcion9:
                    os.system("cls")
                    print("BALANCES DE LA CUENTA:")
                    input("Pulse ENTER para continuar...")
                elif seleccion==opcion10:
                    os.system("cls")
                    print("RESUMEN DE CUENTA:")
                    input("Pulse ENTER para continuar...")
                elif seleccion==opcion11:
                    print("Cerrando Sesion...")
                    input("Pulse ENTER para continuar...")
                    os.system("cls")
                    break

    else:
        print("No existen cuentas con ese DNI...")
        input("Presione ENTER para continuar...")
    os.system("cls")

def menu():
    os.system("cls")
    #no magic numbers
    opcion1 = "1"
    opcion2 = "2"
    opcion3 = "3"

    while True:
        os.system("cls")
        seleccion = validacionSeleccion("--Bienvenido/a al sistema bancario BeeBank--\nIngrese la opcion deseada\n1.Ya tengo una cuenta \n2.Crear cuenta nueva\n3.Salir\nSu seleccion: ",3)
        if seleccion == opcion1:
            os.system("cls")
            menuUsarCliente()
        elif seleccion == opcion2:
            os.system("cls")
            menuCrearCliente()
        elif seleccion == opcion3:
            os.system("cls")
            print("Gracias por usar nuestros servicios...")
            break
        else:
            print("ERROR")
    input("Presione ENTER para finalizar...")
    os.system("cls")


def calcularMontoTotal(precioDolar, cantidadDolares):
    impuestoPais = 0.3  # 30% de impuesto país
    ganancias = 0.35  # 35% de impuesto a las ganancias
    
    montoTotal = cantidadDolares * precioDolar
    impuestoTotal = montoTotal * impuestoPais
    gananciasTotal = montoTotal * ganancias
    
    montoTotalConImpuestos = montoTotal + impuestoTotal + gananciasTotal
    return montoTotalConImpuestos

def descontarComision(monto, porcentajeComision):
    comision = (porcentajeComision / 100) * monto
    montoDescontado = monto - comision
    return montoDescontado

def calcularMontoPlazoFijo(monto, interes):
    montoFinal = monto * (1 + interes)
    return montoFinal
