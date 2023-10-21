from bancoClases import *
import os

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

def validacionTexto2(texto):
    while True:
        entrada = input(texto)
        try:
            entrada = int(entrada)
            break
        except ValueError:
            print("Ingrese una opcion correcta!!")
            input("Presione ENTER para continuar...")
    return str(entrada)

def validacionNumero(texto):
    while True:
        numero = input(texto)
        try:
            numero = int(numero)
            break
        except ValueError:
            print("Ingrese un numero valido!!")
            input("Presione ENTER para continuar...")
    return numero

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


#**********************************************************
#main principal, falta la salida en formato CVG y tambien las opciones de las funciones de calcularMontoTotal,descontarComision,calcularMontoPlazoFijo
lista_clientes = []

#anti magic numbers
opcion1 = "0"
opcion2 = "1"
opcion3 = "2"
opcion4 = "3"
opcion5 = "4"
opcion6 = "5"
opcion7 = "6"
opcion8 = "7"
opcion9 = "8"
opcion10 = "9"
opcion11 = "10"
opcion12 = "11"
opcion13 = "12"
opcion14 = "13"

while True:
    if __name__ == "__main__":
        print("\n --Bienvenido al sistema bancario BeeBank-- \n")
        selection = validacionTexto2("Ingrese la opcion deseada\n1.Ya tengo una cuenta \n2.Crear cuenta nueva\n3.Salir\nSu seleccion: ")
        if selection == opcion2: 
            dniExistente = input("Ingrese el número de DNI: ")
            foundClient = buscar_cliente(dniExistente, lista_clientes)
            if foundClient != None:
                os.system('cls')
                print(f"BIENVENIDO : {foundClient.name} {foundClient.surname}")
                #chequeo de la seleccion

                while True:#entra en la seleccion
                    while True:#verifica la entrada del usuario
                        print("Seleccione una opcion:")
                        print("1. Retiro de Efectivo por Cajero Automático")
                        print("2. Compra en Cuotas con Tarjeta de Crédito   3. Alta Tarjeta de Crédito")
                        print("4. Alta Tarjeta de Débito                    5. Alta Chequera")
                        print("6. Alta Cuenta Corriente                     7. Alta Caja de Ahorro")
                        print("8. Alta Cuenta de Inversión                  9. Compra Dólares")
                        print("10. Venta Dólares                            11. Transferencias")
                        print("12. Ingresar dinero                          13. Visualizar balance")
                        print("0. volver")
                        opcion = input()
                        try:
                            opcion = int(opcion)
                            if opcion<0 and opcion>13:
                                raise ValueError
                            opcion = str(opcion)
                            break
                        except ValueError:
                            print("Error, coloque solo numeros en la seleccion!!")
                            input("Presione ENTER para continuar...")

                    if opcion == opcion2:
                        #retiro efectivo por cajero automatico
                        os.system('cls')
                        tipoCuentaOp = validacionTexto2("Seleccione la caja de ahorro:\n1.Caja ahorro en pesos\n2.Caja ahorro en dolares\nSu entrada: ")
                        monto = validacionNumero("Ingrese el monto a retirar: ")
                        if tipoCuentaOp == opcion2:
                            tipoCuenta = "Caja de ahorro en pesos"
                        elif tipoCuentaOp == opcion3:
                            tipoCuenta = "Caja de ahorro en dólares"
                        foundClient.realizarRetiroEfectivo(tipoCuenta,monto)
                        input("Presione ENTER para continuar...")


                    elif opcion == opcion3:


                         print("Tarjetas de Crédito Disponibles:")
                         tarjetasDisponibles =  foundClient.obtenertarjetasCredito()  # Obtener las tarjetas de crédito disponibles del cliente
                         for elem, tarjeta in enumerate(tarjetasDisponibles, start=1):
                             print(f"{index}. {tarjeta}")

                         try:
                             opcion = int(input("Seleccione la tarjeta de crédito para la compra en cuotas: "))
                             if 1 <= opcion <= len(tarjetasDisponibles):
                                 tarjetaSeleccionada = tarjetasDisponibles[opcion - 1]
                                 monto = float(input("Ingrese el monto de la compra: "))
                                 cuotas = validacionNumero("Ingrese la cantidad de cuotas: ")
                                 if monto <= tarjetaSeleccionada.obtenerLimiteCuota():
                                     foundClient.realizarCompraCuotas(tarjetaSeleccionada, monto, cuotas)
                                     print("Exito.")
                               
                             else:
                                 print("Opción inválida.")
                         except ValueError:
                             print("Por favor, ingrese un número válido.")                                               
                             pass


                    # Lógica para la compra en cuotas con tarjeta de crédito
                    elif opcion == opcion4:
                                try:                             
                                    numero_tarjeta = input("Ingrese el número de la tarjeta de crédito: ")
                                    limite_total = float(input("Ingrese el límite total de la tarjeta de crédito: "))
                                    limite_cuota = float(input("Ingrese el límite por cuota de la tarjeta de crédito: "))
                                    tipo = "Credito"

                                    nuevaTarjetaCredito = TarjetaCredito(numero_tarjeta, limiteTotal, limiteCuota, tipo)
                                    cliente.agregarTarjetaCredito(nuevaTarjetaCredito)
                                    print("Tarjeta de crédito agregada con éxito.")
                                   
                                except  ValueError:
                                    print("Por favor, ingrese un valor válido.")
                                pass
                    elif opcion == opcion5:

                                 try:                             
                                        numero_tarjeta = input("Ingrese el número de la tarjeta de Debito: ")
                                        limite_total = float(input("Ingrese el límite total de la tarjeta de Debito: "))
                                        limite_cuota = float(input("Ingrese el límite por cuota de la tarjeta de Debito: "))
                                        tipo = "Debito"

                                        # Crea una nueva tarjeta de crédito con los datos proporcionados
                                        nuevaTarjetaDebito = TarjetaDebito(numero_tarjeta, limiteTotal, limiteCuota, tipo)

                                        # Agrega la tarjeta de crédito al cliente
                                        cliente.agregarTarjetaDebito(nuevaTarjetaDebito)
                                        print("Tarjeta de Debito agregada con éxito.")
                                 except ValueError:
                                    print("Por favor, ingrese un valor válido.")
                                 pass           


                    elif opcion == opcion6:
                        # Lógica para el alta de tarjeta de débito
                        pass
                    elif opcion == opcion7:
                    # Lógica para el alta de chequera
                        pass
                    elif opcion == opcion8:
                        # Lógica para el alta de cuenta corriente
                        pass
                    elif opcion == opcion9:
                    # Lógica para el alta de caja de ahorro
                        pass
                    elif opcion == opcion10:
                    # Lógica para el alta de cuenta de inversión
                        pass
                    elif opcion == opcion11:
                    # Lógica para la compra de dólares
                        pass
                    elif opcion == opcion12:
                        # Lógica para la venta de dólares
                        pass
                    elif opcion == opcion13:
                        # Lógica para las tranferencias
                        pass
                    elif opcion == opcion14:
                        # Ingreso de dinero (muestra)
                        monto = validacionNumero("Ingrese la cantidad de dinero a agregar: ")
                        foundClient.realizarTransferenciaEntrante(monto)
                        input("Presione ENTER para continuar...")
                    elif opcion == opcion15:
                        print("Saldo de la caja de ahorro en pesos:",str(foundClient.obtenerSaldoCajaPesos()))

                    elif opcion == opcion1:
                        print("Loggin off...")
                        break
                    else:
                        print("Opción inválida. Por favor, seleccione una opción válida.")
            else:
                print("Cliente no encontrado.")
                input("Presione ENTER para continuar...")
        elif selection == opcion3:
            elemento = crearCliente()
            lista_clientes.append(elemento)
        elif selection == opcion4:
            print("Gracias por usar nuestro programa!!")
            break
        else: 
            os.system('cls')