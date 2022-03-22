
while True:
   try:
       x = int(input("Ingrese número entero para dividir por 10: "))
       division = 10/x
       print("10/" + str(x) + " = " + str(division))
       break;
   except ValueError:
       print("EL valor ingresado no es válido. Intente de nuevo...")
   except ZeroDivisionError:
       print("Ingrese un número distinto de cero")

try:
    #c = 5/0       # Si comentas esto entra en TypeError
    d = 2 + "Hola" # Si comentas esto entra en ZeroDivisionError
except ZeroDivisionError:
    print("No se puede dividir entre cero!")
except TypeError:
    print("Problema de tipos!")
