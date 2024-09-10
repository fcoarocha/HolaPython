### Strings ###
my_strean = "Este es Mi strean"
print(my_strean)

my_other_strean = "Este es mi otro strean"
print(my_other_strean)

print("\t" +my_other_strean+"\n"+my_strean )

name = "Francisco"
surname= "Arocha"
age=47

# Formateo 
print("Mi nombre es {} {} y tengo {}".format(name,surname,age))
print("Mi nombre es %s %s y tengo %d" %(name,surname,age))
print(f"Mi nombre es {name} {surname} y tengo {age}") # Mejor manera 


# Desmpaquetado de caracteres

a, b, c, d, e, f = "Python"

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

texto = "ejemplo"

print(texto.capitalize())
print(texto.count("p"))
print("1".isnumeric())
print(texto.isnumeric())
print(texto.upper().isupper())
print(texto.capitalize().startswith("Ej"))

