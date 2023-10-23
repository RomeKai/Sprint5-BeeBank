import os
import json
import random
from datetime import datetime
from classClient import ClienteBlack, ClienteClassic, ClienteGold
from scriptBuscarDni import buscarDniCliente

clientes = []


#validaciones////////////////////////////////////////////////////////////////////////////////////////////
#validacion de la seleccion realizada por el cliente
def validacionSeleccion(texto, overflow):
  while True:
    entrada = input(texto + ": ")
    try:
      entrada = int(entrada)
      if entrada > 0 and entrada <= overflow:
        break
      else:
        raise ValueError
    except ValueError:
      print("Ingrese una opcion correcta!!")
      input("Presione ENTER para continuar...")
      os.system("cls")
  return entrada


#validacion de la informacion ingresada por el cliente
def validacionInformacionCliente(texto):
  entrada = ""
  while True:
    entrada = input(texto + ": ")
    if entrada != "" and entrada != " ":
      if texto != "Ingrese el DNI del cliente" and texto != "Ingrese el tipo de cliente, Classic, Gold o Black":
        break
      elif texto == "Ingrese el tipo de cliente, Classic, Gold o Black":
        entrada = entrada.lower()
        if entrada == "classic" or entrada == "gold" or entrada == "black":
          break
        else:
          print("Error,", texto, "nuevamente!!")
      else:
        try:
          entrada = int(entrada)
          break
        except ValueError:
          print("Error,", texto, "nuevamente!!")
    else:
      print("Error,", texto, "nuevamente!!")
  return entrada


#validacion del numero ingresado por el cliente
def enterPositiveNumber(texto):
  while True:
    entrada = input(texto + ": ")
    try:
      entrada = int(entrada)
      if entrada > 0:
        break
      else:
        raise ValueError
    except ValueError:
      print("Error", texto, "nuevamente...")
      input("Presione ENTER para continuar...")
      os.system("cls")
  return entrada


def enterFloatPositiveNumber(texto):
  while True:
    entrada = input(texto + ": ")
    try:
      entrada = float(entrada)
      if entrada > 0:
        break
      else:
        raise ValueError
    except ValueError:
      print("Error", texto, "nuevamente...")
      input("Presione ENTER para continuar...")
      os.system("cls")
  return entrada


#validacion de confirmacion
def validacionConfirmacion(texto):
  while True:
    entrada = input(texto + ": ")
    entrada = entrada.lower()
    if entrada != "y" and entrada != "n":
      print("Error, solo ingrese y/n como respuesta...")
      input("Presione ENTER para continuar...")
      os.system("cls")
    else:
      break
  return entrada


#funciones del menu//////////////////////////////////////////////////////////////////////////////////////////
#creacion del cliente
def menuCrearCliente():
  name = validacionInformacionCliente("Ingrese el nombre del cliente")
  surname = validacionInformacionCliente("Ingrese el apellido del cliente")
  typeclient = validacionInformacionCliente(
      "Ingrese el tipo de cliente, Classic, Gold o Black")
  dni = validacionInformacionCliente("Ingrese el DNI del cliente")

  if typeclient == "classic":
    nuevoCliente = ClienteClassic(name, surname, dni)
  elif typeclient == "gold":
    nuevoCliente = ClienteGold(name, surname, dni)
  elif typeclient == "black":
    nuevoCliente = ClienteBlack(name, surname, dni)

  os.system("cls")
  print("Cliente creado...")
  print(nuevoCliente)

  input("Presiona ENTER para continuar...")
  return nuevoCliente


