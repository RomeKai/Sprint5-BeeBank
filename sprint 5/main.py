from bancoClases import *
from os import system
from time import sleep

#LOGICA DEL MAIN, Entrar al sistema, preguntar si ya tiene cuenta y que tipo de cliente es, buscar su existencia y desplegar menu de opc disponibles, chequear si la opc seleccionada aplica el cliente en cuestion
#Si no tiene cuenta se crea una dependiendo del tipo de cliente y lo anade a la lista

#*****************FUNCIONES DEL MAIN***********************
def crearCliente():
    name = input("Ingrese el nombre del cliente: ")
    surname = input("Ingrese el apellido del cliente: ")
    typeclient = input("Ingrese el tipo de cliente, Classic, Gold o Black: ")
    number = input("Ingrese el número de cliente: ")
    dni = input("Ingrese el número de DNI del cliente: ")

    # Crear un nuevo objeto cliente y añadirlo a la lista
    nuevoCliente = Client(name, surname, typeclient, number, dni)
    clients_list.append(nuevoCliente)
    print("Cliente creado y añadido a la lista.")


def buscar_cliente(dniExistente, lista_clientes):
    for client in clients_list:
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
if __name__ == "__main__":
    print("\n --Bienvenido al sistema bancario BeeBank-- \n")
    selection = int(input("Ingrese la opcion deseada \n 1.Ya tengo una cuenta \n 2.Crear cuenta nueva"))
    if selection == 1: 
        dniExistente = input("Ingrese el número de DNI: ")
        foundClient = buscar_cliente(dniExistente, lista_clientes)
        if foundClient:
            print(f"BIENVENIDO : {foundClient.name} {foundClient.surname}")  
            int(input(" \n Seleccione una opcion.  \n"))
            while opc == True:
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
                print("0. Salir")

                if opcion == "1":
                    realizar_retiro_efectivo(cliente)
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
                  print("Gracias por usar el programa \n Loggin off...")
                  opc = False
                else:
                    print("Opción inválida. Por favor, seleccione una opción válida.")
        
                
        else:
            print("Cliente no encontrado.")

    elif selection == 2:
        crearCliente()

    else: system('clear')







   