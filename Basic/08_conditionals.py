### Condicionales ###

my_condition = False

if my_condition:
    print("Se ejecuta la condición del if")

my_condition = 5 * 5  ## Se prueba multiplicando 5*3 5*5

if my_condition >= 10 and my_condition <= 20:
    print(f"El valor es: {my_condition} Es mayor de 10 y menor de 20")
elif my_condition == 25:
    print(f"El valor es: {my_condition} es igual a 25")
else:
    print(f"El valor es: {my_condition} No es mayo de 10 and menor a 20 y es distinto de 25")

print("La ejecución continua")

my_string = "Tengo Texto"

if my_string:
    print("La cadena contiene caracteres")

my_string = ""

if not my_string:
    print("La cadena NO contiene caracteres")

  
