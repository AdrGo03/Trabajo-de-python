from utilities import clear, guardado
from tabulate import tabulate
import ast
import time

def _obtener_numc(cuenta_logeada, cuentas):
    # Funcion auxiliar para encontrar el numero de cuenta (la llave)
    # asociado al objeto de cuenta (el valor)
    for numc, cuenta in cuentas.items():
        if cuenta is cuenta_logeada:
            return numc
    return "N/A"

def depositar(cuenta_logeada, cuentas):
    """Permite al usuario depositar dinero en su cuenta."""
    clear()
    numc = _obtener_numc(cuenta_logeada, cuentas)
    print(f"\n--- DEPOSITAR en cuenta {numc} ({cuenta_logeada['tipo']}) ---")
    
    while True:
        try:
            monto = float(input("Ingrese el monto a depositar: $"))
            if monto <= 0:
                print("Error: El monto debe ser positivo.")
                input("Presione Enter para reintentar.")
                clear()
                continue
            break
        except ValueError:
            print("Error: Ingrese un monto numerico valido.")
            input("Presione Enter para reintentar.")
            clear()

    # 1. Actualizar saldo
    saldo_actual = float(cuenta_logeada['saldo'])
    nuevo_saldo = saldo_actual + monto
    cuenta_logeada['saldo'] = str(f"{nuevo_saldo:.2f}")

    # 2. Registrar transaccion
    try:
        transacciones_list = ast.literal_eval(cuenta_logeada['transacciones'])
    except:
        transacciones_list = []
        
    fecha = time.strftime("%Y-%m-%d %H:%M:%S")
    transaccion = (fecha, "DEPOSITO", f"+${monto:.2f}", f"${nuevo_saldo:.2f}")
    transacciones_list.append(transaccion)
    cuenta_logeada['transacciones'] = str(transacciones_list)

    # 3. Guardar cambios
    guardado(cuentas)
    print(f"\nDeposito de ${monto:.2f} realizado con exito.")
    print(f"Su nuevo saldo es: ${nuevo_saldo:.2f}")
    input("\nPresione Enter para continuar...")


def retirar(cuenta_logeada, cuentas):
    """Permite al usuario retirar dinero de su cuenta."""
    clear()
    numc = _obtener_numc(cuenta_logeada, cuentas)
    print(f"\n--- RETIRAR de cuenta {numc} ({cuenta_logeada['tipo']}) ---")

    # Validacion para comprobar si la cuenta se encuentra vacia
    saldo_actual = float(cuenta_logeada['saldo'])
    if saldo_actual <= 0.0:
        print("\n**Error: La cuenta está vacía o tiene saldo negativo. No se puede realizar el retiro.**")
        input("\nPresione Enter para continuar...")
        return
    
    while True:
        try:
            monto = float(input("Ingrese el monto a retirar: $"))
            # Valisacion de monto positivo
            if monto <= 0:
                print("Error: El monto debe ser positivo.")
                input("Presione Enter para reintentar.")
                clear()
                continue
            # Validacion de cantidad de saldo
            if monto > saldo_actual:
                print(f"Error: Saldo insuficiente. Su saldo actual es ${saldo_actual:.2f}.")
                input("Presione Enter para reintentar.")
                clear()
                continue
            
            break
        except ValueError:
            print("Error: Ingrese un monto numerico valido.")
            input("Presione Enter para reintentar.")
            clear()

    # 1. Actualizar saldo
    nuevo_saldo = saldo_actual - monto
    cuenta_logeada['saldo'] = str(f"{nuevo_saldo:.2f}")

    # 2. Registrar transaccion
    try:
        transacciones_list = ast.literal_eval(cuenta_logeada['transacciones'])
    except:
        transacciones_list = []
        
    fecha = time.strftime("%Y-%m-%d %H:%M:%S")
    transaccion = (fecha, "RETIRO", f"-${monto:.2f}", f"${nuevo_saldo:.2f}")
    transacciones_list.append(transaccion)
    cuenta_logeada['transacciones'] = str(transacciones_list)

    # 3. Guardar cambios
    guardado(cuentas)
    print(f"\nRetiro de ${monto:.2f} realizado con exito.")
    print(f"Su nuevo saldo es: ${nuevo_saldo:.2f}")
    input("\nPresione Enter para continuar...")


def ver_saldo(cuenta_logeada, cuentas):
    """Muestra el saldo actual de la cuenta."""
    clear()
    numc = _obtener_numc(cuenta_logeada, cuentas)
    saldo = cuenta_logeada.get('saldo', '0.0')
    
    print(f"\n--- SALDO de cuenta {numc} ({cuenta_logeada['tipo']}) ---")
    print(f"\nSu saldo actual es: ${float(saldo):.2f}")
    
    input("\nPresione Enter para continuar...")


def ver_transacciones(cuenta_logeada, cuentas):
    """Muestra la lista de transacciones de la cuenta."""
    clear()
    numc = _obtener_numc(cuenta_logeada, cuentas)
    print(f"\n--- TRANSACCIONES de cuenta {numc} ({cuenta_logeada['tipo']}) ---")
    
    try:
        # Convertir la string de transacciones a una lista de Python
        transacciones_list = ast.literal_eval(cuenta_logeada['transacciones'])
    except:
        transacciones_list = []
    
    if not transacciones_list:
        print("\nNo hay transacciones registradas.")
    else:
        # Preparar datos para tabulate
        # Formato de transaccion: (fecha, tipo, monto, saldo_final)
        headers = ["Fecha y Hora", "Tipo", "Monto", "Saldo Final"]
        
        # Invertir la lista para mostrar la transaccion mas reciente primero
        tabla_datos = [list(t) for t in transacciones_list]
        tabla_datos.reverse()
        
        print(tabulate(tabla_datos, headers=headers, tablefmt="grid"))
        
    input("\nPresione Enter para continuar...")