#funciones del menu de logueo///////////////
def sistemaAltaDebito(foundClient):
  #no magic number
  opcion1 = 1
  opcion2 = 2
  opcion3 = 3
  while True:
    os.system("cls")
    print("SISTEMA DE ALTA DE TARJETA DE DEBITO:")
    seleccion1 = validacionConfirmacion(
        "Desea dar de alta una nueva tarjeta de Debito? y/n: ")
    if seleccion1 == "y":
      selTarjetaBrand = validacionSeleccion(
          "Por favor seleccione que tipo de rama desea adquirir:\n1.VISA\n2.MASTERCARD\n3.AMERICAN EXPRESS\nSu seleccion",
          3)
      if foundClient.getTypeClient() == "Black":
        if selTarjetaBrand == opcion1:
          tarjetaBrand = "VISA"
        elif selTarjetaBrand == opcion2:
          tarjetaBrand = "MASTERCARD"
        elif selTarjetaBrand == opcion3:
          tarjetaBrand = "AMERICAN EXPRESS"
      else:
        if selTarjetaBrand == opcion1:
          tarjetaBrand = "VISA"
        elif selTarjetaBrand == opcion2:
          tarjetaBrand = "MASTERCARD"

      if foundClient.getCantTDebito() < foundClient.getLimiteTarjetaDebito():
        foundClient.crearTarjeta("Debito",
                                 tarjetaBrand)  #crear tarjeta nueva debito
      else:
        print(
            "Se ha alcanzado el limite de tarjetas de debito de la cuenta...")
      input("Presione ENTER para continuar...")
    else:
      print("Cerrando Alta de tarjeta...")
      input("Presione ENTER para volver al menu principal...")
      break


def sistemaAltaCredito(foundClient):
  #no magic number
  opcion1 = 1
  opcion2 = 2
  opcion3 = 3
  while True:
    os.system("cls")
    print("SISTEMA DE ALTA DE TARJETA DE CREDITO:")
    seleccion1 = validacionConfirmacion(
        "Desea dar de alta una nueva tarjeta de Credito? y/n: ")
    if seleccion1 == "y":
      selTarjetaBrand = validacionSeleccion(
          "Por favor seleccione que tipo de rama desea adquirir:\n1.VISA\n2.MASTERCARD\n3.AMERICAN EXPRESS\nSu seleccion",
          3)
      if foundClient.getTypeClient() == "Black":
        if selTarjetaBrand == opcion1:
          tarjetaBrand = "VISA"
        elif selTarjetaBrand == opcion2:
          tarjetaBrand = "MASTERCARD"
        elif selTarjetaBrand == opcion3:
          tarjetaBrand = "AMERICAN EXPRESS"
      else:
        if selTarjetaBrand == opcion1:
          tarjetaBrand = "VISA"
        elif selTarjetaBrand == opcion2:
          tarjetaBrand = "MASTERCARD"

      foundClient.crearTarjeta("Credito",
                               tarjetaBrand)  #crear tarjeta nueva debito
      input("Presione ENTER para continuar...")
    else:
      print("Cerrando Alta de tarjeta...")
      input("Presione ENTER para volver al menu principal...")
      break


def sistemaAltaCuenta(foundClient, texto):
  #no magic number
  while True:
    os.system("cls")
    print(f"SISTEMA DE ALTA DE {texto}:")
    seleccion1 = validacionConfirmacion(
        f"Desea dar de alta una nueva {texto}? y/n: ")
    if seleccion1 == "y":
      foundClient.crearCuenta(texto, foundClient)
      input("Presione ENTER para continuar...")
    else:
      print(f"Cerrando Alta de {texto}...")
      input("Presione ENTER para volver al menu principal...")
      break


def ingresarDinero(foundClient):
  while True:
    os.system("cls")
    opcion1 = 1
    opcion2 = 2
    opcion3 = 3
    opc = print("Que desea hacer?")
    opc = validacionSeleccion(
        "1. Ingresar Pesos\n2. Ingresar Dolares\n3. Volver", 3)
    if opc == opcion1:
      if (len(foundClient.getCajaAhorroPesos()) == 0):
        print("No hay cuentas disponibles en pesos...")
        input("Presione ENTER para continuar...")
        break
      else:
        monto = enterPositiveNumber("Ingrese el monto")
        foundClient.ingresoDinero(foundClient, "Pesos", monto)
    if opc == opcion2:
      if (len(foundClient.getCajaAhorroDolar()) == 0):
        print("No hay cuentas disponibles en dolares...")
        input("Presione ENTER para continuar...")
        break
      else:
        monto = enterPositiveNumber("Ingrese el monto")
        foundClient.ingresoDinero(foundClient, "Dolar", monto)
    if opc == opcion3:
      break


