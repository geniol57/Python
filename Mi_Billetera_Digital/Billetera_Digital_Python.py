import requests
from datetime import datetime

_ENDPOINT = "https://api.binance.com"
nombre_archivo = "transacciones.txt"

class Usuario(object):
    def __init__(self, codigo):
        self.codigo = codigo
    
    def mostrarCodigo(self):
        return self.codigo

class Criptomoneda(object):
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad
    
    def indicarCantidad(self, cantidad):  
        self.cantidad=cantidad

    def mostrarNombre(self):
        return self.nombre
    
    def mostrarCantidad(self):  
        return  self.cantidad
    
    def calcularSaldo(self, cotizacion):  
        return self.cantidad*cotizacion

def _url(api):
    return _ENDPOINT+api

def get_price(cripto):
    data = requests.get(_url("/api/v3/ticker/price?symbol="+cripto)).json()
    precio = float(data["price"])
    return precio

def esmoneda(cripto):
    criptos = ["BTC","BCC","LTC","ETH"]
    if cripto in criptos:
        return True
    else:
        print("Ingrese una moneda válida (BTC,BCC,LTC,ETH)")
        return False

def validarCodigo(codigo):
    if codigo == usuario.codigo:
        print("\n       ¡TRANSACCIÓN FALLÍDA!, el código indicado es inválido")
        return False
    else:
        return True

def cantidadSuficiente(moneda, cantidad):
    aux = True
    if(moneda== "BTC"):
        if(BTC.cantidad >= cantidad):
            return True
        else:
            aux = False
    if(moneda== "ETH"):
        if(ETH.cantidad >= cantidad):
            return True
        else:
            aux = False
    if(moneda== "BCC"):
        if(BCC.cantidad >= cantidad):
            return True
        else:
            aux = False
    if(moneda== "LTC"):
        if(LTC.cantidad >= cantidad):
            return True
        else:
            aux = False
    if(aux==False):
        print("     ¡TRANSACCIÓN RECHAZADA!, Cantidad de "+ moneda+ " es insuficiente")
        return False

def GuardarRegistro(moneda, operacion, codigo, cantidad, cantTotal):
    archivo = open(nombre_archivo,"a")
    dt = datetime.now()
    precio =  get_price(moneda+"USDT")
    archivo.write("\n"+"Fecha"+ ":" + dt.strftime("%A %d/%m/%Y %I:%M:%S%p") +",Moneda" +":"+str(moneda)
        +",Transacción" +":"+ operacion+",Código de usuario"+ ":"+ str(codigo) + ",Cantidad "+ ":"+ str(cantidad) 
            + ",Total de la operación en $"+":"+ str(precio*cantidad) +", Total acumulado en cuenta en $" + ":"+ str(precio*cantTotal))
    archivo.close()
    return

BTC = Criptomoneda("BTC",2.5)
ETH = Criptomoneda("ETH",0.6734)
BCC = Criptomoneda("BCC",8.5)
LTC = Criptomoneda("LTC",7.36)
monedas = [BTC,ETH,BCC,LTC]
usuario = Usuario(2161)

