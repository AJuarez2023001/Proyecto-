import sys
import time
import os
# Gerente
Productos = {}
Compra = {}


def Salida() :
    sys.exit("""""
▄▀█ █▀▄ █ █▀█ █▀   █░█ █░█ █▀▀ █░░ █░█ █▀▀   █▀█ █▀█ █▀█ █▄░█ ▀█▀ █▀█
█▀█ █▄▀ █ █▄█ ▄█   ▀▄▀ █▄█ ██▄ █▄▄ ▀▄▀ ██▄   █▀▀ █▀▄ █▄█ █░▀█ ░█░ █▄█""")

def Menu():
    menuOption = True
    while(menuOption == True):
        print("""
░█████╗░░█████╗░░░░░░██╗░█████╗░
██╔══██╗██╔══██╗░░░░░██║██╔══██╗
██║░░╚═╝███████║░░░░░██║███████║
██║░░██╗██╔══██║██╗░░██║██╔══██║
╚█████╔╝██║░░██║╚█████╔╝██║░░██║
░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝

██████╗░███████╗░██████╗░██╗░██████╗████████╗██████╗░░█████╗░██████╗░░█████╗░██████╗░░█████╗░
██╔══██╗██╔════╝██╔════╝░██║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██████╔╝█████╗░░██║░░██╗░██║╚█████╗░░░░██║░░░██████╔╝███████║██║░░██║██║░░██║██████╔╝███████║
██╔══██╗██╔══╝░░██║░░╚██╗██║░╚═══██╗░░░██║░░░██╔══██╗██╔══██║██║░░██║██║░░██║██╔══██╗██╔══██║
██║░░██║███████╗╚██████╔╝██║██████╔╝░░░██║░░░██║░░██║██║░░██║██████╔╝╚█████╔╝██║░░██║██║░░██║
╚═╝░░╚═╝╚══════╝░╚═════╝░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝ 
        \n""")
        print('''Por favor seleccione una opcion: 
                    1. Bodega
                    2. Caja
                    3. Exit \n
                    ''')
        option = int(input("Ingrese opción: "))
        if(option == 1):
            menuOption= False
            Bodega()
        elif(option == 2):
            menuOption = False
            MenuCaja()
        elif(option == 3):
            Salida()
        else:
            print("\n El número ingresado ha sido incorrecto, por favor vuelva a intentarlo \n")
            time.sleep(3)
            os.system("cls")
        


def Bodega():
    optionMenuBodega = True
    while optionMenuBodega == True:
        os.system("cls")
        print("""**************************************************
          ************ BIENVENIDO GERENTE *********************
          *****************************************************
          
         Bienvenido, actualmente se encuentra en la DB de Bodega.
            
            Elija una opción para continuar:
            
                1. Ingrese los Productos
                2. Ver Productos Disponibles
                3. Regresar al menú principal \n
                """ )
        optionMenu = int(input("Seleccione Opción: "))
        if(optionMenu==1):
            optionMenuBodega = False
            Gerente()
        elif(optionMenu==2):
            optionMenuBodega = False
            viewGerente()
        elif(optionMenu==3):
            optionMenuBodega = False
            Menu()
        else:
            print("\nHa ocurrido un error, por favor seleccione la opción correcta \n")
            time.sleep(2)
            os.system("cls")
    
    

def Gerente():
     os.system("cls")
     Ingresar = True
     while Ingresar == True :      
        Pregunta = input(" ¿Desea ingresar datos? s/n " )
        if Pregunta == "s" or Pregunta == "S" :
            nombre = input("Ingrese sus productos " )
            precio = float(input("Ingrese el precio del producto "))
            Productos[nombre] = precio
            print("El producto se ha agregado exitosamente!")
            time.sleep(3)
            os.system("cls")
            pass
        elif(Pregunta.lower()=="n"):
            Ingresar = False
            Bodega()
        else:
            print("\nHa ocurrido un error, por favor seleccione la opción correcta \n")
            time.sleep(2)
            os.system("cls")
     
def viewGerente():
    registro = 0
    os.system("cls")
    print("""
╔═══╦═══╦═══╦═══╦╗─╔╦═══╦════╦═══╦═══╗
║╔═╗║╔═╗║╔═╗╠╗╔╗║║─║║╔═╗║╔╗╔╗║╔═╗║╔═╗║
║╚═╝║╚═╝║║─║║║║║║║─║║║─╚╩╝║║╚╣║─║║╚══╗
║╔══╣╔╗╔╣║─║║║║║║║─║║║─╔╗─║║─║║─║╠══╗║
║║──║║║╚╣╚═╝╠╝╚╝║╚═╝║╚═╝║─║║─║╚═╝║╚═╝║
╚╝──╚╝╚═╩═══╩═══╩═══╩═══╝─╚╝─╚═══╩═══╝

    \n""")
    for x in Productos:
        registro = registro + 1
        print(str(registro), x , "El precio de su producto es de Q", Productos[x])
    time.sleep(10)
    os.system("cls")
    Bodega()
    