def retirarEfectivo(foundClient):
  opcion1 = 1
  opcion2 = 2
  while True:
    seleccion = validacionConfirmacion("Desea retirar efectivo? y/n")
    if seleccion == "y":
      monto = enterPositiveNumber("Ingrese el monto")
      cuenta = validacionSeleccion(
          "Seleccione una opcion:\n1. Caja de ahorro en pesos\n2. Caja de ahorro en dolares",
          2)
      if cuenta == opcion1:
        cuenta = "Caja de ahorro en pesos"
      elif cuenta == opcion2:
        cuenta = "Caja de ahorro en dolares"
      foundClient.realizarRetiroEfectivo(foundClient, cuenta, monto)
    else:
      break


def transferencias(foundClient, numero):
  seleccion = validacionSeleccion(
      "Selecione Tipo Transferencia 1.Entrante/2.Saliente", 2)
  if seleccion == 1:
    print("Entrantes")
    monto = enterFloatPositiveNumber("ingresar monto de la transferencia")
    fecha = datetime.now()
    cuenta = foundClient.getNumeroCuenta()
    permitidoActual = 9000
    estado = random.choice(["Aceptada", "Rechazada"])
    foundClient.realizarTransferenciaEntrante(foundClient, monto, fecha,
                                              cuenta, permitidoActual, numero,
                                              estado)

  elif seleccion == 2:
    print("Salientes")
    monto = enterFloatPositiveNumber("ingresar monto de la transferencia")
    fecha = datetime.now()
    cuenta = foundClient.getNumeroCuenta()
    permitidoActual = 9000
    estado = random.choice(["Aceptada", "Rechazada"])
    foundClient.realizarTransferenciaSaliente(foundClient, monto, fecha,
                                              cuenta, permitidoActual, numero,
                                              estado)

  else:
    print("Volver al menu")


def compraDolares(foundClient):
  monto = enterPositiveNumber("Ingrese el monto en pesos a comprar")
  foundClient.comprarDolar(foundClient, monto)
  print("Compra realizada")


##########################################


def VentaDolares(foundClient):
  monto = enterPositiveNumber("Ingrese el monto en pesos a comprar")
  foundClient.venderDolar(foundClient, monto)
  print("Venta realizada")


