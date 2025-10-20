import os
import csv

def clear():
   if os.name == "nt":
      _ = os.system('cls')
   else:
      _ = os.system('clear')

def lectura(cuentas):
   
   # Si el archivo no existe lo creamos con el header de los datos
   
   if not os.path.exists('cuentas.csv'):
      with open('cuentas.csv', 'w', newline='', encoding='utf-8') as file:
         writer = csv.writer(file)
         writer.writerow(['numc', 'tipo', 'pin', 'saldo', 'transacciones'])
    
   # Si existe el archivo lo abrimos modo lectura     
   with open('cuentas.csv', newline='', encoding='utf-8') as file:
      reader = csv.DictReader(file)
      for row in reader:
         cuentas[row['numc']] = dict(tipo=row['tipo'], pin=row['pin'], saldo=row['saldo'], transacciones=row['transacciones'])
         
def guardado(cuentas):
   # Guardar datos del dict en el archivo
   with open('cuentas.csv', 'w', newline='', encoding='utf-8') as file:
      writer = csv.writer(file)
      writer.writerow(['numc', 'tipo', 'pin', 'saldo', 'transacciones'])
      for numc in cuentas:
         writer.writerow([numc, cuentas[numc]['tipo'], cuentas[numc]['pin'], cuentas[numc]['saldo'], cuentas[numc]['transacciones']])