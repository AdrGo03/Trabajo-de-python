from utilities import clear
def menu():
    clear()
    print("""-+- BIENVENIDO AL BANCO MAX -+-
       Que desea realizar?\n
1. Crear
2. Iniciar sesion
3. Lista todos
4. Salir
""")
    opcion = input("Selecciona una opción: ")
    return opcion

def menu2():
    clear()
    print("""*** Menu de opciones ****\n
1. Depositar
2. Retirar
3. Consultar saldo
4. Ver transacciones
5. Salir
""")
    opcion1 = input("Selecciona una opción: ")
    return opcion1