def resumenCuenta(foundClient):
  os.system("cls")
  print("--RESUMEN DE CUENTA BEEBANK--")
  if foundClient.getTypeClient() == "Classic":
    print("Nombre: {}".format(foundClient.getName()))
    print("Apellido: {}".format(foundClient.getSurname()))
    print("DNI: {}".format(foundClient.getDni()))
    print("Numero de cuenta: {}".format(foundClient.getNumberClient()))
    print("Tipo de  de cliente: {}".format(foundClient.getTypeClient()))
    print("Tarjetas de debito activas:")
    if len(foundClient.getTarjetasDebito()) == 0:
      print("No hay tarjetas de debito activas...")
    else:
      for contador, tarjeta in enumerate(foundClient.getTarjetasDebito()):
        print(f"TARJETA NUMERO {contador}")
        print(tarjeta)
    if len(foundClient.getCajaAhorroPesos()) == 0:
      print("No hay cajas de ahorro en pesos activas...")
    else:
      for contador, caja in enumerate(foundClient.getCajaAhorroPesos()):
        print(f"CAJA NUMERO {contador}")
        print(caja)
    if len(foundClient.getCajaAhorroDolar()) == 0:
      print("No hay cajas de ahorro en dolares activas...")
    else:
      for contador, caja in enumerate(foundClient.getCajaAhorroDolar()):
        print(f"CAJA NUMERO {contador}")
        print(caja)
    if len(foundClient.getTransacciones()) == 0:
      print("No hay transacciones realizadas...")
    else:
      for contador, transacciones in enumerate(foundClient.getTransacciones()):
        print(f"CAJA NUMERO {contador}")
        print(transacciones)
  elif foundClient.getTypeClient() == "Gold" or foundClient.getTypeClient(
  ) == "Black":
    print("Nombre: {}".format(foundClient.getName()))
    print("Apellido: {}".format(foundClient.getSurname()))
    print("DNI: {}".format(foundClient.getDni()))
    print("Numero de cuenta: {}".format(foundClient.getNumberClient()))
    print("Tipo de  de cliente: {}".format(foundClient.getTypeClient()))
    print("Tarjetas de debito activas:")
    if len(foundClient.getTarjetasDebito()) == 0:
      print("No hay tarjetas de debito activas...")
    else:
      for contador, tarjeta in enumerate(foundClient.getTarjetasDebito()):
        print(f"TARJETA NUMERO {contador}")
        print(tarjeta)
    if len(foundClient.getTarjetasCredito()) == 0:
      print("No hay tarjetas de credito activas...")
    else:
      for contador, tarjeta in enumerate(foundClient.getTarjetasCredito()):
        print(f"TARJETA NUMERO {contador}")
        print(tarjeta)
    if len(foundClient.getCajaAhorroPesos()) == 0:
      print("No hay cajas de ahorro en pesos activas...")
    else:
      for contador, caja in enumerate(foundClient.getCajaAhorroPesos()):
        print(f"CAJA NUMERO {contador}")
        print(caja)
    if len(foundClient.getCajaAhorroDolar()) == 0:
      print("No hay cajas de ahorro en dolares activas...")
    else:
      for contador, caja in enumerate(foundClient.getCajaAhorroDolar()):
        print(f"CAJA NUMERO {contador}")
        print(caja)
    if len(foundClient.getCuentaCorrientePesos()) == 0:
      print("No hay cuentas corrientes en pesos activas...")
    else:
      for contador, caja in enumerate(foundClient.getCuentaCorrienteDolar()):
        print(f"CAJA NUMERO {contador}")
        print(caja)
    if len(foundClient.getCuentaCorrienteDolar()) == 0:
      print("No hay cuentas corrientes en dolar activas...")
    else:
      for contador, caja in enumerate(foundClient.getCuentaCorrienteDolar()):
        print(f"CAJA NUMERO {contador}")
        print(caja)
    if len(foundClient.getCuentaInversion()) == 0:
      print("No hay cuentas de inversion activas...")
    else:
      for contador, caja in enumerate(foundClient.getCuentaInversion()):
        print(f"CAJA NUMERO {contador}")
        print(caja)
    if len(foundClient.getChequera()) == 0:
      print("No hay chequeras activas...")
    else:
      for contador, caja in enumerate(foundClient.getChequera()):
        print(f"CAJA NUMERO {contador}")
        print(caja)
    if len(foundClient.getTransacciones()) == 0:
      print("No hay transacciones realizadas...")
    else:
      for contador, transacciones in enumerate(foundClient.getTransacciones()):
        print(f"TRANSACCION NUMERO {contador}")
        print(transacciones)

    seleccion = validacionConfirmacion(
        "Desea exportar el resumen de cuenta? y/n")
    if seleccion == "y":
      with open("clienDB.json", "w") as dataDB:
        dataDB.write("{\n")
        dataDB.write("\"Numero Cliente\"" + ":" + str(foundClient.getNumberClient()) +
                     ",\n")
        dataDB.write("\"Nombre\"" + ":\"" + str(foundClient.getName()) +
                     "\",\n")
        dataDB.write("\"Apellido\"" + ":\"" + str(foundClient.getSurname()) +
                     "\",\n")
        dataDB.write("\"dni\"" + ":" + str(foundClient.getDni()) + ",\n")
        dataDB.write("\"Tipo Cliente\"" + ":\"" + str(foundClient.getTypeClient()) +
                     "\",\n")

        lista_de_listas = foundClient.getTransacciones()
        newLista1 = []
        for lista in lista_de_listas:
            
            #[5456465.0, datetime.datetime(2023, 10, 23, 5, 28, 44, 923658), 353382682304907757299, 9000, 2, 'Aceptada']
            diccionario = {
                "estado": lista[5],
                "tipo":"Transaccion",
                "cuentaNumero": lista[2],  # Valor de la lista original
                "permitidoActualParaTransaccion":lista[3],  # Valor de la lista original
                "monto": lista[0],  # Valor de la lista original
                "fecha":lista[1].strftime("%d/%m/%Y %H:%M:%S"),  # Formatear la fecha a la cadena deseada
                "numero": lista[4]  # Valor de la lista original
            }
            newLista1.append(diccionario)

        #lista_de_objetos = [{} for _ in newLista1]
        resultado = {"transacciones": newLista1}
        resultado = json.dumps(resultado)
        dataDB.write(resultado)
        dataDB.write("}")


