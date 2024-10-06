### Error Type ###

# SyntaxError

# print "¡Hola comunidad!" # Descomentar para error 
print ("¡Hola comunidad!")

# NameError
language ="Spanish" # Comentar para error 
print(language)

# IndexError
my_list=["Python","Swift","Kotlin","Dart","JavaScript"]

print(my_list[0])
print(my_list[4])
print(my_list[-1])
#print(my_list[5]) # Descomentar para error 

#  ModuleNotFoundError
# import maths # Descomentar para error 
import math

# AttributeError
# print(math.PI) # Descomentar para error 
print(math.pi)

# KeyError
my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}
print(my_dict["Edad"])
#print(my_dict["Apelido"]) # Descomentar para Error
print(my_dict["Apellido"])

# TypeError
# print(my_list["0"]) # Descomentar para Error
print(my_list[0])
print(my_list[False]) # False se traduce a 0 y True a uno 

# ImportError
#from math import PI # Descomentar para Error
from math import pi
print(pi)

# ValueError
#my_int = int("10 Años")
my_int = int("10")  # Descomentar para Error
print(type(my_int))

# ZeroDivisionError
# print(4/0) # Descomentar para Error
print(4/2)

