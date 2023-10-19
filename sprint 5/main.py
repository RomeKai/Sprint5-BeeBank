from bancoClases import *
import os
from time import sleep

#LOGICA DEL MAIN, Entrar al sistema, preguntar si ya tiene cuenta y que tipo de cliente es, buscar su existencia y desplegar menu de opc disponibles, chequear si la opc seleccionada aplica el cliente en cuestion
#Si no tiene cuenta se crea una dependiendo del tipo de cliente y lo anade a la lista

#*****************FUNCIONES DEL MAIN***********************
def validacionTexto(texto):
    entrada = ""
    while True:
        entrada = input(texto+": ")
        if entrada!="" and entrada!=" ":
            if texto!="Ingrese el DNI del cliente" and texto!="Ingrese el numero del cliente" and texto!="Ingrese el tipo de cliente, Classic, Gold o Black":
                break
            elif texto=="Ingrese el tipo de cliente, Classic, Gold o Black":
                entrada = entrada.lower()
                if entrada=="classic" or entrada=="gold" or entrada=="black":
                    break
            else:
                try:
                    int(entrada)
                    break
                except ValueError:
                    print("Error,",texto,"nuevamente!!")
        else:
            print("Error,",texto,"nuevamente!!")
    return entrada

def validacionTexto2():
    while True:
        entrada = input("Ingrese la opcion deseada\n1.Ya tengo una cuenta \n2.Crear cuenta nueva\n3.Salir\nSu seleccion: ")
        try:
            entrada = int(entrada)
            break
        except ValueError:
            print("Ingrese una opcion correcta!!")
            input("Presione ENTER para continuar...")
    return entrada

def crearCliente():
    name = validacionTexto("Ingrese el nombre del cliente")
    surname = validacionTexto("Ingrese el apellido del cliente")
    typeclient = validacionTexto("Ingrese el tipo de cliente, Classic, Gold o Black")
    numberclient = validacionTexto("Ingrese el numero del cliente")
    dni = validacionTexto("Ingrese el DNI del cliente")

    # Crear un nuevo objeto cliente y añadirlo a la lista
    if typeclient=="classic":
        nuevoCliente = ClienteClassic(name, surname, numberclient, dni)
    elif typeclient=="gold":
        nuevoCliente = ClienteGold(name, surname, numberclient, dni)
    elif typeclient=="black":
        nuevoCliente = ClienteBlack(name, surname, numberclient, dni)

    print("Cliente creado y añadido a la lista.")
    print(nuevoCliente)
    input("Presion ENTER para continuar...")
    return nuevoCliente

def buscar_cliente(dniExistente, lista_clientes):
    for client in lista_clientes:
        if client.dni == dniExistente:
            return client
    return None  



    #estas 3 son obligatorias por el enunciado

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



#**********************************************************
#main principal, falta la salida en formato CVG y tambien las opciones de las funciones de calcularMontoTotal,descontarComision,calcularMontoPlazoFijo
lista_clientes = []
while True:
    if __name__ == "__main__":
        print("\n --Bienvenido al sistema bancario BeeBank-- \n")
        selection = validacionTexto2()
        if selection == 1: 
            dniExistente = input("Ingrese el número de DNI: ")
            foundClient = buscar_cliente(dniExistente, lista_clientes)
            if foundClient != None:
                print(f"BIENVENIDO : {foundClient.name} {foundClient.surname}")
                #chequeo de la seleccion
                while True:
                    print("Seleccione una opcion:")
                    print("1. Retiro de Efectivo por Cajero Automático")
                    print("2. Retiro de Efectivo por Caja")
                    print("3. Compra en Cuotas con Tarjeta de Crédito")
                    print("4. Alta Tarjeta de Crédito")
                    print("5. Alta Tarjeta de Débito")
                    print("6. Alta Chequera")
                    print("7. Alta Cuenta Corriente")
                    print("8. Alta Caja de Ahorro")
                    print("9. Alta Cuenta de Inversión")
                    print("10. Compra Dólares")
                    print("11. Venta Dólares")
                    print("12. Transferencia Enviada")
                    print("13. Transferencia Recibida")
                    print("0. Volver")
                    opcion = input()
                    try:
                        opcion = int(opcion)
                        break
                    except:
                        print("Error, coloque solo numeros en la seleccion!!")

                while True:

                    if opcion == "1":
                        #realizar_retiro_efectivo(cliente)
                        pass
                    elif opcion == "2":
                        # Lógica para el retiro de efectivo por caja
                        pass
                    elif opcion == "3":
                    # Lógica para la compra en cuotas con tarjeta de crédito
                        pass
                    elif opcion == "4":
                    # Lógica para el alta de tarjeta de crédito
                        pass
                    elif opcion == "5":
                        # Lógica para el alta de tarjeta de débito
                        pass
                    elif opcion == "6":
                    # Lógica para el alta de chequera
                        pass
                    elif opcion == "7":
                        # Lógica para el alta de cuenta corriente
                        pass
                    elif opcion == "8":
                    # Lógica para el alta de caja de ahorro
                        pass
                    elif opcion == "9":
                    # Lógica para el alta de cuenta de inversión
                        pass
                    elif opcion == "10":
                    # Lógica para la compra de dólares
                        pass
                    elif opcion == "11":
                        # Lógica para la venta de dólares
                        pass
                    elif opcion == "12":
                        # Lógica para la transferencia enviada
                        pass
                    elif opcion == "13":
                        # Lógica para la transferencia recibida
                        pass
                    elif opcion == "0":
                        print("Loggin off...")
                        break
                    else:
                        print("Opción inválida. Por favor, seleccione una opción válida.")
            else:
                print("Cliente no encontrado.")
                input("Presione ENTER para continuar...")
        elif selection == 2:
            elemento = crearCliente()
            lista_clientes.append(elemento)
        elif selection == 3:
            print("Gracias pro usar nuestro programa!!")
            break
        else: 
            os.system('cls')