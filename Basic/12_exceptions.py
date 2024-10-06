### Exceptions Handling ###
###  Manejo de Errores  ###

numero_uno = 5
numero_dos = 1
numero_dos = "1"

# try except
try:
    print(numero_uno+numero_dos)
    print("NO se ha ocurrio un error !!!")
except:
    print("Ha ocurrio un error !!!")

# try excep else 

try:
    print(numero_uno+numero_dos)
    print("NO se ha ocurrio un error !!!")
except:
    print("Ha ocurrio un error !!!")
else:
    # se ejecuta si no se produce una excepción 
    print("La ejecución continús correctamente")


 # try excep else finally

try:
    print(numero_uno+numero_dos)
    print("NO se ha ocurrio un error !!!")
except:
    print("Ha ocurrio un error !!!")
else:
    # se ejecuta si no se produce una excepción 
    print("La ejecución continús correctamente")
finally:
    # se ejecuta siempre
    print("la ejecución continua")


# excepciones por tipo 
try:
    print(numero_uno+numero_dos)
    print("NO se ha ocurrio un error !!!")
except TypeError:
    print("Ha ocurrio un error !!! TypeError")
except ValueError:
    print("Ha ocurrio un error !!! ValueError")


# Captura de la información de la excepción 
try:
    print(numero_uno+numero_dos)
    print("NO se ha ocurrio un error !!!")
except TypeError as e:
    print("Ha ocurrio un error !!! TypeError")
    print(e)
except Exception as e: #Exception si no se cumple nincuna de las anteriores
    print("Ha ocurrio un error !!")
    print(e)