#menu "logueo"
def menuUsarCliente():
  dni = enterPositiveNumber("ingrese su DNI")
  statePointer1 = buscarDniCliente(dni, clientes)
  stateIndex = 0
  pointerIndex = 1
  numero = 0
  if statePointer1[stateIndex] is True:
    foundClient = clientes[statePointer1[pointerIndex]]
    while True:
      print(f"BIENVENIDO\\A : {foundClient.name} {foundClient.surname}")
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
      opcion12 = 12
      opcion13 = 13
      opcion14 = 14
      opcion15 = 15
      opcion16 = 16
      #CLIENTE CLASSIC***********************************************************************************************************
      if foundClient.getTypeClient() == "Classic":
        while True:
          print("Servicios:")
          print(
              "1. Retiro de Efectivo por Cajero Automático  2. Alta Tarjeta de Débito"
          )
          print(
              "3. Alta Caja de Ahorro Pesos                 4. Alta Caja de Ahorro Dolar"
          )
          print(
              "5. Compra Dólares                            6. Venta Dólares ")
          print(
              "7. Transferencias                            8. Ingresar dinero "
          )
          print(
              "9. Visualizar balances                       10. Resumen de cuenta"
          )
          print("11. Login off")
          seleccion = validacionSeleccion("seleccione una opcion: ", 11)
          break
        if seleccion == opcion1:
          os.system("cls")
          print("RETIRO POR CAJERO AUTOMATICO:")
          retirarEfectivo(foundClient)
        elif seleccion == opcion2:
          os.system("cls")
          sistemaAltaDebito(foundClient)
          os.system("cls")
        elif seleccion == opcion3:
          os.system("cls")
          sistemaAltaCuenta(foundClient, "Caja ahorro pesos")
        elif seleccion == opcion4:
          os.system("cls")
          sistemaAltaCuenta(foundClient, "Caja ahorro dolar")
        elif seleccion == opcion5:
          os.system("cls")
          print("COMPRA DE DOLARES:")
          compraDolares(foundClient)
          input("Pulse ENTER para continuar...")
        elif seleccion == opcion6:
          os.system("cls")
          print("VENTA DE DOLARES:")
          VentaDolares(foundClient)
          input("Pulse ENTER para continuar...")
        elif seleccion == opcion7:
          os.system("cls")
          transferencias(foundClient, numero)
          input("Pulse ENTER para continuar...")
        elif seleccion == opcion8:
          os.system("cls")
          print("INGRESAR DINERO")
          ingresarDinero(foundClient)
        elif seleccion == opcion9:
          os.system("cls")
          print("BALANCES DE LA CUENTA:")
          input("Pulse ENTER para continuar...")
        elif seleccion == opcion10:
          os.system("cls")
          resumenCuenta(foundClient)
        elif seleccion == opcion11:
          print("Cerrando Sesion...")
          input("Pulse ENTER para continuar...")
          os.system("cls")
          break
      #CLIENTE GOLD***********************************************************************************************************
      elif foundClient.getTypeClient() == "Gold":
        while True:
          print("Servicios:")
          print(
              "1. Retiro de Efectivo por Cajero Automático  2. Alta Tarjeta de Débito"
          )
          print(
              "3. Alta Caja de Ahorro Pesos                 4. Alta Caja de Ahorro Dolar"
          )
          print(
              "5. Alta Cuenta Corriente Pesos               6. Alta Cuenta Corriente Dolar"
          )
          print(
              "7. Alta Cuenta Inversion                     8. Alta Chequera")
          print(
              "9. Compra Dólares                            10. Venta Dólares "
          )
          print(
              "11. Transferencias                           12. Ingresar dinero "
          )
          print(
              "13. Visualizar balances                      14. Resumen de cuenta"
          )
          print("15. Alta Tarjeta de Credito                  16. Login off")
          seleccion = validacionSeleccion("seleccione una opcion: ", 16)
          break
        if seleccion == opcion1:
          os.system("cls")
          print("RETIRO POR CAJERO AUTOMATICO:")
          retirarEfectivo(foundClient)
        elif seleccion == opcion2:
          os.system("cls")
          sistemaAltaDebito(foundClient)
          os.system("cls")
        elif seleccion == opcion3:
          os.system("cls")
          sistemaAltaCuenta(foundClient, "Caja ahorro pesos")
        elif seleccion == opcion4:
          os.system("cls")
          sistemaAltaCuenta(foundClient, "Caja ahorro dolares")
        elif seleccion == opcion5:
          os.system("cls")
          sistemaAltaCuenta(foundClient, "Cuenta corriente en pesos")
          input("Pulse ENTER para continuar...")
        elif seleccion == opcion6:
          os.system("cls")
          sistemaAltaCuenta(foundClient, "Cuenta corriente en dolares")
          input("Pulse ENTER para continuar...")
        elif seleccion == opcion7:
          os.system("cls")
          sistemaAltaCuenta(foundClient, "Cuenta inversion")
          input("Pulse ENTER para continuar...")
        elif seleccion == opcion8:
          os.system("cls")
          sistemaAltaCuenta(foundClient, "Chequera")
          input("Pulse ENTER para continuar...")
        elif seleccion == opcion9:
          os.system("cls")
          print("COMPRA DE DOLARES:")
          compraDolares(foundClient)
          input("Pulse ENTER para continuar...")
        elif seleccion == opcion10:
          os.system("cls")
          print("VENTA DE DOLARES:")
          VentaDolares(foundClient)
          input("Pulse ENTER para continuar...")
        elif seleccion == opcion11:
          os.system("cls")
          transferencias(foundClient, numero)
          input("Pulse ENTER para continuar...")
        elif seleccion == opcion12:
          os.system("cls")
          ingresarDinero(foundClient)
        elif seleccion == opcion13:
          os.system("cls")
          print("BALANCES DE LA CUENTA:")
          input("Pulse ENTER para continuar...")
        elif seleccion == opcion14:
          os.system("cls")
          resumenCuenta(foundClient)
        elif seleccion == opcion15:
          os.system("cls")
          sistemaAltaCredito(foundClient)
          os.system("cls")
        elif seleccion == opcion16:
          print("Cerrando Sesion...")
          input("Pulse ENTER para continuar...")
          os.system("cls")
          break
      #CLIENTE BLACK***********************************************************************************************************
      elif foundClient.getTypeClient() == "Black":
        while True:
          print("Servicios:")
          print(
              "1. Retiro de Efectivo por Cajero Automático  2. Alta Tarjeta de Débito"
          )
          print(
              "3. Alta Caja de Ahorro Pesos                 4. Alta Caja de Ahorro Dolar"
          )
          print(
              "5. Alta Cuenta Corriente Pesos               6. Alta Cuenta Corriente Dolar"
          )
          print(
              "7. Alta Cuenta Inversion                     8. Alta Chequera")
          print(
              "9. Compra Dólares                            10. Venta Dólares "
          )
          print(
              "11. Transferencias                           12. Ingresar dinero "
          )
          print(
              "13. Visualizar balances                      14. Resumen de cuenta"
          )
          print("15. Alta Tarjeta de Credito                  16. Login off")
          seleccion = validacionSeleccion("seleccione una opcion: ", 16)
          break
        if seleccion == opcion1:
          os.system("cls")
          print("RETIRO POR CAJERO AUTOMATICO:")
          retirarEfectivo(foundClient)
        elif seleccion == opcion2:
          os.system("cls")
          sistemaAltaDebito(foundClient)
          os.system("cls")
        elif seleccion == opcion3:
          os.system("cls")
          sistemaAltaCuenta(foundClient, "Caja ahorro pesos")
        elif seleccion == opcion4:
          os.system("cls")
          sistemaAltaCuenta(foundClient, "Caja ahorro dolares")
        elif seleccion == opcion5:
          os.system("cls")
          sistemaAltaCuenta(foundClient, "Cuenta corriente en pesos")
          input("Pulse ENTER para continuar...")
        elif seleccion == opcion6:
          os.system("cls")
          sistemaAltaCuenta(foundClient, "Cuenta corriente en dolares")
          input("Pulse ENTER para continuar...")
        elif seleccion == opcion7:
          os.system("cls")
          sistemaAltaCuenta(foundClient, "Cuenta inversion")
          input("Pulse ENTER para continuar...")
        elif seleccion == opcion8:
          os.system("cls")
          sistemaAltaCuenta(foundClient, "Chequera")
          input("Pulse ENTER para continuar...")
        elif seleccion == opcion9:
          os.system("cls")
          print("COMPRA DE DOLARES:")
          compraDolares(foundClient)
          input("Pulse ENTER para continuar...")
        elif seleccion == opcion10:
          os.system("cls")
          print("VENTA DE DOLARES:")
          VentaDolares(foundClient)
          input("Pulse ENTER para continuar...")
        elif seleccion == opcion11:
          os.system("cls")
          transferencias(foundClient, numero)
          input("Pulse ENTER para continuar...")
        elif seleccion == opcion12:
          os.system("cls")
          ingresarDinero(foundClient)
        elif seleccion == opcion13:
          os.system("cls")
          print("BALANCES DE LA CUENTA:")
          input("Pulse ENTER para continuar...")
        elif seleccion == opcion14:
          os.system("cls")
          resumenCuenta(foundClient)
        elif seleccion == opcion15:
          os.system("cls")
          sistemaAltaCredito(foundClient)
          os.system("cls")
        elif seleccion == opcion16:
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
  opcion1 = 1
  opcion2 = 2
  opcion3 = 3

  while True:
    os.system("cls")
    seleccion = validacionSeleccion(
        "--Bienvenido/a al sistema bancario BeeBank--\nIngrese la opcion deseada\n1.Ya tengo una cuenta \n2.Crear cuenta nueva\n3.Salir\nSu seleccion: ",
        3)
    if seleccion == opcion1:
      os.system("cls")
      menuUsarCliente()
    elif seleccion == opcion2:
      os.system("cls")
      newClient = menuCrearCliente()
      clientes.append(newClient)
    elif seleccion == opcion3:
      os.system("cls")
      print("Gracias por usar nuestros servicios...")
      break
    else:
      print("ERROR")
  input("Presione ENTER para finalizar...")
  os.system("cls")
