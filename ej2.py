"""Defina un límite para la cantidad máxima de intentos que el usuario
tiene para ingresar un número de tipo entero de forma correcta,
superada esa cantidad máxima de intentos levante una excepción para que sea manejada por el código invocante.

"""
intentos = 5
while True:

    try:
        int(input("Introducir nro entero: "))
        break
    except TypeError:
        print("Tipo de dato incorrecto")
        intentos -= 1
    except ValueError:
        print("Valor incorrecto")
        intentos -=1
    finally:
        if intentos == 0:
            print("Número máximo de intentos alcanzado")
            break


