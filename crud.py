from tabulate import tabulate
from utilities import clear
from stdiomask import getpass
import sys


def crear(cuentas):
   #Crear registros en el archivo .csv
   
   while True:
    clear()
    while True:
        clear()

        numc = input("Introduzca el numero de cuenta (10 digitos, enter para salir): ")
            
        if numc == "":
            return
      
        if len(numc) == 10 and numc.isdigit():
           break #Sale del bucle de validacion de numc si es valido
        else:
            input("Error: El numero de cuenta debe ser exactamente de 10 digitos y solo contener numeros. Presione enter para reintentar.")

    if numc not in cuentas:
        #Solicita el tipo de cuenta y valida que sea 'ahorro' o 'corriente'.
        while True:
            tipo = input("Ingrese el tipo de cuenta ('ahorro' o 'corriente'): ").lower()
             
            if tipo in ['ahorro', 'corriente']:
                break # Sale del bucle de validacion de tipo si es valido
            else:
                input("Error: El tipo de cuenta debe ser 'ahorro' o 'corriente'. Presione enter para reintentar.")
         
        #Solicita el PIN y valida que sea de 4 digitos.
        while True:
            pin = getpass("Introduzca un PIN (Ha de ser de 4 digitos): ")
             
            if len(pin) == 4 and pin.isdigit():
                break #Sale del bucle de validacion de pin si es valido
            else:
                input("Error: El PIN debe ser exactamente de 4 digitos y solo contener numeros. Presione enter para reintentar.")

        cuentas[numc] = dict(tipo=tipo, pin=pin, saldo=0.0, transacciones=[])

        input("Cuenta creada exitosamente. Presione enter para continuar.")
    else:
        input("La cuenta ya esta registrada. Presione enter para continuar")

def iniseccion(cuentas):
    clear()
    MAX_INTENTOS = 3
    intentos = 0
    print("""\n--- BIENVENIDO, POR FAVOR INICIE SESION ---""")
    while intentos < MAX_INTENTOS:
        intentos_restantes = MAX_INTENTOS - intentos
        print(f"\n--- Le quedan {intentos_restantes} intentos para iniciar sesion ---")

        numc_ingresado = input("Ingrese su numero de cuenta: ")
        # Con esto no apareceran los numeros, sino que apareceran ***
        pin_ingresado = getpass("Ingrese su PIN: ")

        clear()
        # calida la existencia de la cuenta
        if numc_ingresado not in cuentas:
            print(" Error de inicio de sesion: Numero de cuenta no encontrado.")
            intentos += 1
            continue
            
        cuenta = cuentas[numc_ingresado]
        clear()
        
        # Valida el PIN
        if pin_ingresado == cuenta['pin']:
            print(f"\n Inicio de sesion exitoso! Bienvenido, cuenta {numc_ingresado}.")
            return cuenta # Inicio de sesion exitoso, devuelve la cuenta
        else:
            print(" Error de inicio de sesion: PIN incorrecto.")
            intentos += 1

    print(f"\n Ha agotado sus {MAX_INTENTOS} intentos. El programa se cerrara.")
    sys.exit() # Cierra el programa
    
    return None


def listar(cuentas):
   clear()
   
   tabla = []
   
   for numc in cuentas:
      row = [numc, cuentas[numc]['tipo'], cuentas[numc]['pin'], cuentas[numc]['saldo']]
      tabla.append(row)
      
   print(tabulate(tabla, headers=['Numero de Cuenta', 'Tipo', 'Pin', 'Saldo']))
   input("\nPresione enter para continuar")