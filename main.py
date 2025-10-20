import utilities
import opciones
import crud
import movimientos
from time import sleep

cuentas = {}

if __name__ == "__main__":
   
   utilities.lectura(cuentas)
 
   while True:
      
      opcion = opciones.menu()
      
      match opcion:
         case "1":
            crud.crear(cuentas)
            utilities.guardado(cuentas)
         
         case "2":
            cuenta_logeada = crud.iniseccion(cuentas)

            while True:
               opcion1 = opciones.menu2()
               match opcion1:
                  case "1":
                     movimientos.depositar(cuenta_logeada,cuentas)
                  case "2":
                     movimientos.retirar(cuenta_logeada, cuentas)
                  case "3":
                     movimientos.ver_saldo(cuenta_logeada, cuentas)
                  case "4":
                     movimientos.ver_transacciones(cuenta_logeada, cuentas)
                  case "5":
                     utilities.clear()
                     print("\n Gracias por usar el Banco MAX. ¡Hasta pronto!")
                     sleep(3)
                     break

         case "3":
            crud.listar(cuentas)
         case "4":
            break

         