def MenuCaja():
    os.system("cls")
    print("""
█▀▀ █▀▀█ ░░▀ █▀▀█ 
█░░ █▄▄█ ░░█ █▄▄█ 
▀▀▀ ▀░░▀ █▄█ ▀░░▀
   \n""" )
    print('''Seleccione una  opción para la compra
    1. Compra
    2.  Facturar \n
    3.  Salir
    ''')
    opcion = int(input("Ingrese una opción: "))
    if(opcion ==1):
        ComprasProductos()
    elif(opcion == 2):
        Facturacion()
    elif(opcion ==3):
        Menu()

def ComprasProductos():
    os.system("cls")
    Ingresar = True
    conteo = 0
    print("""""
░█████╗░░█████╗░███╗░░░███╗██████╗░██████╗░░█████╗░░██████╗
██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░╚═╝██║░░██║██╔████╔██║██████╔╝██████╔╝███████║╚█████╗░
██║░░██╗██║░░██║██║╚██╔╝██║██╔═══╝░██╔══██╗██╔══██║░╚═══██╗
╚█████╔╝╚█████╔╝██║░╚═╝░██║██║░░░░░██║░░██║██║░░██║██████╔╝
░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░\n""" )
    for y in Productos:
        conteo = conteo + 1
        print(str(conteo)+" . " + y + " precio: Q" +str(Productos[y]))
    print("\n")

    nProd = input("Ingrese el producto que desea comprar: ")
    
    for z in Productos:
        if nProd == z:
            cantidadProd = int(input("Ingrese cantidad: "))
            Compra[nProd] = cantidadProd * Productos[nProd]
            print("su compra")
            print(Compra)
        else:
            for b in Productos:
                if nProd == z:
                    cantidadProd = int(input("Ingrese cantidad: "))
                    Compra[nProd] = cantidadProd * Productos[nProd]
                    print("su compra")
                    print(Compra)

    while Ingresar == True :
        Preguntar = input (" ¿Desea Ingresar más productos s/n ")
        if Preguntar == "s" or Preguntar == "S" :
            
            nProd = input("Ingrese el producto que desea comprar: ")
    
            for z in Productos:
                    if nProd == z:
                        cantidadProd = int(input("Ingrese cantidad: "))
                        Compra[nProd] = cantidadProd * Productos[nProd]
                        print("su compra")
                        print(Compra)
                    else:
                        for b in Productos:
                            if nProd == z:
                                cantidadProd = int(input("Ingrese cantidad: "))
                                Compra[nProd] = cantidadProd * Productos[nProd]
                                print("su compra")
                                print(Compra)
        elif(Preguntar.lower()=="n"):
            Ingresar = False
            
            Facturacion()

def Facturacion():
    Subtotal = 0
    registro = 0
    os.system("cls")
    print(""""" 
        ███████╗░██████╗████████╗░█████╗░░██████╗  ███████╗███╗░░██╗
        ██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔════╝  ██╔════╝████╗░██║
        █████╗░░╚█████╗░░░░██║░░░███████║╚█████╗░  █████╗░░██╔██╗██║
        ██╔══╝░░░╚═══██╗░░░██║░░░██╔══██║░╚═══██╗  ██╔══╝░░██║╚████║
        ███████╗██████╔╝░░░██║░░░██║░░██║██████╔╝  ███████╗██║░╚███║
        ╚══════╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░  ╚══════╝╚═╝░░╚══╝

        ███████╗░█████╗░░█████╗░████████╗██╗░░░██╗██████╗░░█████╗░░█████╗░██╗░█████╗░███╗░░██╗
        ██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██║░░░██║██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗████╗░██║
        █████╗░░███████║██║░░╚═╝░░░██║░░░██║░░░██║██████╔╝███████║██║░░╚═╝██║██║░░██║██╔██╗██║
        ██╔══╝░░██╔══██║██║░░██╗░░░██║░░░██║░░░██║██╔══██╗██╔══██║██║░░██╗██║██║░░██║██║╚████║
        ██║░░░░░██║░░██║╚█████╔╝░░░██║░░░╚██████╔╝██║░░██║██║░░██║╚█████╔╝██║╚█████╔╝██║░╚███║
        ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░╚════╝░╚═╝░░╚══╝ 
       \n""" )
    print("NO. Producto Subtotal" ) 
    for y in Compra:
        registro = registro + 1
        print(str(registro), y ,"", Compra[y])
        Subtotal = Subtotal + Compra[y]
       
    print("El total a pagar es de: "+ str(Subtotal)) 
    print("IVA a pagar: "+str(Subtotal * 0.12))
    

pass



Menu()


    