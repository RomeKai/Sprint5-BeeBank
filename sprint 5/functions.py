import os
from scriptDB import reconstruirCliente
from scriptDB import buscarDniCliente
from clientClass import ClienteClassic
from clientClass import ClienteGold
from clientClass import ClienteBlack

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
        entrada = input(texto)
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

def menu():
    os.system("cls")
    #no magic numbers
    opcion1 = "1"
    opcion2 = "2"
    opcion3 = "3"
    opcion4 = "4"
    opcion5 = "5"
    opcion6 = "6"
    opcion7 = "7"
    opcion8 = "8"

    while True:
        os.system("cls")
        seleccion = validacionSeleccion("--Bienvenido/a al sistema bancario BeeBank--\nIngrese la opcion deseada\n1.Ya tengo una cuenta \n2.Crear cuenta nueva\n3.Salir\nSu seleccion: ",3)
        if seleccion == opcion1:
            os.system("cls")
            dni = enterPositiveNumber("ingrese su DNI")
            os.system("cls")
        elif seleccion == opcion2:
            os.system("cls")
            menuCrearCliente()
        elif seleccion == opcion3:
            os.system("cls")
            print("Gracias por usar nuestros servicios...")
            break
        else:
            print("ERROR")
    input("Presion ENTER para finalizar...")
    os.system("cls")