while True:
    print("------------------------------------------------------------")
    print("<<<<<<<<<<<<<<< Billitera Digital tipo Desktop >>>>>>>>>>>>>>>")
    print("------------------------------------------------------------")
    print("Tú código de Usuario es: " + str(usuario.mostrarCodigo()))
    print("Menú de opciones: ")
    print(("1. Recibir Cantidad \n"
        "2. Transferir monto\n"
        "3. Mostrar balance de una moneda\n"
        "4. Mostrar balance general\n"
        "5. Mostrar histórico de transacciones\n"
        "6. Salir del programa"))
    seleccion = int(input("Selecciona opción para continuar:"))

    if(seleccion==1):
        moneda = input("    Ingrese la moneda a recibir: ")
        while not esmoneda(moneda):
            moneda = input("    Ingrese la moneda a recibir: ")
        cantidad = float(input("        Ingrese la cantidad a recibir de " + moneda+ ":"))
        codigo = int(input("        Ingrese el código del emisor: "))
        while not validarCodigo(codigo):
            codigo = int(input("        Ingrese el código del emisor: "))
        if(moneda=="BTC"):
            BTC.indicarCantidad(BTC.cantidad + cantidad)
            GuardarRegistro(moneda,"Recibido",codigo, cantidad, BTC.mostrarCantidad())
        elif(moneda=="ETH"):
            ethe.indicarCantidad(ETH.cantidad + cantidad)
            GuardarRegistro(moneda,"Recibido",codigo, cantidad,ETH.mostrarCantidad())
        elif(moneda=="BCC"):
            BCC.indicarCantidad(BCC.cantidad + cantidad)
            GuardarRegistro(moneda,"Recibido",codigo, cantidad,BCC.mostrarCantidad())
        elif(moneda=="LTC"):
            LTC.indicarCantidad(LTC.cantidad + cantidad)
            GuardarRegistro(moneda,"Recibido",codigo, cantidad,LTC.mostrarCantidad())
        print("\n       ¡TRANSACCIÓN EXITOSA!, El saldo fue añadido correctamente a su billetera")
        

    elif(seleccion==2):
        moneda = input("    Ingrese la moneda a transferir: ")
        while not esmoneda(moneda):
            moneda = input("    Ingrese la moneda a transferir: ")
        cantidad = float(input("        Ingrese la cantidad a transferir de " + moneda+ ":"))
        while not cantidadSuficiente(moneda, cantidad):
            cantidad = float(input("        Ingrese la cantidad a transferir de " + moneda+ ":"))
        codigo = int(input("        Ingrese el código del receptor: "))
        while not validarCodigo(codigo):
            codigo = int(input("        Ingrese el código del receptor: "))
        if(moneda=="BTC"):
            BTC.indicarCantidad(BTC.cantidad - cantidad)
            GuardarRegistro(moneda,"Enviado",codigo, cantidad, BTC.mostrarCantidad())
        elif(moneda=="ETH"):
            ETH.indicarCantidad(ETH.cantidad - cantidad)
            GuardarRegistro(moneda,"Enviado",codigo, cantidad, ETH.mostrarCantidad())
        elif(moneda=="BCC"):
            BCC.indicarCantidad(BCC.cantidad - cantidad)
            GuardarRegistro(moneda,"Enviado",codigo, cantidad, BCC.mostrarCantidad())
        elif(moneda=="LTC"):
            LTC.indicarCantidad(LTC.cantidad - cantidad)
            GuardarRegistro(moneda,"Enviado",codigo, cantidad, LTC.mostrarCantidad())
        print("\n       ¡TRANSACCIÓN EXITOSA!, El saldo fue descontado correctamente de su billetera")
        
    elif(seleccion==3):
        moneda = input("    Ingrese la moneda a consultar: ")
        while not esmoneda(moneda):
            moneda = input("    Ingrese la moneda a consultar: ")
        precio = get_price(moneda+"USDT")
        if(moneda=="BTC"):
            print("Moneda: " + moneda + " Cantidad: "+ str(BTC.mostrarCantidad()) +" Saldo disponible: $."+ str(BTC.calcularSaldo(precio)))
        elif(moneda=="ETH"):
             print("Moneda: " + moneda + " Cantidad: "+str(ETH.mostrarCantidad()) +" Saldo disponible: $."+str(ETH.calcularSaldo(precio)))
        elif(moneda=="BCC"):
             print("Moneda: " + moneda + " Cantidad: "+str(BCC.mostrarCantidad()) + " Saldo disponible: $."+str(BCC.calcularSaldo(precio)))
        elif(moneda=="LTC"):
             print("Moneda: " + moneda + " Cantidad: "+ str(LTC.mostrarCantidad()) +" Saldo disponible: $."+str(LTC.calcularSaldo(precio)))

    elif(seleccion==4):
        moneda = ""
        totalUSD = 0
        for moneda in monedas:
            precio = get_price(moneda.mostrarNombre()+"USDT")
            totalUSD += moneda.calcularSaldo(precio)
            print("Moneda: " + moneda.mostrarNombre() + " Cantidad: "+ str(moneda.mostrarCantidad()) +" Saldo disponible: $."+ str(moneda.calcularSaldo(precio)) +"\n")
        print("El monto acumulado total de todas las criptomonedas es $." + str(totalUSD))

    elif(seleccion==5):
        archivo = open(nombre_archivo,"r")
        texto = archivo.read()
        archivo.close()
        lineas = texto.splitlines()
        print(texto)
    elif(seleccion==6):
        print("\nGracias por usar tu billetera virtual")
        break
    else:
        print("\nPor favor, selecciona una opción válida")